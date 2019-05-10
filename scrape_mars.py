'''
This script contains three core functions to web scraping the data regarding
Mars from multiple web sources.

Expected results:
1) The first function initializes chromedriver
2) The second function returns majority of the web scraping
3) The third function returns a dataframe of a table of Mars facts

These functions are called when Flask app runs. 
'''

from bs4 import BeautifulSoup
from splinter import Browser

import pandas as pd
import requests
import time


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    posts = {}

    # time delay
    time.sleep(10) 
    
    # scrape Mars News
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    news_soup = BeautifulSoup(response.text, 'lxml')
    news_title = news_soup.find('div', class_='slide').find('div', class_='content_title').text
    news_title = news_title.strip()
    news_p = news_soup.find('div', class_='slide').find('div', class_='rollover_description_inner').text
    news_p = news_p.strip()

    # scrape JPL Mars - Featured Image
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    featured_img_link = image_soup.find('div', class_='carousel_items').find('a', class_="button fancybox").get('data-fancybox-href')
    featured_img_url = 'https://www.jpl.nasa.gov' + featured_img_link 


    # # scrape Mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    weather_soup = BeautifulSoup(response.text, 'lxml')
    mars_weather = weather_soup.find('div', class_="js-tweet-text-container").text

    # # scrape Mars Hemispheres
    valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    valles_response = requests.get(valles_url)
    valles_soup = BeautifulSoup(valles_response.text, 'lxml')
    valles_img_link = valles_soup.find('div', class_="wide-image-wrapper").find('a').get('href')

    syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    syrtis_response = requests.get(syrtis_url)
    syrtis_soup = BeautifulSoup(syrtis_response.text, 'lxml')
    syrtis_img_link = syrtis_soup.find('div', class_="wide-image-wrapper").find('a').get('href')

    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    cerberus_response = requests.get(cerberus_url)
    cerberus_soup = BeautifulSoup(cerberus_response.text, 'lxml')
    cerberus_img_link = cerberus_soup.find('div', class_="wide-image-wrapper").find('a').get('href')

    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    schiaparelli_response = requests.get(schiaparelli_url)
    schiaparelli_soup = BeautifulSoup(schiaparelli_response.text, 'lxml')
    schiaparelli_img_link = schiaparelli_soup.find('div', class_="wide-image-wrapper").find('a').get('href')

    browser.quit()

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_img_link},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_img_link},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_img_link},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_img_link},
        ]
    
    posts["latest_news_title"] = news_title
    posts["latest_news"] = news_p
    posts["featured_image"] = featured_img_url
    posts["mars_weather"] = mars_weather
    posts["hemisphere"] = hemisphere_image_urls

    return posts

def scrape_table():
    # scrape Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Value']
    df.set_index('Description', inplace=True)
    return df
