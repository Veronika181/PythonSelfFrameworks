
#testování webového formuláře pomocí stránky HomePage

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
        #Metoda pro testování odeslání formuláře
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        # Vyplnění jména, příjmení, zaškrtnutí checkboxu a výběr pohlaví.
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])


        homepage.submitForm().click()


        alertText = homepage.getSuccessMessage().text
        # Ověření, zda text obsahuje "Success" a obnovení stránky.
        assert ("Success" in alertText)
        self.driver.refresh()

    # Fixture pro získání testovacích dat pomocí metody z HomePageData.
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param