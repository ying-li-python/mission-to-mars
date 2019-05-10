# Mission to Mars
Interested in how web scraping works as a web app? Great!

The purpose of this project is to build a Flask application that scrapes data from various websites of the red planet, Mars. 

## Installations required 
- [Mongo](https://docs.mongodb.com/manual/installation/)
- [Flask](http://flask.pocoo.org/), [flask_PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [splinter](https://splinter.readthedocs.io/en/latest/install.html), [Pandas](https://pandas.pydata.org), [requests](https://2.python-requests.org//en/v2.7.0/user/install/)
- [Google Chrome](https://www.google.com/chrome/)
- [Jupyter Notebook](https://jupyter.org/) (optional, for looking at testing the script)

## Getting started
1. Run the mongo server in terminal to initialize a local connection.
```
$ monogod
```

2. In a new terminal window, download the project and go into the directory. Run the script.
```
$ cd mission-to-mars
$ python app.py
```

3. Open a new window in Google Chrome and type in http://localhost:5000

4. Click on the "Scrape New Data" button and you should see the results as shown below:

<img src="https://raw.githubusercontent.com/ying-li-python/mission-to-mars/master/Images/example1.png">
<img src="https://raw.githubusercontent.com/ying-li-python/mission-to-mars/master/Images/example2.png" height="80%" width="80%">

Enjoy!

## Author
Ying Li
