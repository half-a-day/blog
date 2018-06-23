from selenium import webdriver

browser = webdriver.Opera()

browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close() 