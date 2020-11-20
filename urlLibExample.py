import urllib.request
# serverUrl="https://www.online.citibank.co.in/"
# requestURl=urllib.request.urlopen(serverUrl)
# print(requestURl.read())
# serverUrl="https://jsonplaceholder.typicode.com/posts"
# requestURl=urllib.request.urlopen(serverUrl)
# print(requestURl.read())

from urllib.parse import *
parseUrl=urlparse("https://jsonplaceholder.typicode.com/posts?fname=sara&lname=khan")
print("Parsed url",parseUrl)

splitUrl=urlsplit("https://jsonplaceholder.typicode.com/posts?fname=sara&lname=khan")
print("Split url",splitUrl)
# create a url ; join the various comp to get a url
joinedUrl=urlunparse(parseUrl);
print(joinedUrl)



