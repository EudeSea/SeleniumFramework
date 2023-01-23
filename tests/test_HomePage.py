import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        log.info("the first name is "+getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.checkB().click()
        gend = homePage.getGender()
        self.selectOptionByText(gend, getData["gender"])

        homePage.subForm().click()

        alert_text = homePage.alertSuc().text

        assert "successfully" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param




