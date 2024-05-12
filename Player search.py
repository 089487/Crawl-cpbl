from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import time
def find_verify_token(driver):
    script_content = driver.execute_script("return Array.from(document.getElementsByTagName('script')).map(s => s.textContent).join('\\n');")

    # Use a regular expression to find the RequestVerificationToken in the script content
    pos = script_content.find(r"RequestVerificationToken")
    posl = script_content.find("'", pos)
    posr = script_content.find("'", posl + 1)
    res = script_content[posl+1:posr]
    if res:
        return res
    else:
        return "Couldn't find the Request Verification Token in the script."
def search_player(name):
    # Create a new instance of the Chrome driver
    

    # Go to the website
    driver.get("https://www.cpbl.com.tw/player")

    # Wait until the page is fully loaded
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

    # Retrieve the CSRF token. This depends on how the token is stored.
    # This is just an example. You might need to adjust this part.
    #csrf_token = driver.get_cookie('RequestVerificationToken')['value']
    verify_token = find_verify_token(driver)
    cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
    print(verify_token)
    print(cookie_string)
    url = 'https://www.cpbl.com.tw/player/searchplayers'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie_string,
        'Origin': 'https://www.cpbl.com.tw',
        'Referer': 'https://www.cpbl.com.tw/player',
        'Requestverificationtoken': verify_token,
        'Sec-Ch-Ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Gpc': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'Keyword': name
    }

    response = requests.post(url, headers=headers, data=data)

    import brotli

    if response.status_code == 200:
        # Decompress the response content with Brotli
        #response_content = brotli.decompress(response.content).decode('utf-8')
        #print(response_content)
        players = response.json()
        Playerurl = {}
        for player in players['Items']:
            Playerurl[player['Name']]='https://www.cpbl.com.tw/team/person?acnt='+player['Acnt']
        return Playerurl
    else:
        print(f"Request failed with status code {response.status_code}")
    time.sleep(1)
    

if __name__ == "__main__":
    driver = webdriver.Chrome()
    name = input("Please input the name you want to search: ")
    res=search_player(name)
    if res:
        url = res[name]
        driver.get(url)
        time.sleep(5)
    else:
        print("No player URL found.")
    driver.close()