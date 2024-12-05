from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants, Messages
from locators import Locators


class Test_Log_In:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_button_main_page(self, driver_main):
        driver_main.find_element(*Locators.MAIN_PAGE_BUTTON).click()
        driver_main.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver_main.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver_main.find_element(*Locators.AUTH_BUTTON).click()
        button_text = WebDriverWait(driver_main, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert button_text == Messages.ORDER_BUTTON_TEXT

    # вход через кнопку «Личный кабинет»
    def test_button_LK(self, driver_main):
        driver_main.find_element(*Locators.LK_BUTTON).click()
        driver_main.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver_main.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver_main.find_element(*Locators.AUTH_BUTTON).click()
        button_text = WebDriverWait(driver_main, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert button_text == Messages.ORDER_BUTTON_TEXT

    # вход через кнопку в форме регистрации
    def test_button_reg_form(self, driver):
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        button_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert button_text == Messages.ORDER_BUTTON_TEXT

    # вход через кнопку в форме восстановления пароля
    def test_button_pass_recovery(self, driver):
        driver.find_element(*Locators.PASS_RECOVERY_BUTTON).click()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        button_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert button_text == Messages.ORDER_BUTTON_TEXT