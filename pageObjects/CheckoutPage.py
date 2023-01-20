from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div[@class='card h-100']")
    productFooter = (By.XPATH, "div/button")
    buttonOne = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    buttonSucess = (By.XPATH, "//button[@class='btn btn-success']")


    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.productTitle)

    def getProductFooter(self):
        return self.driver.find_elements(*CheckoutPage.productFooter)

    def button(self):
        return self.driver.find_element(*CheckoutPage.buttonOne)

    def sucessButton(self):
        self.driver.find_element(*CheckoutPage.buttonSucess).click()
        btn = ConfirmPage(self.driver)
        return btn
       # return self.driver.find_element(*CheckoutPage.buttonSucess)

