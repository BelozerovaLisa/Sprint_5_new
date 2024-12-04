
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from constants import Constants, Messages
from locators import Locators

# from locators import Locators
faker = Faker()
class Test_Auth:
    # Успешная регистрация
    def test_registration(self, driver):
        email = faker.email()
        name = faker.name()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_ON_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        reg_text = WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.AFTER_REG)).text
        assert reg_text == Messages.REG_MESS

    # Ошибка для некорректного пароля
    def test_registration_bad_password(self, driver):
        email = faker.email()
        name = faker.name()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_ON_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD_BAD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        reg_text = WebDriverWait(driver,2).until(EC.visibility_of_element_located(Locators.BAD_PASS)).text
        assert reg_text == Messages.BAD_PASS_MESS