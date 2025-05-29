import bs4
import requests as r

# repeating the steps we learned before
url='https://en.wikipedia.org/wiki/Python_(programming_language)'
res=r.get(url)
soup=bs4.BeautifulSoup(res.text,'lxml')


# we dont want all images including logo etc we just want all the real images
# with a little analysis of the page i saw all the images belonged to a class->mw-file-elements
all_img=soup.select('.mw-file-element')
i=1#this will help us in iteration
# now i am running a loop to access each img tag
for img in all_img:
    src=img['src'] #this accesses the source of the image which is a link
    # now i have to send a get request to the source to get its responce
    response=r.get(f'https:{src}')#raw src doesnt contain 
    data=response.content#now this contains the actual data of the image in byte form
    # to download the image we have to write its data into a file
    with open(f'C:/Users/DELL/Desktop/learning-python-/web_scrapping/images/img_{i}.jpg','wb') as f:#wb means write as binary
        f.write(data)
    i+=1
    

