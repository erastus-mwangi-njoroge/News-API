# News-API
An application that help list and preview news articles from various sources using News API key.   

## Author

[Erastus Njoroge](https://github.com/indomitable-core)

## Description

This project is a Flask application that consumes the [News API](https://newsapi.org/) and displays real time articles from major media stations all over the world.

## User Stories

You will be able to see:

- news sources
- Select any article
- Select the top news articles from that various article sites
- Click on an article and read it fully from the news source

## Installation / Setup instruction

#### The application requires the following installations to operate

- python3.9
- virtualenv(name of environment)
- pip

#### Set Up

- Open Terminal {Ctrl+Alt+T}

- git clone `https://github.com/indomitable-core/News-API`

- cd into the news_article folder/preferred folder

- create a virtual environment using the command `$ virtualenv venv`

- enter the virtual environment by typing `source venv\bin\activate`

- install all dependencies using `pip install -r requirements.txt`

- create an instance/config.py file
- assign your news api key to the variable ARTICLE_API_KEY

### Running the Application

- To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py

- To run tests for the application
  $ python3 article_test.py
  $ python3 source_test.py

## Technologies Used

- python3.8.10
- html
- css
- flask
- heroku cli

## Known Bugs

- The app may have server bugs (Error 503) that will be worked upon

## Contact Information

If you have any question or contributions, please email me at [eramwangiz@gmail.com]

## License

- _MIT License:_
- Copyright (c) 2021 **Erastus Njoroge**