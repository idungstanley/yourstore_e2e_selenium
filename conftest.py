from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    home = "http://tutorialsninja.com/demo"
    service_obj = Service("/Users/USER/Documents/chromedriver/chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("head")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.get(home)
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()


