import bs4
import requests as r

bn=1
# repeating the steps we learned before
# this site isnt normal it consists of 50 pages and 20 books in each page 
# having its own price rating and picture and title
# we hav to find a way to go through each page and store all tha data of each book in a large list of dictionary of data
data=[]
# after doing some research i found out to get to the next page we need its url and the urls in a pattern
for i in range(1,51):#to run through all 50 pages

    url=f'https://books.toscrape.com/catalogue/page-{i}.html'
    res=r.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    # grabbing all data from this page:
    # all the books have their own page to get its url we need to analyze the page a little 
    # so all the links of books are in their pictur and have a common class .image_container
    link_tags=soup.select('.image_container > a') #this gives every file with this class which an a tag directly in it
    # now iterating through each book's page
    for book in link_tags:
        br=r.get(f'https://books.toscrape.com/catalogue/{book['href']}')
        print(f'https://books.toscrape.com/catalogue/{book['href']}')
        booksoup=bs4.BeautifulSoup(br.text,'lxml')
        # now we have to get the data :
        #1.we will get title of the book which is in the first h1 of div
        title=booksoup.select('div > h1')[0].getText()
        # print(title)
        #2.  now going to price it is in a para of class price_color
        price=booksoup.select('.price_color')[0].getText()[2:]  #i will slice it and leave the first element coz its a currency symbol
        # print(price)
        #3. now gonna get it avilibility which is in a class 'instock.availibility'
        instock=booksoup.select('.instock.availability')[0].getText().strip()
        # print(instock)
        #4.now comes the rating which is in the class name actually:
        # now first looking at the class name it is compounded (two classed) first 'star-rating' second is the actual rating out of five
        # we can use get_attribute_list('class') to get class of all the elements that belong to class 'star-rating' as:
        rating=booksoup.select('.star-rating')[0].get_attribute_list('class')[1]  #eg ['star-rating', 'Three'] so we select second element
        # print(rating)
        # 5 now we have to get its picture which is inside class 'item active'
        imgsrc=booksoup.select('.item.active img')[0]['src']
        # this src contains some thing at it starting so we would slice it off
        imgr=r.get(f'https://books.toscrape.com/{imgsrc[6:]}')
        img=imgr.content

        # now i want to make a folder for every book that is here
        import os
        path=f'C:/Users/DELL/Desktop/learning-python-/web_scrapping/books/book{bn}'
        os.mkdir(path)
        bn+=1
        # now i want to save everything to that folder
        with open(f'{path}/data.txt','w',encoding='utf-8') as f:
            f.write(f'title:{title};\nprice:{price};\navailability:{instock};\nrating out of five:{rating};\n    ')
        with open(f'{path}/cover.jpg','wb') as f:
            f.write(img)
        # next we will put all the data into a dictionary and append it to the main list
        dic={'title':title,'price':float(price),'availability':instock,'star rating':rating}
        data.append(dic)

    



    