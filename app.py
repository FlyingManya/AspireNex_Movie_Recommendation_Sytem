from flask import Flask, render_template
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds

app = Flask(__name__)

# Sample data
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'movie_id': [1, 2, 3, 1, 2, 4, 2, 3, 4, 1, 3, 4],
    'rating': [5, 4, 1, 4, 5, 1, 2, 4, 5, 4, 3, 5]
}

df = pd.DataFrame(data)

# Sample movie data
movies = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Dilwale Dulhania Le Jayenge', 'Kabhi Khushi Kabhie Gham', 'Dangal', 'Lagaan', 'Gully Boy'],
    'poster': [
        'static/Pictures/ddlj.jpg',
        'static/Pictures/kabhi khushi kabhi gam poster.jpg',
        'static/Pictures/dangal.jpg',
        'static/Pictures/lagan.jpg',
        'static/Pictures/gully boy poster.jpg'
    ]
}

movies_df = pd.DataFrame(movies)

# Create user-item matrix
user_item_matrix = df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

# Convert to scipy.sparse.csr_matrix
user_item_matrix_sparse = csr_matrix(user_item_matrix.values)

# Normalize by subtracting mean
user_ratings_mean = np.mean(user_item_matrix_sparse, axis=1)
R_demeaned = user_item_matrix_sparse - user_ratings_mean.reshape(-1, 1)

# Perform SVD
U, sigma, Vt = svds(R_demeaned, k=2)

# Convert sigma to diagonal matrix
sigma = np.diag(sigma)

# Reconstruct matrix
all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
preds_df = pd.DataFrame(all_user_predicted_ratings, columns=user_item_matrix.columns)

def recommend_movies(predictions_df, user_id, movies_df, original_ratings_df, num_recommendations=5):
    user_row_number = user_id - 1
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)

    user_data = original_ratings_df[original_ratings_df.user_id == user_id]
    user_full = (user_data.merge(movies_df, how='left', left_on='movie_id', right_on='movie_id').
                 sort_values(['rating'], ascending=False))

    recommendations = (movies_df[~movies_df['movie_id'].isin(user_full['movie_id'])].
                       merge(pd.DataFrame(sorted_user_predictions).reset_index(), how='left',
                             left_on='movie_id',
                             right_on='movie_id').
                       rename(columns={user_row_number: 'Predictions'}).
                       sort_values('Predictions', ascending=False).
                       iloc[:num_recommendations, :-1])

    return user_full, recommendations

@app.route('/')
def index():
    user_id = 1
    already_rated, recommendations = recommend_movies(preds_df, user_id, movies_df, df)
    return render_template('index.html', user_id=user_id, already_rated=already_rated, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
