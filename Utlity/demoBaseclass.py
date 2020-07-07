import pytest

from PageObjects.Homepage import HomePage


@pytest.mark.usefixtures("launchBrowser")
class BaseClass:

    def useHomepage(self):
        homepage=HomePage(self.driver)
        #homepage.click()

