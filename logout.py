from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print(input('Press any key.'))
log_out = driver.find_elements_by_class_name('rAUz7')
log_out[2].click()
pp = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
pp.click()