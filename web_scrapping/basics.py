import bs4
import requests as rq
# request helps us fetch data from websites
# beutifulsoup helps to scrap it(get what we want)

# first we nee to select a webpage
url='http://httpbin.org/html'
# then we have to get its data by get()
response=rq.get(url)

# now we have to create a soup of html to parse it into python
# bs4 is a noob he cant read through html so we have to giuve it some encoding which is lxml.idk what it is but it helps to decode that html
# pip install lxml
# to create a soupe we nead to create a bs4 object with argument:text of response of page and a encoding like lxml
soup=bs4.BeautifulSoup(response.text,'lxml')

# now soup contains encoded html file
# now to select a perticular element we use select(tag) function
# it returns a special iterable containing all the occurence of that tag
print(soup.select('h1'))  #this gives ---->[<h1>Herman Melville - Moby-Dick</h1>]
print(soup.select('title')) #this gives ---->[] coz there is no title tag in the page

# now if you still want only the text inside a perticulat tag u can use
for data in soup.select('h1'):
    text_h1=data.get_text()
    print('data inside h1:',text_h1)