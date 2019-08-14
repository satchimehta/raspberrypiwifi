import os
import re
import subprocess
import time
import datetime
import pyrebase
import requests

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = float(ping[0].replace(',', '.'))
download = float(download[0].replace(',', '.'))
upload = float(upload[0].replace(',', '.'))

facebook = requests.get("https://www.facebook.com").elapsed.microseconds/1000.00
reddit = requests.get("https://www.reddit.com").elapsed.microseconds/1000.00
instagram = requests.get("https://www.instagram.com").elapsed.microseconds/1000.00
wikipedia = requests.get("https://www.wikipedia.org").elapsed.microseconds/1000.00
datetime = time.strftime('%m-%d-%y %H:%M')

config = {
  "apiKey": "AIzaSyDUaDWObKlROYbaoKGzU36padtjXLPUhDs",
  "authDomain": "cubs-wifi-raspberry-pi.firebaseapp.com",
  "databaseURL": "https://cubs-wifi-raspberry-pi.firebaseio.com",
  "storageBucket": "cubs-wifi-raspberry-pi.appspot.com",
  "serviceAccount": "/home/pi/serviceAccountCredentials.json"
  }


firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()
uid = "x5mawVsPDmO6zeDu2NFosgGv2Ax2"

custom_token = auth.create_custom_token(uid)

# Log the user in
user = auth.sign_in_with_custom_token(custom_token)

# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "ping(ms)": ping,
    "download(Mbps)": download,
    "upload(Mbps)": upload,
    "facebook(ms)": facebook,
    "instagram(ms)": instagram,
    "reddit(ms)": reddit,
    "wikipedia(ms)": wikipedia
}


# Pass the user's idToken to the push method
results = db.child("Pi 1").child(datetime).set(data, user['idToken'])

print(results)