from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import pytesseract
import cv2
 
options=Options()
options.add_experimental_option("detach",True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ssl-version-min=tls1.2')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
# here we specifiy the exact locatin of google driver after download
s= Service("C:/Users/Shashank Rai/OneDrive/Desktop/chromedriver.exe")
driver=webdriver.Chrome(service=s,options=options)
time.sleep(1)
driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=11089656103618132619&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9302435&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1')

'''
captcha_element = driver.find_element(By.XPATH, value="/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img")
# Take a screenshot of the CAPTCHA and save it
captcha_element.screenshot("captcha.png")
# Load the saved image with OpenCV
image = cv2.imread("captcha.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Save the processed image (optional for debugging)
cv2.imwrite("processed_captcha.png", thresh)

# Extract the CAPTCHA text using Tesseract
captcha_text = pytesseract.image_to_string(thresh, config='--psm 6').strip()
print(f"Extracted CAPTCHA: {captcha_text}")

captcha_input = driver.find_element(By.XPATH, value="/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/input")
captcha_input.send_keys(captcha_text)'''



mobile=driver.find_element(By.XPATH,value="/html/body/div[1]/header/div/div[5]/div[2]/div/div/a[6]")
mobile.click()
time.sleep(1)
phones=driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/ul/li[6]/span/a/span").click()

prime=driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/span/a/div/label/i").click()

old_height =driver.execute_script('return document.body.scrollHeight')
counter =1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    new_height=driver.execute_script('return document.body.scrollHeight')
    print (counter)
    counter+=1
    print('Old Height',old_height)
    print('New Heoght',new_height)
    
    if new_height==old_height:
        break
    old_height=new_height
html=driver.page_source
with open('Amazon.html','w',encoding='utf-8')as f:
    f.write(html)