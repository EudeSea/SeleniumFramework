from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryID  = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitBtn = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def countryField(self):
        return self.driver.find_element(*ConfirmPage.countryID)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitBtn)

    def alertSucess(self):
        return self.driver.find_element(*ConfirmPage.alert)