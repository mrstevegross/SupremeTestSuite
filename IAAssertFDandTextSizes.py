from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import xlrd
import time
import unittest
import os
from IAVariables import workbookNameData
from pyvirtualdisplay import Display

# Test verifies the Future Info Toolbar buttons are fully functional

# Required Function For Working With Jenkins Virtual Machine

workbook = xlrd.open_workbook(workbookNameData)
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
adjustResolution = worksheet.cell(1, 3).value

def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()


if adjustResolution == 1:
    AdjustResolution()


class Verify_Future_Dates_And_Text_Sizes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1800, 1100)
        self.driver.get(url)

    def test_Future_Info_Toolbar_Is_Active(self):

        driver = self.driver

        time.sleep(3)
        loginElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'timeFrameSelectorDiv')))

        driver.find_element_by_id('timeFrameSelectorDiv').click()

        assert driver.find_element_by_id('timeFrameSelectorDiv').is_enabled()

        assert driver.find_element_by_id('smallTextLnk').is_enabled()

        assert driver.find_element_by_id('normalTextLnk').is_enabled()

        assert driver.find_element_by_id('largeTextLnk').is_enabled()

        assert driver.find_element_by_id('textOnlySiteLinkSpan').is_enabled()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

