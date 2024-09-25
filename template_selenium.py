import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.options import Options
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

web_options = Options()
web_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=web_options)
# driver = webdriver.Firefox(options=web_options)
# driver = webdriver.Chrome(options=web_options)

action = ActionChains(driver)

website = 'https://www.google.com'
driver.get(website)

driver.maximize_window()

wait = WebDriverWait(driver, 60)