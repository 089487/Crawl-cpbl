from selenium import webdriver
import re

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Make a GET request to the website
url = 'https://www.cpbl.com.tw/player'
driver.get(url)

# Get the script content as a string
def find_request_token(driver):
    script_content = driver.execute_script("return Array.from(document.getElementsByTagName('script')).map(s => s.textContent).join('\\n');")

    # Use a regular expression to find the RequestVerificationToken in the script content
    pos = script_content.find(r"RequestVerificationToken")
    posl = script_content.find("'", pos)
    posr = script_content.find("'", posl + 1)
    res = script_content[posl:posr]
    if res:
        return res
    else:
        return "Couldn't find the Request Verification Token in the script."

# Call the function
request_token = find_request_token(driver)
print(request_token)

# Don't forget to quit the driver when you're done
driver.quit()