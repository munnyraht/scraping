#download resistor images from duckduckgo.com 
import os
import urllib.request
from lxml.html import fromstring
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time


driver = webdriver.Chrome('C://chromedriver.exe') #download a chrome driver and replace this dir with the driver location
driver.get('https://duckduckgo.com/?q=resistor+&t=h_&iax=images&ia=images')#enter the url of the website u which to scrape from


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.0)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if (new_height >=5000):
        break
    last_height = new_height

containers = driver.page_source
soup=bs(driver.page_source,'lxml')
images= soup.findAll('img',{'tile--img__img js-lazyload'}) #selects all image tags with the class='tile--img__img js-lazyload'
os.mkdir('image_s')
for i,image in enumerate(images):
    try:
        component=('https:'+ image['src'])
        urllib.request.urlretrieve(component,r'image_s\resistor'+str(i)+'.jpg')
    except ValueError:
        pass