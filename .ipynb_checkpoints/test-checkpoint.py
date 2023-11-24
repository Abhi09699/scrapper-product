from selenium import webdriver

driver = webdriver.Chrome(executable_path="chrome.exe")

driver.get("https://www.youtube.com/")
print(driver.title)
