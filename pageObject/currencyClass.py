from selenium.webdriver.common.by import By


class Currency:
    def __int__(self, driver):
        self.driver = driver

    target_currency = (By.CSS_SELECTOR, 'button[class="btn btn-link dropdown-toggle"]')
    target_eur = (By.CSS_SELECTOR, 'button[name="EUR"]')
    target_gbp = (By.CSS_SELECTOR, 'button[name="GBP"]')
    target_usd = (By.CSS_SELECTOR, 'button[name="USD"]')
    target_checkout_cur = (By.ID, 'cart-total')
    target_price = (By.CSS_SELECTOR, 'p[class ="price"]')

    def click_currency(self):
        return self.driver.find_element(*Currency.target_currency).click()

    def select_euro(self):
        return self.driver.find_element(*Currency.target_eur).click()

    def select_pounds(self):
        return self.driver.find_element(*Currency.target_gbp).click()

    def select_dollars(self):
        return self.driver.find_element(*Currency.target_usd).click()

    def checkout_currency(self):
        return self.driver.find_element(*Currency.target_checkout_cur).text

    def price_currency(self):
        return self.driver.find_elements(*Currency.target_price)
