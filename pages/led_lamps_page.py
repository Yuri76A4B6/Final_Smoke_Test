import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
from utilities.logger import Logger
import time


class Led_lamps_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS FILTERS
    AVAILABLE = "(//ins[text()='Только в наличии'])[1]"
    FIND_BRAND_INPUT = "(//div/input[@type='text' and @name='qry' and @class='srch_qry'])[1]" # Я пытался))
    GAUSS_FILTER = "//label[@data-role='label_arrFilter_228_810500906']"
    CHOOSE_FORM = "//ins/a[@href='/catalog/cvetodiodnye-lampy/v-forme-grushi/']"
    CANDLE_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/v-forme-svechi/']"
    BUTTON_MORE_FORM = "//*[@id='filterListBlock-221']/div[2]/ul/li[19]"
    TABLET_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/tabletka/']"
    POWER_10W_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/10-vt/']"
    POWER_12W_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/12-vt/']"
    MATOVAYA_KOLBA = "//ins/a[@href='/catalog/cvetodiodnye-lampy/matovye/']"
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

    def get_candle_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CANDLE_CHECKBOX)))

    def get_button_more_form(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_MORE_FORM)))

    def get_tablet_form(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TABLET_CHECKBOX)))

    def get_10W_power(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.POWER_10W_CHECKBOX)))

    def get_12W_power(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.POWER_12W_CHECKBOX)))

    def get_matte_kolba(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.MATOVAYA_KOLBA)))

    # ACTIONS


    def click_available_lamp(self):
        self.get_available_lamp().click()
        print("Выполнен клик по фильтру 'Только в наличии'")

    def click_brand(self):
        self.get_input_brand().click()
        print("Выполнен клик для выбора бренда")

    def send_brand(self, sending_text=choosed_brand):
        self.get_input_brand().clear()
        self.get_input_brand().send_keys(sending_text)

    def click_Gauss(self):
        self.get_Gauss().click()
        print("Выполнен клик на фильтр Gauss")

    def click_pear_form(self):
        self.get_form_filter().click()
        print("Выполнен клик на фильтр 'ГРУША'")

    def click_candle_form(self):
        self.get_candle_checkbox().click()
        print("Выполнен клик на фильтр 'СВЕЧА'")

    def click_more_checkbox_form(self):
        self.get_button_more_form().click()
        print("Выполнен клик на кнопку 'ЕЩЕ' для выбора дополнительных фильтров форм ламп")

    def click_tablet_checkbox_form(self):
        self.get_tablet_form().click()
        print("Выполнен клик на фильтр 'ТАБЛЕТКА'")

    def click_10W_checkbox(self):
        self.get_10W_power().click()
        print("Выполнен клик на фильтр мощности '10 Вт'")

    def click_12W_checkbox(self):
        self.get_12W_power().click()
        print("Выполнен клик на фильтр мощности '12 Вт'")

    def click_matte_checkbox(self):
        self.get_matte_kolba().click()
        print("Выполнен клик на фильтр 'Покрытие колбы'")

    # METHODS

    def choose_lamp_for_buy(self):
        with allure.step("choose_lamp_for_buy"):
            Logger.add_start_step(method="choose_lamp_for_buy")
            action = ActionChains(self.driver)
            self.get_current_url()
            self.click_available_lamp()
            self.click_brand()
            self.send_brand()
            try:
                self.click_Gauss()
            except ElementClickInterceptedException as e:
                print(f"Ошибка {e}")
                action.scroll_by_amount(0, 500).perform()
                self.click_Gauss()
            # _move_to_form = self.driver.find_element(By.XPATH, "//div[@data-filter='221'] ")
            # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", _move_to_form)
            time.sleep(3)
            action.scroll_by_amount(0, 600).perform()
            self.click_pear_form()
            self.click_candle_form()
            self.click_more_checkbox_form()
            time.sleep(3)
            self.click_tablet_checkbox_form()
            try:
                self.click_10W_checkbox()
                self.click_12W_checkbox()
            except ElementClickInterceptedException as d:
                print(f"Ошибка {d}")
                _move_to_12W = self.get_12W_power()
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", _move_to_12W)
                self.click_10W_checkbox()
                self.click_12W_checkbox()
            self.click_matte_checkbox()
            Logger.add_end_step(url=self.driver.current_url, method="choose_lamp_for_buy")