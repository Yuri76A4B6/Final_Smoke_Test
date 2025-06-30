import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Led_lamps_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS FILTERS
    AVAILABLE = "(//ins[text()='Только в наличии'])[1]"
    FIND_BRAND_INPUT = "(//div/input[@type='text' and @name='qry' and @class='srch_qry'])[1]" # Я пытался))
    GAUSS_FILTER = "//a[@href='/catalog/cvetodiodnye-lampy/gauss/']"
    CHOOSE_FORM = "//ins/a[@href='/catalog/cvetodiodnye-lampy/v-forme-grushi/']"

    #ВЫБОР БРЕНДА ДЛЯ ПОИСКА
    choosed_brand = "Gauss"
    # GETTERS

    def get_available_lamp(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.AVAILABLE)))

    def get_input_brand(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FIND_BRAND_INPUT)))

    def get_Gauss(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.GAUSS_FILTER)))

    def get_form_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CHOOSE_FORM)))

    # ACTIONS

    def click_available_lamp(self):
        self.get_available_lamp().click()
        print("Выполнен клик по фильтру 'Только в наличии'")

    # def click_brand(self):
    #     self.get_input_brand().click()
    #     print("Выполнен клик для выбора бренда")

    def send_brand(self, sending_text=choosed_brand):
        self.get_input_brand().send_keys(sending_text)

    def click_Gauss(self):
        self.get_Gauss().click()
        print("Выполнен клик на фильтр Gauss")

    def click_form_of_lamp(self):
        self.get_form_filter().click()
        print("Выполнен клик на фильтр 'ГРУША'")



    # METHODS

    def choose_lamp_for_buy(self):
        with allure.step("choose_lamp_for_buy"):
            Logger.add_start_step(method="choose_lamp_for_buy")
            self.get_current_url()
            self.click_available_lamp()
            self.scroll_down(0, 900)
            self.send_brand()
            self.click_Gauss()
            self.click_form_of_lamp()
            Logger.add_end_step(url=self.driver.current_url, method="choose_lamp_for_buy")