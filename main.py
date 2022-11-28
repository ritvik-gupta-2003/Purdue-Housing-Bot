import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from discordwebhook import Discord

discord = Discord(url = "https://discordapp.com/api/webhooks/1042691320956858411/XMy93U4dSTN34NPq8qk8k4zGk0Uv391Swfdv-ThBTFs5UD3tSF2KuoARpLXmEBW06Wc4")

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://myhousing.purdue.edu/StarRezPortalX/8D7E8611/1/1/Home-Home")


loginButton = driver.find_element("link text", "Log In")
loginButton.click()

usernameInput = driver.find_element(By.ID, "username")
passwordInput = driver.find_element(By.ID, "password")

time.sleep(0.5)

usernameInput.send_keys("gupta897")
passwordInput.send_keys("2022,push")

time.sleep(1)

submitButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")
submitButton.click()

time.sleep(12)


contractButton = driver.find_element("link text", "Contract Renewal (Renew with University Residences)")
contractButton.click()

time.sleep(3)

continueButton = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[2]/div[2]/button")
continueButton.click()

time.sleep(3)

proceedButton = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[2]/button")
proceedButton.click()

time.sleep(3)

roomSelection = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/section/div/div/div[2]/div/a[7]/div[1]")
roomSelection.click()

time.sleep(3)

changeRoomLink = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/div[7]/div[3]/div/div/span/ul[1]/li/strong[1]/a")
changeRoomLink.click()

time.sleep(3)


condition = True

hilly = False
frieda = False
winifred = False


while (condition):

    if "Hillenbrand" in driver.page_source:

        if hilly == False:
            discord.post(content="Hillenbrand Available!")
            hilly == True

    else:

        if hilly == True:
            discord.post(content="Hillenbrand Gone!")
            hilly == False

    if "Winifred" in driver.page_source:
        discord.post(content="Winifred Parker Available!")

    if "Frieda" in driver.page_source:
        discord.post(content="Frieda Parker Available!")


    driver.refresh()

    time.sleep(3)
