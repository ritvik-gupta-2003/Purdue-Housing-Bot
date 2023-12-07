import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from discordwebhook import Discord
from selenium.webdriver.chrome.options import Options

# Function to log to the console and discord
def log(message):
    print(message)
    discord.post(content=message)

try:
    # Load in the important variables
    discordURL = input("Enter Discord Webhook URL: ")

    # The tools we will use
    global discord 
    discord = Discord(url = discordURL)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Announce that we have begun
    log("Webhook Running")

    # State variables to prevent multiple notifications
    hilly = False
    frieda = False
    winifred = False
    cary = False
    hawkins = False
    earehart = False

    input(
    """
    Please log in to the housing portal and navigate
    to the list of available dorms. Then,
    press enter to begin monitoring...
    """)

    while (True):
        # Alerts for appearances and disappearances
        if "Hillenbrand" in driver.page_source and not hilly:
            log("Hilly Available!")
            hilly == True
        if not ("Hillenbrand" in driver.page_source) and hilly:
            log("Hilly Gone!")
            hilly == False

        if "Winifred" in driver.page_source and not winifred:
            log("Winifred Available!")
            winifred = True
        if not ("Winifred" in driver.page_source) and winifred:
            log("Winifred Gone!")
            winifred = False

        if "Frieda" in driver.page_source and not frieda:
            log("Frieda Available!")
            frieda = True
        if not ("Frieda" in driver.page_source) and frieda:
            log("Frieda Gone!")
            frieda = False

        if "Cary" in driver.page_source and not cary:
            log("Cary Available!")
            cary = True
        if not ("Cary" in driver.page_source) and cary:
            log("Cary Gone!")
            cary = False
        if "Hawkins" in driver.page_source and not hawkins:
            log("Hawkins Available!")
            hawkins == True
        if not ("Hawkins" in driver.page_source) and hawkins:
            log("Hawkins Gone!")
            hawkins == False
        if "Earhart" in driver.page_source and not earehart:
            log("Earhart Available!")
            earehart == True
        if not ("Earhart" in driver.page_source) and earehart:
            log("Earhart Gone!")
            earehart == False

        driver.refresh()
        time.sleep(5)

except Exception as e:
    discord.post(content="Error: " + str(e))
    print("Error: " + str(e))
    driver.quit()
