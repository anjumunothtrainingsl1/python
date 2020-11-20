import requests
 # get Asking for some data
 #post save some data
 #delete delete some data
 #put - update some existing data
serverUrl="https://jsonplaceholder.typicode.com/posts"

requests.get(serverUrl , params={"bookId":101})

response=requests.get(serverUrl)
print(response)
print(response.content)
print(response.json())
print("Header info",response.headers)
for item in response.headers.keys():
    print(item ," : ", response.headers[item])
print("Status code",response.status_code)
print("Status code message",response.reason)

print(response.text)
print("Cookies",response.cookies)
for cookie in response.cookies:
    print(cookie)