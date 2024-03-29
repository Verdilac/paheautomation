from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from guppy import hpy
import time


h = hpy()
# print(h.heap())

options = webdriver.ChromeOptions()
options.add_argument("window-size=1200x600")
# options.add_argument('headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])


requiredmovielink = input('Enter the movie link:')


driver = webdriver.Chrome(
    options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')

driver.maximize_window()

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
    finally:
        elems = driver.find_elements_by_xpath(
            '//*[@id="the-post"]/div/p/span[2]/a')
    # tags = []
    # for element in elements:
    #     text = element.text
    #     tags.append(text)

    answer = False
    is_Ongoing = False

    # check = element.text
    # print(check)

    for elem in elems:
        check = elem.text
        if 'TV' in check:
            answer = True
        if 'Ongoing' in check:
            is_Ongoing = True

    # if 'TV' in check:
    #     answer = True
    # else:
    #     answer = False

    return answer, is_Ongoing


def showepisodes():
    episodes = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/ul/li')

    for epi in episodes:
        text = epi.text
        print(text)

    requiredepisode = input('Enter the required Episode:')

    driver.implicitly_wait(5)
    episodes[int(requiredepisode)-1].click()

    return requiredepisode


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


def findmegalinkshow(epinum):
    megalinks = driver.find_elements_by_class_name("shortc-button")
    required = megalinks[2].get_attribute('outerHTML')
    # print(required)

    modlink1 = required.split(None, 1)
    code = modlink1[0]
    modcode = code[1:]

    onlymegalinks = driver.find_elements_by_xpath(
        '//*[@id="the-post"]/div/div[2]/div[2]/div[2]/div/div//'+modcode+"[contains(.,'MG')]")

    # i had to take the full xpath because most of the recent episodes were coverd
    # by a wrapper element so the element i wanted to interact with was not
    # clickable hence the use of full x paths.

    # i also had to implement the episode number in to the full expath
    # keep in mind since we are using full xpath its not relative so
    # any sudden changed on the website will need maintatnce on the script
    fullxmegalinks = driver.find_elements_by_xpath(
        '/html/body/div[1]/div[2]/div/div[1]/div[1]/article/div/div[2]/div[2]/div[' + epinum + ']/div/div//'+modcode+"[contains(.,'MG')]")

    return fullxmegalinks


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


def episoderesolutions(epinum):

    # driver.implicitly_wait(10)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="the-post"]/div/div[2]/div[2]/div[1]/div/div/strong[1]'))
        )
    except:
        print('Element not found')
    finally:
        allstrongs = driver.find_elements_by_xpath(
            '//*[@id="the-post"]/div/div[2]/div[2]/div[' + epinum + ']/div/div/strong')

    resolutionsettings = []

    for res in allstrongs:
        text = res.text
        resolutionsettings.append(text)

    return resolutionsettings


def skipagreement():
    print('skipping agreement')

    try:
        wait = WebDriverWait(driver, 15)
        agree = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'qc-cmp2-consent-info')))

    except:
        print('element not found')
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


def closelatesttab():
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])


def seasonstack():
    seasons = driver.find_elements_by_xpath("//li[contains(text(), 'Season')]")

    for s in seasons:
        t = s.text
        print(t)
    requiredseason = input('Enter the Required Season:')

    seasons[1].click()


# checking the functionality of find type keepin for furture tests
if (tvormov):
    print('its a show')

    is_Ongoing = False
    if (tvormov[1]):
        is_Ongoing = True
    else:
        is_Ongoing = False

    if not is_Ongoing:
        seasonstack()
        closelatesttab()
    #this is not very used these days 
    #to be continued


    else:
        epinum = showepisodes()

        closelatesttab()
        time.sleep(5)
        tvresolutions = episoderesolutions(epinum)

        for index, item in enumerate(tvresolutions):
            print(item+'--------'+str(index+1))

        megalinks = findmegalinkshow(epinum)

        wantedtvres = input(
            "Enter The Number Assigned To The  Required Resolution: ")

        megalinks[int(wantedtvres)-1].click()

        driver.implicitly_wait(6)

        skipagreement()

        skipintercelestial()

        driver.implicitly_wait(6)

        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(6)

        skiplinegee()


else:

    print('its not a show ')
    resolutions = findavalableresolutions()

    for index, item in enumerate(resolutions):
        print(item+'--------'+str(index+1))

    requestedreso = input(
        "Enter The Number Assigned To The  Required Resolution: ")

    rightlink = findmegalink()

    rightlink[int(requestedreso)-1].click()

    driver.implicitly_wait(4)

    skipagreement()

    skipintercelestial()

    driver.implicitly_wait(6)

    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(6)

    skiplinegee()
