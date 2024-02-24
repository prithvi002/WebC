#import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# instantiate options
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
# run browser in headless mode
options.headless = True
# instantiate driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


print("reading the urls from the file and parsing the content")
# Open the file in read mode
with open('urls_list.txt', 'r') as file:
    # Read all the lines into a list
    lines = file.readlines()
    # Iterate over the list
    for line in lines:
        # Print each line
        # create a code to parse the content of each url and print the content
      print(line)
      driver.get(line)
      sleep(2)
      print(driver.title)
      # get the entire website content 
      #driver.get(url) 
      print("Waiting for the page to load")
      try:
          element = WebDriverWait(driver, 1).until(
              EC.presence_of_element_located((By.CLASS_NAME, 'basicsSection-title')))
      except Exception as e:
          print("Check the below error\n:", e)
      # select elements by class name 
      elements = driver.find_elements(By.CLASS_NAME, 'basicsSection-title') 
      for title in elements: 
          # select H2s, within element, by tag name 
          # print H2s 
          print(title.text)
      sleep(2)