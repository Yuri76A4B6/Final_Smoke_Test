import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Authorization_page(Base):


    # LOCATORS
    USER_LOGIN = "//input[@name='USER_LOGIN']"
    USER_PASSWORD = "//input[@name='USER_PASSWORD']"
    ENTRY_BUTTON = "//button[@class='enter-form-button']"
    FAST_REGISTRATION = "//a[@class='checkout button not-registered-button']"

    def get_fast_registration(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FAST_REGISTRATION)))

    def click_fast_registration(self):
        self.get_fast_registration().click()
        print("Выполнен клик на быструю регистрацию")

    def make_fast_registration(self):
        with allure.step("Make fast registration"):
            Logger.add_start_step(method="make_fast_registration")
            self.get_current_url()
            self.click_fast_registration()
            Logger.add_end_step(url=self.driver.current_url, method="make_fast_registration")