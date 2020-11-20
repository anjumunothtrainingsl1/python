import requests

serverUrl="https://jsonplaceholder.typicode.com/posts/1"

myData={
    "empId":101,
    "empName":"Sara"
}
response =requests.delete(serverUrl)
print(response)
print("Response status",response.status_code)
print("Response content in json ",response.json())
print("Response content in text ",response.text)
