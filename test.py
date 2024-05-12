from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开页面
driver.get("https://www.cpbl.com.tw/player")

try:
    # 等待直到关键字输入框出现
    keyword_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )

    # 输入关键字
    keyword_input.send_keys("潘威倫")

    # 等待一段时间确保自动完成请求完成
    driver.implicitly_wait(5)

    # 执行JavaScript代码，模拟选择第一个自动完成结果
    driver.execute_script("$('.ui-autocomplete li:first-child a').click()")

finally:
    # 关闭WebDriver
    driver.quit()
