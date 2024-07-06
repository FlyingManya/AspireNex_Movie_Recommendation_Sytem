# MOVIE RECOMMENDATION SYSTEM
***Greetings Everyone🌻, This is my Movie Recommendation System built using Flask and Python***<br>

*This task was assigned by AspireNex for the Artificial Intelligence Internship Selection Process*.<br>
<hr>

**TASK 2 - RECOMMENDATION SYSTEM**<br>
<p>Create a simple recommendation system that suggests items to users based on their preferences.
You can use techniques like collaborative filtering or content-based filtering to recommend movies, books, or products to users.</p>

<hr>
<br>

![RSys](https://github.com/FlyingManya/AspireNex_Movie_Recommendation_Sytem/assets/98754211/7ee53dbc-bcb0-47df-b007-9d65f92ac3de)
<br>
*This project is a movie recommendation system built using Flask, Python, and AI techniques like Singular Value Decomposition (SVD) for recommendations.The frontend is designed using HTML,
CSS (Tailwind), and JavaScript.*
<br>

## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="60" height="60"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="60" height="60"/></a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="50" height="60"/></a> </p>
<br>

# CODE EXPLANATION
*Let’s take a quick look at how the code works*

## app.py
**Data Handling and Flask Setup:**
*The movie recommendation system is built using Flask, a lightweight web framework for Python*<br>

- **Data Preparation:**
    *The sample data and movie data are defined using dictionaries and converted to Pandas DataFrames.*
     ![Data](https://github.com/FlyingManya/AspireNex_Movie_Recommendation_Sytem/assets/98754211/8f7c3955-61a6-4b35-9ac3-3f57faa41977)
    <br>
- **User-Item Matrix Creation:**
   *A pivot table is created to form the user-item matrix, which is then converted to a sparse matrix format.*

- **Normalization:**
   *The user-item matrix is normalized by subtracting the mean rating for each user.*

- **Singular Value Decomposition (SVD):**
   *SVD is performed on the normalized matrix to decompose it into three matrices (U, Sigma, Vt).*
    ![SVD](https://github.com/FlyingManya/AspireNex_Movie_Recommendation_Sytem/assets/98754211/7d73c39c-aa24-4367-a99a-48d8cfad94b4)

- **Prediction Generation:**
  *The decomposed matrices are used to reconstruct the original matrix, generating predicted ratings for all users.*

- **Recommendation Function:**
  *A function `recommend_movies` is defined to generate movie recommendations for a specific user based on the predicted ratings.*
 
- **Flask Route:**
  *The `/` route renders the `index.html` template with the recommended and already rated movies for a sample user.*<br>

## static
- **main.css:** Contains the CSS styles used to customize the appearance and layout of HTML elements in the project.
- **pictures:** Directory containing movie posters.
- **input.css:** Tailwind CSS input file.

## templates
- **index.html:** This HTML file serves as the main template for your web application, defining the structure and content that Flask will render and serve to users.

## Other Files
- **package-lock.json:** Auto-generated file that holds the exact versions of dependencies.
- **package.json:** Holds the metadata for the project and dependencies for Tailwind CSS.
- **postcss.config.js:** Configuration for PostCSS.
- **tailwind.config.js:** Configuration file for Tailwind CSS.
<br>

## Running the Code
After cloning the repository, open the project in your code editor.<br>
Navigate to the terminal and execute the following command to start the Flask server:
<br>
<br>

![run](https://github.com/FlyingManya/AspireNex_Movie_Recommendation_Sytem/assets/98754211/d1d704e1-4ca1-4eae-8ae9-4c754477ab78)
<br>

# CONCLUSION
*In summary, this movie recommendation system effectively suggests movies to users based on their preferences using Singular Value Decomposition (SVD).<br>
It normalizes user ratings, decomposes the user-item matrix, and generates personalized recommendations.<br>
Moving forward, I plan to enhance its capabilities further by integrating more advanced collaborative filtering techniques.<br>
Thank you for visiting!*

<br>
<br>
<br>

<br>
<image align="right" alt="coding" width="250" src="https://github.com/FlyingManya/FlyingManya/assets/98754211/0a854199-b287-4dca-a4cc-8265cbd3335e" alt="flyingmanya"></p>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/flyingmanya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="flyingmanya" height="30" width="40" /></a>
<a href="https://instagram.com/flying_manya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="flying_manya" height="30" width="40" /></a>
<a href="https://www.leetcode.com/flying_manya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="flying_manya" height="30" width="40" /></a>
</p>

🌵 https://gautamrajputmanya.wixsite.com/mysite 

📫 *gautamrajputmanya@gmail.com*
