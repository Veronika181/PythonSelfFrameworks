from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver): #Konstruktor třídy, který příjámá odkaz na objekt webového ovladače a ukládá ho jako atribut self.driver
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value= 'Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")  #lokátory elementů jsou definovány jako třídy By (např. By.CSS_SELECTOR, By.NAME)
                                                                    #každý lokátor je reprezentován dvojicí (typ lokárotu, hodnota lokátoru)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()            #klikne na odkaz na nákupní stránce(lokátor shop)
        checkOutPage = CheckOutPage(self.driver)                    #vytvoří objekt třídy CheckOutPage a předá mu odkaz na webový prohlížeč
        return checkOutPage                                         #vrací instanci třídy ChechOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    #Tyto metody slouží k získání odkazů na různé elementy na stránce pomocí lokátorů definovaných v třídě
    #Každá metoda vrací objekt webového elementu, který může být použit pro další interakce nebo oveření
    #Celkově tato třída poskytuje metody pro interakci s různými prvky na domovské stránce, což umožnuje snadnou automatizaci testů webových stránek


    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

