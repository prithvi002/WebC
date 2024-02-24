from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# instantiate options 
options = webdriver.ChromeOptions() 
options.add_argument('ignore-certificate-errors')


 
# run browser in headless mode 
options.headless = True 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
# load website 
url = 'https://www.indiegogo.com/explore/all?project_type=campaign&project_timing=all&sort=trending' 

print("getting the website content")
# get the entire website content 
driver.get(url) 
print("Waiting for the page to load")
try:
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CLASS_NAME, 'baseDiscoverableCard.baseDiscoverableCardExperiment')))
except Exception as e:
    print("Check the below error\n:", e)

    

 
# # select elements by class name 
# elements = driver.find_elements(By.CLASS_NAME, 'baseDiscoverableCard baseDiscoverableCardExperiment') 
# for title in elements: 
# 	# select H2s, within element, by tag name 
# 	heading = title.find_element(By.TAG_NAME, 'h2').text 
# 	# print H2s 
# 	print(heading)
sleep(2)

url_list = []
elements = driver.find_elements(By.CLASS_NAME, 'baseDiscoverableCard.baseDiscoverableCardExperiment')
print(len(elements))
for title in elements: 
    # select <a> tags within the element
    
    a_tags = title.find_elements(By.TAG_NAME, 'a')
    for a_tag in a_tags:
        # extract the href attribute from each <a> tag
        href_content = a_tag.get_attribute('href')
        url_list.append(href_content)

        print(href_content)
        sleep(1)

print("writing the urls to a file")
# Sample list

# Open a file in write mode
with open('urls_list.txt', 'w') as file:
    # Iterate over the list
    for item in url_list:
        # Write each item to the file followed by a newline character
        file.write(item + '\n')

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
          element = WebDriverWait(driver, 10).until(
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

        
        



# Funding info	Funded
# 	Amount requested (USD)
# 	Amount raised (USD)
# 	Percent funded (%)
# 	Number of investors
# 	Project duration (days)
# Project-details	Number of certificates
# 	Number of projects by the fundraiser
# 	Number of comments
# 	Region info
# 	- Provide video
# 	- Provide tags
# 	- Provide description
# 	- Length of title
# 	- Length of tags
# 	- Length of description
# Project categories	Charity/ Music/ Film/ Game
# Project description	As complete as possible (unstructured data