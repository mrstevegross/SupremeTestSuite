# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import time
import unittest
import xlrd
import requests
from IAVariables import workbookNameData
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-

# /Users/ryankavanaugh/Desktop/AmazonIA/

def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

workbook = xlrd.open_workbook(workbookNameData)
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

# Pull data from spreadsheet to compare against web page
legendDataWS = workbook.sheet_by_index(2)
legendData = []
# Range of spreadsheet *Check For Each Agency*
for x in range (1, 8):
    legendData.append(legendDataWS.cell(x, 0).value)

if adjustResolution == 1:
    AdjustResolution()


class Verify_Legend_Data(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def test_Legend_Data_Text(self):
        driver = self.driver

        searchButonWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'mapLegend')))
        mapLegend = driver.find_element_by_id('mapLegend')

        # Assert the legend is hidden initially
        mapLegendDisplay = driver.find_element_by_id('legendContent')
        assert (mapLegendDisplay.get_attribute('style') == 'display: none;')

        # Assert the map legend button is displayed and can be expanded
        assert (mapLegend.is_displayed())
        legendButton = driver.find_element_by_xpath("//*[@title='Toggle Legend']")
        legendButton.click()

        # Verify the correct data is in the map legend
        legendContent = driver.find_element_by_id('legendContent')
        pageData = legendContent.get_attribute("innerHTML")

        # Range: *Check For Each Agency*
        for indexNumber in range (0, 7):
            word = legendData[indexNumber]
            assert word in pageData


    def test_Map_Legend_Icons(self):
        driver = self.driver
        testCounter = 0
        searchButonWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'mapLegend')))
        for w in range(0, 7):
            imageLink = driver.find_element_by_xpath("//*[@alt='{0} icon']".format(legendData[w])).get_attribute('src')
            # print imageLink
            requestForlink = requests.get(imageLink)
            statusCode = requestForlink.status_code
            # print statusCode

            if statusCode != 200:
                print 'This link is down:'
                print imageLink
                testCounter += 1

            if testCounter >0:
                assert False


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()