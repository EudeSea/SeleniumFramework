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
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItem()
        log.info("getting all the products titles")
        #checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getProductTitles()

       # confirmPage = ConfirmPage(self.driver)
        i = -1

        for product in products:
            i = i + 1
            productName = product.text
           # log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getProductFooter()[i].click()

        checkoutPage.button().click()
        confirmPage = checkoutPage.sucessButton()
        log.info("enterring country name as India")
        confirmPage.countryField().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getCountry().click()
        confirmPage.getCheckBox().click()
        confirmPage.submit().click()
        sucessText = confirmPage.alertSucess().text
        log.info("test received  from application is "+sucessText)
        assert "Success! Thank you!" in sucessText




