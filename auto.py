from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from guppy import hpy


h = hpy()
# print(h.heap())

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])


requiredmovielink = input('Enter the movie link:')


driver = webdriver.Chrome(
    options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get(requiredmovielink)


# Function Definitions

def findtype():
    # //*[@id="the-post"]/div/p/span[2]/a
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="the-post"]/div/p/span[2]/a[2]'))
        )
    except:
        print('Element not found')

    # tags = []
    # for element in elements:
    #     text = element.text
    #     tags.append(text)
    check = element.text
    print(check)

    answer = None
    if 'TV' in check:
        answer = True
    else:
        answer = False

    return answer


def findmegalink():
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[10].get_attribute('outerHTML')
    # print(required)

    modlink1 = required.split(None, 1)
    code = modlink1[0]
    modcode = code[1:]

    onlymegalinks = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div//'+modcode+"[contains(.,'MG')]")

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
    print('skipping agreement')

    try:
        wait = WebDriverWait(driver, 15)
        agree = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'qc-cmp2-consent-info')))

    finally:
        agreement = driver.find_element_by_xpath(
            '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')

        agreement.click()


def skipintercelestial():
    print('Skipping Intercelestial.....')
    firstverfication = driver.find_element_by_xpath(
        '//*[@id="landing"]/div[2]/center/img')

    firstverfication.click()

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


# Running the execution commands
tvormov = findtype()

if (tvormov):
    print('its a show')
else:
    print('its not a show ')
# resolutions = findavalableresolutions()

# for index, item in enumerate(resolutions):
#     print(item+'--------'+str(index+1))


# requestedreso = input(
#     "Enter The Number Assigned To The  Required Resolution: ")


# rightlink = findmegalink()

# rightlink[int(requestedreso)-1].click()


# driver.implicitly_wait(4)


# skipagreement()

# skipintercelestial()


# driver.implicitly_wait(6)


# driver.switch_to.window(driver.window_handles[1])
# driver.implicitly_wait(6)

# skiplinegee()
