from selenium.webdriver.common.by import By
from Chose_countryPage import ChoseCountry


class Cart:

    promo_input = (By.CSS_SELECTOR, "input[class='promoCode']")
    promo_btn = (By.CSS_SELECTOR, "button[class='promoBtn']")
    purchase_summary = (By.CSS_SELECTOR, "table[id='productCartTables'] tbody tr td:nth-child(5)")
    total_amount = (By.CSS_SELECTOR, "span[class='totAmt']")
    discount_perc = (By.CSS_SELECTOR, "span[class='discountPerc'")
    place_order = (By.CSS_SELECTOR, "div[class='products'] button:last-child")
    after_disc = (By.CSS_SELECTOR, "span[class='discountAmt']")
    
    def __init__(self, driver):
        self.driver = driver

    def enter_promo(self):
        return self.driver.find_element(*Cart.promo_input)

    def apply(self):
        return self.driver.find_element(*Cart.promo_btn)

    def sum_assert(self):
        total = self.driver.find_elements(*Cart.purchase_summary)
        cost = 0
        for price in total:
            cost += int(price.text)
        return cost

    def price(self):
        total_price = int(self.driver.find_element(*Cart.total_amount).text)
        return total_price

    def discount(self):
        return self.driver.find_element(*Cart.discount_perc).text

    def order(self):
        self.driver.find_element(*Cart.place_order).click()
        chose_country = ChoseCountry(self.driver)
        return chose_country

    def price_disc(self):
        return self.driver.find_element(*Cart.after_disc)
