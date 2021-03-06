'''
-----------------------------------------------------------------------
The Below Script Shows A Python Script That Sends Weather Information
As Windows Notification. It is build using several python packages.
Result: At The End If You Run the Python Script it will automatically
scrapes the weather information and shows it as a window notification.

(C) 2021 Abhayparashar31
-----------------------------------------------------------------------
Author - Abhay Parashar
Follow Him On Medium - abhayparashar31.medium.com
------------------------------------------------------------------------
Read The Related Article From Here
https://medium.com/pythoneers/python-script-that-sends-weather-information-as-notification-693aca5edc90

'''

from bs4 import BeautifulSoup
import requests
import time
from win10toast import ToastNotifier


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    current_time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    information = f"{location} \n {current_time} \n {info} \n {weather} °C "
        
    toaster = ToastNotifier()
    toaster.show_toast("Weather Information",
    f"{information}",
    duration=10,
    threaded=True)
    while toaster.notification_active(): time.sleep(0.005)   


# print("enter the city name")
# city=input()
city = "Jaipur"
city=city+" weather"
weather(city)
