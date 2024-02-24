from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService 

# Instantiate options
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

# Run browser in headless mode
options.headless = True

# Instantiate driver
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
# Load website
url = 'https://www.indiegogo.com/explore/all?project_type=campaign&project_timing=all&sort=trending'
driver.get(url)

# Define a function to scroll down the page
def scroll_down():
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for some time for the content to load
    sleep(2)

# Scroll down and extract data for 10 scrolls
scroll_count = 0
while scroll_count < 10:
    scroll_down()
    elements = driver.find_elements(By.CLASS_NAME, 'baseDiscoverableCard.baseDiscoverableCardExperiment')
    for title in elements:
        # Select <a> tags within the element
        a_tags = title.find_elements(By.TAG_NAME, 'a')
        for a_tag in a_tags:
            # Extract the href attribute from each <a> tag
            href_content = a_tag.get_attribute('href')
            print(href_content)
            sleep(1)
    scroll_count += 1

# Close the driver
driver.quit()
