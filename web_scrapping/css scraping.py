import bs4
import requests as r

# repeating the steps we learned before
url='https://www.scrapethissite.com/pages/simple/'
res=r.get(url)
soup=bs4.BeautifulSoup(res.text,'lxml')

# as we know we can scrap all headings from a page as:
for i in range(1,7):
    for data in soup.select(f'h{i}'):
        text_h=data.get_text()
        print(f'data inside h{i}:{text_h.strip()}')

# we can also use the select() function to get css elements but we have to use some special encodings:
# select('#some_id')->gives all elements with id some_id
# select('.some_cl')->gives all elements with class some_cl
# select('div abc')->gives all div with abc in them
# select('div > abc')->gives all div with abc directly  in them


# this prints all tha data inside the tags that have class country_name
for country in soup.select('.country-name'):
    print(country.get_text().strip(),end='\t')

print(soup.select('#footer'))# this gives all the tags that have id="footer"

print(soup.select('div h3')) #gives eevery h3 that is indside a div
print(soup.select('div > h3')) #gives eevery h3 that is directly inside a div