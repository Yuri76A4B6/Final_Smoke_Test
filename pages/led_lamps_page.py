import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
from utilities.logger import Logger
import time


class Led_lamps_page(Base):


    # LOCATORS FILTERS
    AVAILABLE = "(//ins[text()='Только в наличии'])[1]"
    FIND_BRAND_INPUT = "(//div/input[@type='text' and @name='qry' and @class='srch_qry'])[1]" # Я пытался))
    GAUSS_FILTER = "//label[@data-role='label_arrFilter_228_810500906']"
    CHOOSE_FORM = "//ins/a[@href='/catalog/cvetodiodnye-lampy/v-forme-grushi/']"
    CANDLE_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/v-forme-svechi/']"
    BUTTON_MORE_FORM = "(//li[@class='show-more-but'])[2]"
    TABLET_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/tabletka/']"
    POWER_10W_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/10-vt/']"
    POWER_12W_CHECKBOX = "//ins/a[@href='/catalog/cvetodiodnye-lampy/12-vt/']"
    MATOVAYA_KOLBA = "//ins/a[@href='/catalog/cvetodiodnye-lampy/matovye/']"
    SERIES_ELEMENTARY = "//a[@href='/catalog/cvetodiodnye-lampy/elementary/']"
    SERIES_GAUSS = "//a[@href='/catalog/cvetodiodnye-lampy/gauss-elementary/']"
    SERIES_GLOBE_A60 = "//a[@href='/catalog/cvetodiodnye-lampy/globe-a60/']"
    FLUX_730 = "//a[@href='/catalog/cvetodiodnye-lampy/730-lm/']"
    FLUX_950 = "//a[@href='/catalog/cvetodiodnye-lampy/950-lm/']"
    FLUX_1130 = "//a[@href='/catalog/cvetodiodnye-lampy/1130-lm/']"
    TYPE_E14 = "//a[@href='/catalog/cvetodiodnye-lampy/s-tsokolem-e14/']"
    TYPE_E27 = "//ins/a[@href='/catalog/cvetodiodnye-lampy/s-tsokolem-e27/']"
    GLOW_4100K = "//ins/a[@href='/catalog/cvetodiodnye-lampy/4100-k/']"
    GLOW_6500K = "//ins/a[@href='/catalog/cvetodiodnye-lampy/6500-k/']"
    BUTTON_FINISH_SET_FILTER = "//button[@id='set_filter']"
    SHOW_BUTTON = ("//a[@href='/catalog/cvetodiodnye-lampy/v-forme-grushi/v-forme-svechi/gauss/10-vt/12-vt/matovye"
                   "/elementary/gauss-elementary/globe-a60/?available=y']")
    BUY_PRODUCT_BUTTON = "//div/a[@data-id='5653491' and @data-offers-add='5653726']"
    NAME_PRODUCT = "(//a[@href='/product/lampa-svetodiodnaya-10-vt-e14-c37-4100k-730lm-led-svecha-elementary-33120-gauss/'])[1]"
    CART_LOCATION = "(//a[@href='/personal/cart/'])[1]"

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

    def get_series_elementary(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.SERIES_ELEMENTARY)))

    def get_series_gauss(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.SERIES_GAUSS)))

    def get_series_globe_a60(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.SERIES_GLOBE_A60)))

    def get_flux_730(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FLUX_730)))

    def get_flux_950(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FLUX_950)))

    def get_flux_1130(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FLUX_1130)))

    def get_type_e14(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TYPE_E14)))

    def get_type_e27(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TYPE_E27)))

    def get_glow_4100k(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.GLOW_4100K)))

    def get_glow_6500k(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.GLOW_6500K)))

    def get_finish_set_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_FINISH_SET_FILTER)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable((By.XPATH, self.SHOW_BUTTON)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.BUY_PRODUCT_BUTTON)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CART_LOCATION)))

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

    def click_series_elementary(self):
        self.get_series_elementary().click()
        print("Выполнен клик на фильтр 'Серия/ELEMENTARY'")

    def click_series_gauss(self):
        self.get_series_gauss().click()
        print("Выполнен клик на фильтр 'Серия/GAUSS'")

    def click_series_globe_a60(self):
        self.get_series_globe_a60().click()
        print("Выполнен клик на фильтр 'Серия/GLOBE A60'")

    def click_flux_730(self):
        self.get_flux_730().click()
        print("Выполнен клик на фильтр 'Световой поток,Лм, 730'")

    def click_flux_950(self):
        self.get_flux_950().click()
        print("Выполнен клик на фильтр 'Световой поток,Лм, 950'")

    def click_flux_1130(self):
        self.get_flux_1130().click()
        print("Выполнен клик на фильтр 'Световой поток,Лм, 1130'")

    def click_type_E14(self):
        self.get_type_e14().click()
        print("Выполнен клик на фильтр 'Тип цоколя/E14'")

    def click_type_E27(self):
        self.get_type_e27().click()
        print("Выполнен клик на фильтр 'Тип цоколя/E27'")

    def click_glow_4100k(self):
        self.get_glow_4100k().click()
        print("Выполнен клик на фильтр 'Цветовая температура 4100 кельвинов'")

    def click_glow_6500k(self):
        self.get_glow_6500k().click()
        print("Выполнен клик на фильтр 'Цветовая температура 6500 кельвинов'")

    def click_finish_set_button(self):
        self.get_finish_set_filter().click()
        print("Выполнен клик на фильтр подбора ламп")

    def click_show_button(self):
        self.get_show_button().click()
        print("Выполнен клик на кнопку показать")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Выполнен клик на кнопку купить")

    def click_cart(self):
        try:
            self.get_cart().click()
        except ElementNotInteractableException as v:
            print(f"Элемент не кликается. Ошибка {v}")
            self.get_cart().click()
        print("Выполнен клик на кнопку корзина")
    # METHODS

    def choose_lamp_for_buy(self):
        with allure.step("Choose lamp for buy"):
            Logger.add_start_step(method="choose_lamp_for_buy")
            action = ActionChains(self.driver)
            self.get_current_url()
            self.click_available_lamp()
            time.sleep(2)
            self.click_brand()
            self.send_brand()
            try:
                self.click_Gauss()
            except ElementClickInterceptedException as e:
                print(f"Ошибка {e}")
                action.scroll_by_amount(0, 500).perform()
                self.click_Gauss()
            action.scroll_by_amount(0, 600).perform()
            self.click_pear_form()
            self.click_candle_form()
            self.click_more_checkbox_form()
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
            action.scroll_by_amount(0, 700).perform()
            self.click_series_elementary()
            self.click_series_gauss()
            self.click_series_globe_a60()
            self.click_show_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_lamp_for_buy")

    def choose_lamp_for_buy_if_not_available(self):
        with allure.step("Choose lamp for buy"):
            Logger.add_start_step(method="choose_lamp_for_buy")
            action = ActionChains(self.driver)
            self.get_current_url()
            self.click_brand()
            self.send_brand()
            try:
                self.click_Gauss()
            except ElementClickInterceptedException as e:
                print(f"Ошибка {e}")
                action.scroll_by_amount(0, 500).perform()
                self.click_Gauss()
            action.scroll_by_amount(0, 600).perform()
            self.click_pear_form()
            self.click_candle_form()
            self.click_more_checkbox_form()
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
            action.scroll_by_amount(0, 700).perform()
            self.click_series_elementary()
            self.click_series_gauss()
            self.click_series_globe_a60()
            _move_to_finish_button = self.get_finish_set_filter()
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", _move_to_finish_button)
            time.sleep(2)  # Без таймслипа не успевает навестись на кнопку, не кликает и тест падает...
            self.click_finish_set_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_lamp_for_buy")

    def buy_found_product(self):
        with allure.step("Buy found_product"):
            Logger.add_start_step(method="buy_found_product")
            try:
                action = ActionChains(self.driver)
                action.scroll_by_amount(0, 450).perform()
                self.click_buy_button()
            except ElementClickInterceptedException as bp:
                print(f"Ошибка {bp}")
                # action = ActionChains(self.driver)
                # action.scroll_by_amount(0,333)
                # move_to_buy = self.get_buy_button()
                # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", move_to_buy)
                self.click_buy_button()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="buy_found_product")

# ВНИМАНИЕ!!! ДАННЫЙ БЛОК КОДА ПРИШЛОСЬ ИСКЛЮЧИТЬ ПОТОМУ, ЧТО САЙТ НЕСТАБИЛЬНО РАБОТАЕТ!!! ПРИ ВЫБОРЕ ПОЧТИ ВСЕХ
# ИМЕЮЩИХСЯ ФИЛЬТРОВ САЙТ ПИШЕТ, ЧТО НА НЕМ ВЕДУТСЯ ТЕХНИЧЕСКИЕ РАБОТЫ. ТЕСТ СРАБАТЫВАЕТ ПОЛНОСТЬЮ ЧЕРЕЗ РАЗ!!!

    # def choose_flux_filters(self):
    #     with allure.step("Метод choose flux filters"):
    #         Logger.add_start_step(method="choose_flux_filters")
    #         try:
    #             self.click_flux_730()
    #             self.click_flux_950()
    #             self.click_flux_1130()
    #         except ElementClickInterceptedException as f:
    #             print(f"Ошибка {f} (Локатор вне зоны видимости)")
    #             action = ActionChains(self.driver)
    #             action.scroll_by_amount(0, 600).perform()
    #             self.click_flux_730()
    #             self.click_flux_950()
    #             self.click_flux_1130()
    #         Logger.add_end_step(url=self.driver.current_url, method="choose_flux_filters")
    #
    # def choose_type_base_and_glow_temp(self):
    #     with allure.step("Метод choose type base and glow temp"):
    #         Logger.add_start_step(method="choose_type_base_and_glow_temp")
    #         move_to_type4100 = self.get_type_e14()
    #         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", move_to_type4100)
    #         time.sleep(2)
    #         self.click_type_E14()
    #         self.click_type_E27()
    #         self.click_glow_4100k()
    #         self.click_glow_6500k()
    #         self.click_finish_set_button()
    #         Logger.add_end_step(url=self.driver.current_url, method="choose_type_base_and_glow_temp")

