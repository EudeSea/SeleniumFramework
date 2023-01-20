import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "firefox", help = "my option: firefox or chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_obj = Service("C:/Users/Eudyy/Videos/geckodriver.exe")
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(options=options, service=service_obj)

    #driver.get("https://gaclickacademy.github.io/protocommerce/")
    elif browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Eudyy/Videos/chromedriver.exe")


    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
