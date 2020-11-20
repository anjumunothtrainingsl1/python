import requests

serverUrl="https://jsonplaceholder.typicode.com/posts"

myData={
    "empId":101,
    "empName":"Sara"
}
response =requests.post(serverUrl,data=myData)
print(response)
print("Response status",response.status_code)
print("Response content in json ",response.json())
print("Response content in text ",response.text)
