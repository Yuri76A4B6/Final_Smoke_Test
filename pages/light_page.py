import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Light_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    LED_LAMPS = "// a[ @ href = '/catalog/cvetodiodnye-lampy/']" #Светодиодные лампы
    NAKAL_LAMP = "//a[@href='/catalog/lampy-nakalivaniya/']" #Лампы накаливания
    NEON_AND_COMPONENTS = "//a[@href='/catalog/neon/']" #Неоновые ленты и комплектующие

    # GETTERS

    def get_led_lamp(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LED_LAMPS)))

    def get_lamp_nakal(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.NAKAL_LAMP)))

    def get_neon(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.NEON_AND_COMPONENTS)))

    # ACTIONS

    def click_led_lamp(self):
        self.get_led_lamp().click()
        print("Выполнен переход во вкладку 'Светодиодные лампы'")

    def click_lamp_nakal(self):
        self.get_lamp_nakal().click()
        print("Выполнен переход во вкладку 'Лампы накаливания'")

    def click_neon(self):
        self.get_neon().click()
        print("Выполнен переход во вкладку 'Неоновые лампы и компоненты'")

    # METHODS

    def light_page_choose_type_of_lamps(self):
        with allure.step("light_page_choose_type_of_lamps"):
            Logger.add_start_step(method="light_page_choose_type_of_lamps")
            self.get_current_url()
            self.click_led_lamp()
            Logger.add_end_step(url=self.driver.current_url, method="light_page_choose_type_of_lamps")


