import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ssl-version-min=tls1.2')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

s = Service('C:/Users/Shashank Rai/OneDrive/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

# Using the given XPath

driver.find_element(By.XPATH, '/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]').click()

old_height = driver.execute_script('return document.body.scrollHeight')
counter = 1

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    print(counter)
    counter += 1
    print('Old Height:', old_height)
    print('New Height:', new_height)
    
    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source

with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Page saved successfully!")

driver.quit()
