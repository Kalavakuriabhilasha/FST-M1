from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https://v1.training-support.net/selenium/dynamic-controls")
    print("The page title is: ", driver.title)
    print(driver.find_element(By.XPATH, "//input[@class='willDisappear']").is_displayed())
    driver.find_element(By.ID, "toggleCheckbox").click()
    print(driver.find_element(By.XPATH, "//input[@class='willDisappear']").is_displayed())
    driver.quit()