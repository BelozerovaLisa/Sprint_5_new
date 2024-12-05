from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants, Messages
from locators import Locators


class Test_LK:
    # переход к разделу Булки
    def test_bulka(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SOUS_BUTTON)).click()
        driver.find_element(*Locators.BULKA_BUTTON).click()
        text_page_bulki = driver.find_element(*Locators.H2_BULKI).text
        assert text_page_bulki == Messages.H2_MAIN_TEXT_BULKI

    # переход к разделу Соусы
    def test_sous(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SOUS_BUTTON)).click()
        text_page_sous = driver.find_element(*Locators.H2_SOUS).text
        assert text_page_sous == Messages.H2_MAIN_TEXT_SOUS
    # переход к разделу Начинки
    def test_filling(self, driver):
        driver.find_element(*Locators.EMAIL_ON_LOG).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLING_BUTTON)).click()
        text_page_sous = driver.find_element(*Locators.H2_FILLING).text
        assert text_page_sous == Messages.H2_MAIN_TEXT_FILLING