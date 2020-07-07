
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import HomePage
from Utlity.demoBaseclass import BaseClass


class Testdemo(BaseClass):


    def test_endToend(self):
        actual = "Samsung Note 8"
        expected = ""
        #homepage = HomePage(self.driver)

        self.useHomepage()
       # homepage.shoplink().click()
        assert "ProtoCommerce" ==self. driver.title
        self.driver.find_element_by_xpath("//a[.='Samsung Note 8']/../../..//button").click()
        self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
        cartitem = self.driver.find_elements_by_xpath("//h4[@class='media-heading']//a")
        for items in cartitem:
            expected = items.text
        assert expected == actual
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[.='India']")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        print(self.driver.find_element_by_xpath("//div[contains(@class,'alert ')]//strong").text)
        #self.driver.get_screenshot_as_file()

     #def test_new(self):
         #print("this is new case")

