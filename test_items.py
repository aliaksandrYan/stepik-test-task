import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestStepik(object):
    def test_existence_of_add_button(self,browser):
        browser.get(link)
        #time.sleep(30)
        isButton = True
        try:
            button = browser.find_element_by_css_selector(".btn-add-to-basket")
            print("This is text of button " + button.text)
        except:
            isButton = False
        assert isButton == True, "Adding button not found!"
