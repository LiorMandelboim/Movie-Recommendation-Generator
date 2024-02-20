# My Project - Movie Recommendation Generator

## Description
This project recommends movies to a user, from IMDb top 250 movies, based on his preferences (rating, movie genre, the length of a movie, relevent years, director and actor).
the project has 4 files:
1. database.py- creates the database using web scraping.
2. movies.csv- the local database that was created in database.py, and used for selecting the best suitable movie for the user.
3. movie_algorithm.py- the backend file of the program: this class withdraws the information from movies.csv, and uses weights dictionary, which gets a different weight for every preference of the user and eventually calculates the movie final score and creates a list of the top 5 movies.
4. GUI_create.py- this class creates the GUI using Tkinter library. the class contains several more classes when each one creates a different kind of label. At the end of the program it shows the best recommended movies by order, with posters.

## Installation
- Step 1: clone the repository-
    Run the following command
    ```
    git clone https://github.com/LiorMandelboim/Tondo
   ```
- Step 2: Install dependencies-
    Run the following command
    ```
    pip install -r requirements.txt 
    ```
- Step 3: Activate the program-
    run the following command
    ```
    python GUI_create.py
    ```

* To see the posters,and run database.py you must have an internet connection.
* All fields are optional.



