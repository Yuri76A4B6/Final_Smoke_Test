import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_Page(Base):

    url = "https://www.minimaks.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    ABOUT_COMPANY = "(//a[@href='/about_company/'])[1]"
    ABOUT_VACANCY = "(//a[@href='/about/vacancy/'])[1]"
    LEGAL_ENTITY = "(//a[@href='/market/'])[1]" #Юр.Лицам
    CART = "//div[@id='bakset-small-can-buy']"
    SEARCH_SOMETHING = "//input[@id='title-search-input-diginetica']" #локатор для поля поиска товаров на сайте
    LIGHT = "(//a[@href='/catalog/svetotekhnika/'])[2]" #локатор для перехода во вкладку "светотехника"


    # Getters

    def get_about_company(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ABOUT_COMPANY)))

    def get_about_vacancy(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ABOUT_VACANCY)))

    def get_legal_entity(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LEGAL_ENTITY)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CART)))

    def get_search_line(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_SOMETHING)))

    def get_light(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LIGHT)))

    #ACTIONS

    def click_light(self):
        self.get_light().click()
        print("Выполнен переход во вкладку 'Светотехника'")

    def click_about_company(self):
        self.get_about_company().click()
        print("Выполнен клик для перехода на страницу 'О компании'")

    def click_about_vacancy(self):
        self.get_about_vacancy().click()
        print("Выполнен клик для перехода на страницу 'Вакансии'")

    def click_legal_entity(self):
        self.get_legal_entity().click()
        print("Выполнен клик для перехода на вкладку информации Юр.лицам")

    def click_cart(self):
        self.get_cart().click()
        print("Выполнен клик для перехода в корзину")

    def click_search_line(self):
        self.get_cart().click()
        print("Выполнен клик в строку поиска")

        # METHODS

    def find_light_page(self):
        with allure.step("find_light_page"):
            Logger.add_start_step(method="find_light_page")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_light()
            Logger.add_end_step(url=self.driver.current_url, method="find_light_page")
