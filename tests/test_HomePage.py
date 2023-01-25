import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["name"])
        log.info("the first name is "+getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.checkB().click()
        gend = homePage.getGender()
        self.selectOptionByText(gend, getData["gender"])

        homePage.subForm().click()

        alert_text = homePage.alertSuc().text

        assert "successfully" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Test_case_01"))
    def getData(self, request):
        return request.param




