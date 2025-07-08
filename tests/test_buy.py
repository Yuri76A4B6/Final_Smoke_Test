from selenium import webdriver
import allure
import pytest
from base.base_class import Base
from pages.authorization_page import Authorization_page
from pages.cart_page import Cart_page
from pages.led_lamps_page import Led_lamps_page
from pages.light_page import Light_page
from pages.main_page import Main_Page
from pages.make_order_page_ import Make_order_page


@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)


    bc = Base(driver)
    mp = Main_Page(driver)
    mp.find_light_page()

    lp = Light_page(driver)
    lp.light_page_choose_type_of_lamps()

    llp = Led_lamps_page(driver)
    llp.choose_lamp_for_buy()
    llp.buy_found_product()
    # llp.choose_flux_filters()
    # llp.choose_type_base_and_glow_temp()
    cp = Cart_page(driver)
    cp.make_order_in_cart()

    ap = Authorization_page(driver)
    ap.make_fast_registration()

    mop = Make_order_page(driver)
    mop.make_order_last_step()


