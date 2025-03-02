#Selenium use here for Automation 

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
#options.add_argument("--incognito")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

# ChromeDriver setup can download from net and use it
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# Google open karein
driver.get('http://google.com')
time.sleep(2)

# Search karein
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('learnwithCampusX')
search_box.send_keys(Keys.RETURN)
time.sleep(2)

link0=driver.find_element(By.XPATH,value='/html/body/div[3]/div/div[12]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/div[2]/cite')
link0.click()

link1=driver.find_element(By.XPATH,value="/html/body/div[1]/header/section[2]/a[1]")
link1.click()

link2=driver.find_element(By.XPATH,value='/html/body/div[2]/div/div[3]/div[2]/a')
link2.click()
# Close mat karein, jab tak manually na band karein
