from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from constants import Constants, Messages
from locators import Locators


class Test_LK:
    # Проверь переход по клику на «Личный кабинет».
    def test_lk_transfer(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        button_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).text
        assert button_text == Messages.PROFILE_BUTTON_TEXT
    # переход по клику на «Конструктор»
    def test_constructor_transfer(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        h1_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.H1_TEXT_ON_MAIN_PAGE)).text
        assert h1_text == Messages.H1_MAIN_TEXT
    # переход по клику на логотип Stellar Burgers
    def test_constructor_transfer_on_logo(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.BURGER_BUTTON).click()
        h1_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.H1_TEXT_ON_MAIN_PAGE)).text
        assert h1_text == Messages.H1_MAIN_TEXT
    # выход по кнопке «Выйти» в личном кабинете
    def test_exit_from_lk(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON)).click()
        reg_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AFTER_REG)).text
        assert reg_text == Messages.REG_MESS






