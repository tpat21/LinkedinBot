import pandas as pd
import numpy as np
from selenium import webdriver



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path='/Users/tpat/PycharmProjects/Linkedin_Bot/chromedriver2',options=chrome_options)



driver.get('https://www.linkedin.com')