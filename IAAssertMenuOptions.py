# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
import time
import unittest
import xlrd
from pyvirtualdisplay import Display
from IAVariables import workbookNameData
# -*- coding: utf-8 -*-


def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

workbook = xlrd.open_workbook(workbookNameData)
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == 1:
    AdjustResolution()

class Verify_Menu_Options(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)


    def test_Menu_Options(self):

        driver = self.driver

        # Login To The System
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sign-in-link')))
        driver.find_element_by_id('sign-in-link').click()
        driver.find_element_by_id('userAccountEmail').send_keys(username)
        driver.find_element_by_id('userAccountPassword').send_keys(password)
        driver.find_element_by_id('userAccountPassword').submit()

        # Check that the menu items are all present
        left_Panel_Wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Ryan’s Favorites"]')))
        # 1
        assert (driver.find_element_by_xpath('//*[@title="Ryan’s Favorites"]').is_enabled()) == True, "Favorites Is Faulty"
        # 2
        assert driver.find_element_by_xpath("//*[contains(text(), 'Travel At-A-Glance')]").is_enabled(), "Travel At-A-Glance Is Faulty"
        # 3
        assert driver.find_element_by_xpath('//*[@title="Incidents"]').is_enabled(), "Incidents Is Faulty"
        # 4
        assert driver.find_element_by_xpath('//*[@title="Construction"]').is_enabled(), "Construction Are Faulty"
        # 5
        assert driver.find_element_by_xpath('//*[@title="Winter Driving & Incidents"]').is_enabled(), "Winter Driving & Incidents Are Faulty"
        # 6
        assert driver.find_element_by_xpath('//*[@title="Cameras & Speeds"]').is_enabled(), "Cameras & Speeds Are Faulty"
        # 7
        assert driver.find_element_by_xpath("//*[contains(text(), 'Twitter')]").is_enabled(), "Twitter not present"
        # 8
        assert driver.find_element_by_xpath("//*[contains(text(), 'Facebook')]").is_enabled(), "Facebook not present"

    def tearDown(self):
         self.driver.quit()


if __name__ == '__main__':
    unittest.main()
