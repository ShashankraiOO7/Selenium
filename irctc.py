from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ssl-version-min=tls1.2')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")


# Initialize driver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# Open IRCTC login page
driver.get('https://www.irctc.co.in/nget/train-search')
time.sleep(1)
menu=driver.find_element(By.XPATH,value="/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]")
menu.click()
# Click on login button
login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/div[3]/p-sidebar/div/nav/div/label")
login_button.click()
time.sleep(1)

# Enter username
username_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/input")
username_input.send_keys("Raishashnk")  # Replace with your IRCTC username

# Enter password
password_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[3]/input")
password_input.send_keys("Srk275305@")  # Replace with your IRCTC password
time.sleep(10)
# Pause to manually enter captcha (optional)
'''captcha_input = driver.find_element(By.ID, "captcha")
captcha_value = input("aLbgt ")
captcha_input.send_keys(captcha_value)'''

# Click login
submit_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/span/button")
submit_button.click()
time.sleep(1)

# After login, fill in train search details
input0 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input")
input0.send_keys('MAU JN - MAU')
#time.sleep(1)
input0.send_keys(Keys.TAB)

input1 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input")
input1.send_keys('ANAND VIHAR TRM - ANVT')
time.sleep(0.5)
input1.send_keys(Keys.TAB)

input3 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
input3.clear()
input3.send_keys('05/03/2025')
input1.send_keys(Keys.TAB)
time.sleep(2)
input4 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div[1]")
input4.click()
