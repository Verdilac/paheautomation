from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# driverlocation = 'C:\\\\ProgramData\chocolatey\bin\chromedriver.exe'
options = webdriver.ChromeOptions()
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


# megalink = driver.find_element_by_xpath(
#     '//*[@id="the-post"]/div/div[2]/div[2]/div/name()')

driver.implicitly_wait(5)


def findmegalink():
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[10].get_attribute('outerHTML')
   

    linkmod1 = required[:16]
    linkmod2 = linkmod1[1:]


    actuallink = driver.find_element_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div/'+linkmod2 + '[10]')

    return actuallink


findmegalink().click()
