'''
Welcome! The purpose of this project is to perform web scraping 
of Mars news, facts, and information from several sources. 

To observe how the web scraping script was built, see the 
Jupyter Notebook file. 

To run the flask app:
- You must start the Mongo daemon in terminal: 
$ mongod 

- Run the script:
$ python app.py 

Open a new window in Chrome and type in: 
http://localhost:5000

Try out the web scrape! Enjoy!
'''

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd 
from scrape_mars import scrape_table

app = Flask(__name__, template_folder='templates')

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    posts = mongo.db.mars_scrape.find_one()
    df = scrape_table()
    return render_template('index.html', posts=posts, tables = [df.to_html(classes='data', header=True)])

@app.route("/scrape")
def scraper():
    posts = mongo.db.mars_scrape
    post_data = scrape_mars.scrape()
    posts.update({}, post_data, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__': 
    app.run(debug=True)