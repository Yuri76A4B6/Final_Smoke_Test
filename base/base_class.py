import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод для получения URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Метод assert word"""

    def assert_word(self, word, expected_result):
        value_word = word.text
        assert value_word == expected_result
        print("Good value")

    """Метод screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Python projects\\PythonProject\\automation_practice\\screen' + name_screenshot)

    """Метод assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")