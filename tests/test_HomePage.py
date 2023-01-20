
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("eude")
        homePage.getEmail().send_keys("eude@eude.com")
        homePage.checkB().click()
        gend = homePage.getGender()

        sel = Select(gend)
        sel.select_by_visible_text("Male")
        homePage.subForm().click()

        alert_text = homePage.alertSuc().text

        assert "successfully" in alert_text



