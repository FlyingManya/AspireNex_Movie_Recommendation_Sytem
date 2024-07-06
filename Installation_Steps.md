1. Create a virtual environment.
2. Setup flask project.
3. static, templates, app.py
4. execute `npm init -y` to create package.json file.
5. execute `npm install tailwindcss postcss autoprefixer` to install tailwindcss.
6. execute `npx tailwindcss init -p` to create tailwind.config.js file.
7. create two folder in css named `src` and `css`.
8. create a file named `main.css` in `css` folder. (compiled css) we do not care about this file, automatically generated.
9. create a file named `input.css` in `src` folder. The actual tailwindcss file.
10. add `@tailwind base; @tailwind components; @tailwind utilities;` in `input.css` file.
12. 
11. Add the below command in `package.json` file.
```json
"tailwind": "npx tailwindcss -i ./static/src/input.css -o ./static/css/main.css --watch"
```
12. In postcss.config.js file, add the below code.
```js
module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    // Add more plugins as needed
  ]
}
```
14. In tailwind.config.js file, add the below code.
```js
module.exports = {
  content: [
    './templates/.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
12. execute `npm run tailwind` to compile tailwindcss, in one terminal.
13. execute `python app.py` to run the server, in another terminal.
