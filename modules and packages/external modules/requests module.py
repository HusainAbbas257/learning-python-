import requests
# this module helps us interact with websites or whaatever APi is
# we can get data of a wepage by get(url) method
response=requests.get('https://httpbin.org/post')
print(response)
# it has a responce code :
print(response.status_code)
# text value contains actual code of the page:
print(response.text)


# we can give data to a url by post(url,json) method:

url = "https://httpbin.org/post"

data = {
    "username": "Husain bhai",
    "role": "student",
    "language": "Python"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Returned JSON:", response.json())

