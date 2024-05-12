from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def crawl_website():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Go to the website
    driver.get("https://www.cpbl.com.tw/player")

    # Wait until the input field with id "keyword" is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "keyword")))

    # Find the input field by id
    input_field = driver.find_element(By.ID, "keyword")

    s=input("Please input the name you want to search: ")
    # Send keys to the input field
    input_field.send_keys(s)

    # Wait until the elements with class name "logo" are present
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "logo")))

    # Find all elements with the class name "logo"
    logos = driver.find_elements(By.CLASS_NAME, "logo")

    # Print the alt attribute of each logo (which usually contains the name)
    for logo in logos:
        print(logo.get_attribute("alt"))

    # Close the driver
    driver.close()

if __name__ == "__main__":
    crawl_website()