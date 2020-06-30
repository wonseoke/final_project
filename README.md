# Moving Quote Service

Calculates an estimated or minimum quote that you should expect for moving

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/final_project
```

Create and activate a new Anaconda virtual environment, perhaps named "movingquote-env":

```sh
conda create -n movingquote-env python=3.7
conda activate movingquote-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain API Keys from the [Zip Code](hhttps://www.zipcodeapi.com/)
 Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

APP_ENV="development" # or set to "production" on Heroku server

Zip_Key="_______________"
```

> IMPORTANT: remember to save the ".env" file :-D

## Usage

From within the virtual environment, ensure you can run each of the following files and see them produce their desired results of: printing today's weather forecast, and sending an example email, respectively.

```sh
python app/quote_app.py


## Web App Usage

Run the app:
# windows:
set FLASK_APP=web_app
flask run
