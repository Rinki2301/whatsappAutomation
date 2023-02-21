from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here. 

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from re import fullmatch
import time
import pandas as pd
from selenium.webdriver.common.by import By  

from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome('chromedriver.exe') 

def home(request):
    v = (request.GET.get('loginbtn'))
    return render(request,"Whatsapp_App\home.html")

def loginPage(request):
    driver.get('https://web.whatsapp.com/')
    return render(request,"Whatsapp_App\message.html")

def WhatsappAutomation(message, imgPath):
    
    img_path = "C:/Users/Hp/Desktop/LearnDjango/whatsapp/static/images/internship.jpeg"

    wait=WebDriverWait(driver,1000)
    def read_excel(path_to_file):
        df = pd.read_excel(path_to_file)
        return df

    def dataframe_to_dict(df, key_column, value_column):
        name_email_dict = df.set_index(key_column)[value_column].to_dict()
        return name_email_dict

    #excel file path
    path_to_file = r"leads.xlsx"
    df = read_excel(path_to_file)
    name_email_dict = dataframe_to_dict(df,'Name','Contact')
    print(name_email_dict)

    a = 1
    notvalid=[]
    for i in name_email_dict:

        print(f'{a}. {i}. Sending message to: {name_email_dict[i]}')
        
        # Goes to site
        try:
            site = f"https://web.whatsapp.com/send?phone=91{name_email_dict[i]}&text={quote(message)}"
            driver.get(site)

            # Uses XPATH to find a send button
            element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")

            # Waits until send is found (in case of login)
            loaded = WebDriverWait(driver, 1000).until(method=element, message="User never signed in")

            # Loads a send button
            driver.implicitly_wait(10)
            send = element(driver)[0]

            # Clicks the send button
            send.click()
            print(f'Message Sent')

            attachment_section = driver.find_element(By.XPATH, '//div[@title = "Attach"]')
            attachment_section.click()
            image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(img_path)
            time.sleep(8)
            send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            send_button.click()
            print(f'Image Sent')
            print('    ')
        except:
            notvalid.append(name_email_dict[i])
            print("error")
        # Sleeps for 5 secs to allow time for text to send before closing window
        time.sleep(5) 
        a = a + 1 

def SendData(request): 
     Msg = request.POST['Message'] 
     ImgPath= request.POST['imagePath']
    #  file_data = request.FILES['excelfile']

     print(ImgPath)
     WhatsappAutomation(Msg,ImgPath)
     return render(request,"Whatsapp_App\home.html")
