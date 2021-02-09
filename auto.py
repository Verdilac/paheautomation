from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def findmegalink():
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[10].get_attribute('outerHTML')

    linkmod1 = required[:16]
    linkmod2 = linkmod1[1:]

    actuallink = driver.find_element_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div/'+linkmod2 + '[10]')

    return actuallink


driver = webdriver.Chrome()

driver.get('https://pahe.ph')

searchbox = driver.find_element_by_xpath('//*[@id="s-header"]')
searchbox.send_keys('the little')

searchButton = driver.find_element_by_xpath(
    '//*[@id="searchform-header"]/button')

searchButton.click()

driver.implicitly_wait(5)

driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])


movielink = driver.find_element_by_xpath(
    '//*[@id="main-content"]/div[1]/div[2]/div/div/ul[1]/li/div[1]/h2/a')

movielink.click()


findmegalink().click()


driver.implicitly_wait(10)

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


driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(6)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

finallink = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div/div[1]/div[3]/center/a')


finallink.click()
