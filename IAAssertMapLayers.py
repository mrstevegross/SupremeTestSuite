# coding=utf-8
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import xlrd
from pprint import pprint
from IAVariables import workbookNameData
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-

# Required function for making test work in Jenkins
def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

workbook = xlrd.open_workbook(workbookNameData)
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == 1:
    AdjustResolution()

verifyMapLayersWorksheet = workbook.sheet_by_index(1)

# Lists for holding Map Layer Data from Spreadsheet
itemText = []
itemLink = []
itemXpath = []

# Loop to gather all relevant info for drop down layers
for x in range (0, 13):
    itemText.append(verifyMapLayersWorksheet.cell(x + 1, 1).value)
    itemXpath.append(verifyMapLayersWorksheet.cell(x + 1, 2).value)

# Function to verify drop down layers
def Verify_Layer_Drop_Down_Item(driver, xPath, itemText):
    item = driver.find_element_by_xpath(xPath)
    itemHTML = item.get_attribute('innerHTML')
    if (itemText in itemHTML):
        return True
    else:
        return False

# Unit test for reporting status of test back to team
class Verify_Map_Layers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()


    def test_presence_of_correct_layers(self):
        driver = self.driver

        dropDownMenuWait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'layers-menu-dropdown-button')))
        driver.find_element_by_id('layers-menu-dropdown-button').click()

        itemWait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layerSelector"]/ul/li[1]/a/span/img[1]')))
        # 1. First Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[0], itemText[0]), (itemText[0] + " Is Faulty")
        # 2. Second Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[1], itemText[1]), (itemText[1] + " Is Faulty")
        # 3. Third Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[2], itemText[2]), (itemText[2] + " Is Faulty")
        # 4. Fourth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[3], itemText[3]), (itemText[3] + " Is Faulty")
        # 5. Fifth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[4], itemText[4]), (itemText[4] + " Is Faulty")
        # 6. Sixth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[5], itemText[5]), (itemText[5] + " Is Faulty")
        # 7. Seventh Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[6], itemText[6]), (itemText[6] + " Is Faulty")
        # 8. Eighth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[7], itemText[7]), (itemText[7] + " Is Faulty")
        # 9. Ninth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[8], itemText[8]), (itemText[8] + " Is Faulty")
        # 10. Tenth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[9], itemText[9]), (itemText[9] + " Is Faulty")
        # 11. Eleventh Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[10], itemText[10]), (itemText[10] + " Is Faulty")
        # 12. Twelfth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[11], itemText[11]), (itemText[11] + " Is Faulty")
        # 12. Thirteenth Item Verification
        assert Verify_Layer_Drop_Down_Item(driver, itemXpath[12], itemText[12]), (itemText[12] + " Is Faulty")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    print ('\n') + "Verifying TG Web Map Layers" + '\n'
    unittest.main()