# My Project - Movie Recommendation Generator

## Description
The Movie Recommendation algorithm is designed to provide personalized movie recommendations based on user preferences. It utilizes a dataset of movies, from IMDb top 250 movies, stored in a CSV file, containing information such as movie name, genre, director, rating, release year, duration, and actors.

Features:
* Web Scraping: To create the movie dataset, the algorithm performs web scraping on IMDb's list of top-rated movies. It sends a GET request to the IMDb website, extracts relevant information such as movie name, genre, director, rating, release year, duration, actors, and URL for the movie poster, and adds this data to the dataset.

* Data Loading: The algorithm loads the movie dataset using the Pandas library, creating a DataFrame that can be easily manipulated and queried.

* Preference Weighting: Each user preference (genre, director, rating, release year, duration, actors) is assigned a weight, indicating its importance in the recommendation process. These weights are defined in a dictionary, allowing for easy customization.

* Recommendation Calculation: For each movie in the dataset, the algorithm calculates a final score based on the user's preferences and the corresponding weights. The score is determined by comparing the movie's attributes with the user's preferences, using various comparison functions such as exact match, closest match, numeric comparison, and range comparison.

* Top Movie Selection: After calculating scores for all movies, the algorithm selects the top five highest-scoring movies to recommend to the user. These movies represent the best matches for the user's preferences.

* The project has 4 files:
1. `database.py`- creates the database using web scraping.
2. `movies.csv`- the movies' database.
3. `movie_algorithm.py`- runs the recommendation algorithm and returns the top 5           recommended movies
4. `GUI_create.py`- creates a graphical user interface (GUI) application using Tkinter.
Users can input their movie preferences through labeled comboboxes and entry fields, and the application retrieves and displays movie recommendations based on these preferences.



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

* To see the posters,and run `database.py` you must have an internet connection.
* All fields are optional.



