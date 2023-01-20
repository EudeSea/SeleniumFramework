from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    sub = (By.XPATH, "//input[@value='Submit']")
    alertS = (By.CSS_SELECTOR, "[class*='alert-success'")

    shop = (By.CSS_SELECTOR,"a[href*='shop']" )

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkB(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def subForm(self):
        return self.driver.find_element(*HomePage.sub)

    def alertSuc(self):
        return self.driver.find_element(*HomePage.alertS)

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        shop = CheckoutPage(self.driver)
        return shop
        #return self.driver.find_element(*HomePage.shop) # o * é para saber que é uma tupla
