from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# driverlocation = 'C:\\\\ProgramData\chocolatey\bin\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome()

# driver.get('https://pahe.ph')

# searchbox = driver.find_element_by_xpath('//*[@id="s-header"]')
# searchbox.send_keys('the little')

# searchButton = driver.find_element_by_xpath(
#     '//*[@id="searchform-header"]/button')
# searchButton.click()


# movielink = driver.find_element_by_xpath(
#     '//*[@id="main-content"]/div[1]/div[2]/div/div/ul[1]/li/div[1]/h2/a')


# movielink.click()


# # megalink = driver.find_element_by_xpath(
# #     '//*[@id="the-post"]/div/div[2]/div[2]/div/name()')

# driver.implicitly_wait(5)

requiredmovielink = input('Enter the movie link:')


driver = webdriver.Chrome(
    options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get(requiredmovielink)


def findmegalink():
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[10].get_attribute('outerHTML')

    linkmod1 = required[:17]
    linkmod2 = linkmod1[1:]
    linkmod2.strip()

    onlymegalinks = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div//'+linkmod2 + "[contains(., 'MG')]")

    # for link in onlymegalinks:
    #     i = link.get_attribute('outerHTML')
    #     print(i)

    return onlymegalinks


def findavalableresolutions():
    strongscount = len(driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div/strong'))

    allstrongs = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div/strong')

    resolutionsettings = []

    for res in allstrongs:
        text = res.text

        resolutionsettings.append(text)

    # testing
    # for i in resolutionsettings:
    #     print(i)

    # print(strongscount)
    # print(type(resolutionsettings))
    # print('---------------------')
    # print(resolutionsettings[2])
    return resolutionsettings


resolutions = findavalableresolutions()

for index, item in enumerate(resolutions):
    print(item+'--------'+str(index+1))


requestedreso = input(
    "Enter The Number Assigned To The  Required Resolution: ")


rightlink = findmegalink()

rightlink[int(requestedreso)-1].click()
