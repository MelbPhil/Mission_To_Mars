# Mission_To_Mars
Using Web Scraping to keep updated on the latest developments on NASA's mission to mars.

## Overview of Mission_To_Mars
This week I created a web app that scrapes the latest data on Mars from multiple active websites leveraging my new knowledge of HTML and CSS. The data was then stored on a Mongo databse, and then I used a web application to display the data, and altered the design of the web app to accomodate the images and data.

## Resources
- Data Sources: Web-scraping
- Python: 3.7.13, Jupyter Notebook
- MongoDB
- Flask


## Analysis Results
This week I learned the basic structures of websites, and how to create my own. With some simple HTML, and the necessary data stored in my Mongo database, I was able to create the following:

![Mission_to_Mars](https://user-images.githubusercontent.com/106599446/183228886-624da85c-095a-4461-8794-4396b5f79062.png)

As you can see, the site includes the latest article on Mars, the featured image from the article, and some basic Mars & Earth facts.
Finally, I was able to pull images of each of the four Mars hemispheres.
Most importantly, clicking the button at the top "Scrape New Data" will pull the latest information from the websites in the 'scraping.py' script. As these websites get updated with new information, my app / website will be capable of portraying these latest results. 

The only concern that would cause my app / website to break, is if the source websites get updated structurally, in this situation, my code would be looking for data that no longer exists.
