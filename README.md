# Purdue-Housing-Bot

Uses Selenium and a webdriver to monitor the housing option menu after the user manually logs in. It will then constantly refresh the page, looking for acceptable housing options after which it will send a message in a Discord channel using a Discord Webhook Integration

**NOTE:** During its busiest times, the housing option menu takes approximately 12 seconds to load, and another 20 to actually fetch the housing data. If this is the case, it's possible that the refersh rate of this script will be too aggressive to actually catch housing options. Use at your own risk, therefore, and modify to your own liking.
