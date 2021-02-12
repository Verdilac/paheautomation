from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])


requiredmovielink = input('Enter the movie link:')


driver = webdriver.Chrome(
    options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get(requiredmovielink)


# Function Definitions

def findmegalink():
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[10].get_attribute('outerHTML')

    linkmod1 = required[:17]
    linkmod2 = linkmod1[1:]
    finallinkmod = linkmod2.strip()

    onlymegalinks = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div//'+finallinkmod+"[contains(.,'MG')]")

    return onlymegalinks


def findavalableresolutions():
    print('Searching For Avalable Resolutions....')
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


def skipagreement():
    agreement = driver.find_element_by_xpath(
        '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')

    agreement.click()


def skipintercelestial():
    print('Skipping Intercelestial.....')
    firstverfication = driver.find_element_by_xpath('//*[@id="landing"]')

    firstverfication.submit()

    driver.implicitly_wait(5)

    generatelink = driver.find_element_by_xpath('//*[@id="generater"]')

    generatelink.click()

    driver.implicitly_wait(6)

    downloadlink = driver.find_element_by_xpath('//*[@id="showlink"]')

    downloadlink.click()


def skiplinegee():
    print('Finalizing....')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    finallink = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div/div[1]/div/div[1]/div[3]/center/a')

    finallink.click()
    megaurl = driver.current_url
    print('Requested Mega Url:  '+megaurl)


resolutions = findavalableresolutions()

for index, item in enumerate(resolutions):
    print(item+'--------'+str(index+1))


requestedreso = input(
    "Enter The Number Assigned To The  Required Resolution: ")


rightlink = findmegalink()

rightlink[int(requestedreso)-1].click()


driver.implicitly_wait(10)


skipagreement()

skipintercelestial()


driver.implicitly_wait(6)


driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(6)


skiplinegee()
