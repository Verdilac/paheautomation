from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()

driver.get('https://pahe.ph')

searchbox = driver.find_element_by_xpath('//*[@id="s-header"]')
searchbox.send_keys('the little')

searchButton = driver.find_element_by_xpath(
    '//*[@id="searchform-header"]/button')

searchButton.click()


movielink = driver.find_element_by_xpath(
    '//*[@id="main-content"]/div[1]/div[2]/div/div/ul[1]/li/div[1]/h2/a')

movielink.click()


megalink = driver.find_element_by_xpath(
    '//*[@id="the-post"]/div/div[2]/div[2]/div/ecfdddbcafbeedab[4]')

megalink.click()

agreement = driver.find_element_by_xpath(
    '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')

agreement.click()

firstverfication = driver.find_element_by_xpath('//*[@id="landing"]')

firstverfication.submit()


driver.implicitly_wait(5)

generatelink = driver.find_element_by_xpath('//*[@id="generater"]')

generatelink.click()

driver.implicitly_wait(6)

downloadlink = driver.find_element_by_xpath('//*[@id="showlink"]')

downloadlink.click()

driver.implicitly_wait(6)


finallink = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div/div[1]/div[3]/center/a')

finallink.click()
