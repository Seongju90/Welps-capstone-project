# Welp

Welp is a clone of Yelp. At first it was used for restaurants, but now it has grown to cover all business reviews.

Visit [Welp](https://welp-o2rq.onrender.com)

## Index

[MVP Feature List](https://github.com/Seongju90/Welps-capstone-project/wiki/MVP-Features-List)
[Database Schema](https://github.com/Seongju90/Welps-capstone-project/wiki/Database-Schema)
[User Stories](https://github.com/Seongju90/Welps-capstone-project/wiki/User-Stories)
[Wire Frames](https://github.com/Seongju90/Welps-capstone-project/wiki/Wireframes)

## Technologies Used
### Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
### Backend
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
### Host
![Render](https://img.shields.io/badge/render-%4351e8.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Getting Started

1. Clone this repository from: ```https://github.com/Seongju90/Welps-capstone-project```

2. Install dependencies into the backend:
    ```bash
    pipenv install -r requirements.txt
    ```

3. Install dependcies into the frontend:
    ```
    npm install
    ```
4. Create a **.env** file with proper settings for development environment

5. Make sure the Sqlite3 database connection URL is in the **.env** file

6. Get into your pipenv, migrate the database, seed the database, then run the flask app:
   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

7. Create another terminal and cd into react-app then start the app:
    ```
    npm start
    ```

# Features

## Restaurants
* Users can create a restaurant
* Users can edit/delete their own restaurant on my profile page
* Users can view a list of restaurants
* Users can navigate to a single restaurant page

## Reviews
* Users can create a review
* Users can edit/delete a review
* Users can view a list of their own reviews on my profile page
* Users can view reviews of restaurants on the single restaurant page
* Users can see 6 random reviews on the splash page

# Future Features

## Search
* Users will be able to have a search function to search for restaurants
## Restaurant Images
* Users will be able to add Images to their restaurant
## Google Maps API
* Users will be able to locate the spot of restaurant using Google API Map
## AWS upload
* Users can upload images using AWS instead of loading urls
