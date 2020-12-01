import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import schedule



class LinkedinBot:
    def __init__(self, username, password, recruiterName, company):
        """ Initialized Chromedriver, sets common urls, username and password for user """



        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(executable_path='/Users/tpat/PycharmProjects/Linkedin_Bot/chromedriver2',
                                  options=chrome_options)

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password
        self.recruiterName = recruiterName
        self.company = company

    def _nav(self, url):
        self.driver.get(url)
        # time.sleep(3/)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def connect(self):
        self.driver.find_element_by_class_name('pv-s-profile-actions__overflow').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('pv-s-profile-actions--connect').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('artdeco-button--3').click()





    def sendMessage(self,recruiterName, company):
        message = ''

        self.driver.find_element_by_xpath('//*[@id="custom-message"]').click()
        self.driver.find_element_by_xpath('//*[@id="custom-message"]').send_keys(message)
        self.driver.find_element_by_class_name('artdeco-button--primary').click()







if __name__ == '__main__':

    username = ''
    password = ''
    database = pd.read_csv('data.csv', delimiter=',')

    data = (np.array(database[['Searched Company', 'Name', 'Linkedin Link']]))


    
    inc =lambda i: i + 1
    

    i = 0
    while True:
        company = data[i][0]
        recruiterName = data[i][1].split()[0]
        url = data[i][2]


        try:
            bot = LinkedinBot(username, password, recruiterName, company)
            bot.login(username, password)
            bot._nav(url)
            bot.connect()
            bot.sendMessage(recruiterName, company)
            i += 1
            print("Current Recruiter: {} {}% Done".format(recruiterName, round(i / 2135)))

        except Exception:
            i += 1
            print("Current Recruiter: {} {}% Done".format(recruiterName, round(i / 2135)))




