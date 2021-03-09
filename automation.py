from selenium import webdriver

chrome_browser= webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

message_button = chrome_browser.find_element_by_class_name('btn-default')

user_message= chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM VEEERRYYY COOOOOOLLLL')
message_button.click()

printed_text = chrome_browser.find_element_by_id('display')
print(printed_text.get_attribute('innerHTML'))

chrome_browser.close()