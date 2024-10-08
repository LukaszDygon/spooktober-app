### About
Halloween 2k20 means no parties this year, so to get into the festive spirit, I decided to create a big, fun list of
spooky films to watch. One a day for each day of October.

This project allows easy creation of a compact web app, containing posters and information for your list
of films. I am planning to print mine as a poster. Kind of a poster poster.

![poster poster](https://github.com/LukaszDygon/spooktober-app/blob/master/spooktober.png)

### Run instructions

1. Create a `input.csv` file containing pipe `|` separated list of movies you want included, with optional year (to avoid ambiguity)

    e.g. 
    ```csv name: input.csv
    Shining|
    The Silence of the Lambs|
    Godzilla|1954
    Them!|1954
   ``` 
   *N.B. 35 is a perfect number of films if you would like to print them in an A1 format*
2. Get a free TMDb key from https://www.themoviedb.org/settings/api. It usually arrives quickly.
3. Run `pip install -r requirements.txt` to install python requirements (using virtual environment is recommended)
4. Run `python tmdb.py --key { your key } --input {your input file} --shuffle` to download movie data
5. Run `python -m flask run` to start the server
6. (Optional if you would like a big nice image) In browser, for Chrome
*Print > set destination to **"Save as PDF"** > change paper size in "More settings" to something big like **A1***
