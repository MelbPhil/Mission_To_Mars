# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Import Pandas 
import pandas as pd

# Set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Setup the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# ##### Assign the title and summary text to variables

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[7]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[12]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[13]:


# convert DF to html
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[14]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[15]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Parse the resulting html with soup
html = browser.html
hemi_soup = soup(html, 'html.parser')
results = hemi_soup.find_all('div', class_='description')

for result in results:
    
    # Use first word of titles to find links
    title = result.find('h3').text
    browser.links.find_by_partial_text(title).click()
    
    # Set up HTML parser again
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    
    href = hemi_soup.find('a', text='Sample')['href']
    hemisphere_image_urls.append(
        {'img_url': url + href, 
         'title': title})
    browser.back()


# In[16]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# ### End the automated browsing session

# In[17]:


# 5
browser.quit()

