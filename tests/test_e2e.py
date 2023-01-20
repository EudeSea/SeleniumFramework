import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage

class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItem()

        #checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getProductTitles()

       # confirmPage = ConfirmPage(self.driver)
        i = -1

        for product in products:
            i = i + 1
            productName = product.text
            if productName == "Blackberry":
                checkoutPage.getProductFooter()[i].click()

        checkoutPage.button().click()
        confirmPage = checkoutPage.sucessButton()
        confirmPage.countryField().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getCountry().click()
        confirmPage.getCheckBox().click()
        confirmPage.submit().click()
        sucessText = confirmPage.alertSucess().text
        assert "Success! Thank you!" in sucessText




