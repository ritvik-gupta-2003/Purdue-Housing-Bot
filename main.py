import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from discordwebhook import Discord
from selenium.webdriver.chrome.options import Options

try:
    # Load in the important variables
    discordURL = input("Enter Discord Webhook URL: ")

    # The tools we will use
    discord = Discord(url = discordURL)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Announce that we have begun
    discord.post(content="Webhook Running")
    print("Webhook Running")

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
            discord.post(content="Hilly Available!")
            hilly == True
        if not ("Hillenbrand" in driver.page_source) and hilly:
            discord.post(content="Hilly Gone!")
            hilly == False

        if "Winifred" in driver.page_source and not winifred:
            discord.post(content="Winifred Available!")
            winifred = True
        if not ("Winifred" in driver.page_source) and winifred:
            discord.post(content="Winifred Gone!")
            winifred = False

        if "Frieda" in driver.page_source and not frieda:
            discord.post(content="Frieda Available!")
            frieda = True
        if not ("Frieda" in driver.page_source) and frieda:
            discord.post(content="Frieda Gone!")
            frieda = False

        if "Cary" in driver.page_source and not cary:
            discord.post(content="Cary Available!")
            cary = True
        if not ("Cary" in driver.page_source) and cary:
            discord.post(content="Cary Gone!")
            cary = False
        if "Hawkins" in driver.page_source and not hawkins:
            discord.post(content="Hawkins Available!")
            hawkins == True
        if not ("Hawkins" in driver.page_source) and hawkins:
            discord.post(content="Hawkins Gone!")
            hawkins == False
        if "Earhart" in driver.page_source and not earehart:
            discord.post(content="Earhart Available!")
            earehart == True
        if not ("Earhart" in driver.page_source) and earehart:
            discord.post(content="Earhart Gone!")
            earehart == False

        driver.refresh()
        time.sleep(5)

except Exception as e:
    discord.post(content="Error: " + str(e))
    print("Error: " + str(e))
    driver.quit()
