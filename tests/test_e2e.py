#importuje potřebné moduly a třídy pro ovládání webového prohlížeče
from datetime import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass): #třída dědí metody a atributy definované v BaseClass

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver) #inicializuje objekt Homepage a pomocí něj navigje na stránku nákupu
        checkoutPage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutPage.getCardTitles() #získá seznam karet a iteruje přes ně
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click() #klikne na tlačítko s odkazem

        confirmpage = checkoutPage.checkOutItems() #volá metodu checkOutItems na stránce pokladny
        log.info("Entering country name as ind")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='country']")) #čeká dokud není na stránce přítomen xpath
        )
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind") #do pole pro zemi zadá "ind"
        # time.sleep(5)
        self.verifyLinkPresence("India") #volá metodu pro ověření přítomnosti odkazu na stránce s textem "India"

        self.driver.find_element(By.LINK_TEXT, "India").click()
        element = self.driver.find_element(By.XPATH, "//input[@id='checkbox2']") #klikne na checkbox
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click() #klikně na tlačítko
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is" +textMatch)
        assert '×\nSuccess! Thank you! Your order will be delivered in next few weeks :-).' in textMatch

