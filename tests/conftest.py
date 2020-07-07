import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def launchBrowser(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    request.cls.driver = driver
    yield
    driver.close()
