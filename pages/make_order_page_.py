import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from base.base_class import Base
from utilities.logger import Logger

class Make_order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    ORDER_NAME = "//input[@name='ORDER_PROP_1']"
    ORDER_PHONE_NUMBER = "//input[@name='ORDER_PROP_3']"
    ORDER_EMAIL = "//input[@name='ORDER_PROP_2']"
    ORDER_RECEIPT_METHOD = "//span[contains(text(),'Самовывоз')]"
    ADRESS_POINT = "//div[@class='takeItem' and @data-item='281']"
    BUTTON_ADRESS_POINT = "//button[@class='takeCurrent__button button--primary' and @data-store='281']"
    COMMENT_INPUT_FIELD = "//div/textarea[@name='COMMENT']"
    PRODUCT_PRICE = "(//div/span[contains(text(),'57,50 ₽')])[1]"
    TOTAL_PRICE = "//span[@id='orderResultBlock2']"

    # GETTERS

    def get_product_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.PRODUCT_PRICE)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TOTAL_PRICE)))

    def get_order_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ORDER_NAME)))

    def get_order_phone_number(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ORDER_PHONE_NUMBER)))

    def get_order_email(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ORDER_EMAIL)))

    def get_order_receipt_method(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ORDER_RECEIPT_METHOD)))

    def get_adress_point(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ADRESS_POINT)))

    def get_button_adress_point(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_ADRESS_POINT)))

    def get_comment_input_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.COMMENT_INPUT_FIELD)))

    # ACTIONS
    def input_order_name(self):
        self.get_order_name().send_keys("Test user")
        print("Заполнено поле с именем")

    def input_order_phone_number(self):
        self.get_order_phone_number().send_keys("9996663311")
        print("Заполнено поле с номером телефона")

    def input_order_email(self):
        self.get_order_email().send_keys("test_user@selenium.ru")
        print("Заполнено поле с адресом электронной почты")

    def click_order_receipt_method(self):
        self.get_order_receipt_method().click()
        print("Выбран метод получения заказа")

    def click_adress_point(self):
        self.get_adress_point().click()
        print("Выбрано место получения заказа")

    def click_button_adress_point(self):
        self.get_button_adress_point().click()
        print("Выполнен клик для подтверждения выбора пункта выдачи")

    def input_comment_field(self, text):
        self.get_comment_input_field().send_keys(text)
        print("Выполнено заполнение поля 'комментарий к заказу'")

    #METHODS

    def make_order_last_step(self):
        with allure.step("Make order last step"):
            Logger.add_start_step(method="make_order_last_step")
            self.get_current_url()
            self.assert_price(self.get_product_price(), self.get_total_price())
            self.input_order_name()
            self.input_order_phone_number()
            self.input_order_email()
            self.click_order_receipt_method()
            self.click_adress_point()
            self.click_button_adress_point()
            text_message = "Если это поле заполнено, значит тест завершен успешно. Для проверки проверить скриншот в директории screen"
            self.input_comment_field(text_message)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="make_order_last_step")
