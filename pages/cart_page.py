import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from base.base_class import Base
from utilities.logger import Logger



class Cart_page(Base):

    # LOCATORS
    NAME_PRODUCT_IN_CART = ("//a[@href='/product/lampa-svetodiodnaya-10-vt-e14-c37-4100k-730lm-led-svecha-elementary-"
                            "33120-gauss/' and @rel='noreferrer']")
    CHOOSE_PRODUCT_CHECKBOX = "//div[@class='check-item']"
    MAKE_ORDER = "//a[@href='/personal/orders/make/']"
    PRICE_PRODUCT = "//div[@class='table-all-price']"

    # GETTERS
    def get_name_product_in_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.NAME_PRODUCT_IN_CART)))

    def get_choose_product(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CHOOSE_PRODUCT_CHECKBOX)))

    def get_make_order(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.MAKE_ORDER)))

    def get_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.PRICE_PRODUCT)))

    # ACTIONS

    def click_choose_product(self):
        self.get_choose_product().click()
        print("Выполнен клик по чекбоксу для выбора товара")

    def click_make_order(self):
        self.get_make_order().click()
        print("Выполнен клик для оформления заказа")

    # METHODS

    def make_order_in_cart(self):
        with allure.step("Make order in cart"):
            Logger.add_start_step(method="make_order_in_cart")
            self.get_current_url()
            Expected_result_for_assert = "Лампа светодиодная 10 Вт E14 C37 4100K 730Лм LED Свеча Elementary 33120 GAUSS"
            self.assert_word(self.get_name_product_in_cart(), Expected_result_for_assert)
            self.click_choose_product()
            self.click_make_order()
            Logger.add_end_step(url=self.driver.current_url, method="make_order_in_cart")
