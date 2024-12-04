from selenium.webdriver.common.by import By


class Locators:
    # кнопка Зарегистрироваться
    REG_BUTTON = (By.XPATH, "//a[@href = '/register']")
    # поле ввода имени
    NAME = (By.XPATH,"//fieldset[1]/div/div/input")
    # поле ввода логина
    EMAIL_ON_REG = (By.XPATH, "//fieldset[2]/div/div/input")
    # поле ввода логина на странице авторизации
    EMAIL_ON_LOG = (By.XPATH, "//div/input[@type = 'text']")
    # поле вода пароля
    PASSWORD = (By.XPATH, "//div/input[@type = 'password']")
    # кнопка вход
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # текст над формой авторизации
    AFTER_REG = (By.XPATH, "//div/h2[contains(text(),'Вход')]")
    # текст ошибки Некорректный пароль
    BAD_PASS = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    # кнопка "Войти в аккаунт"
    MAIN_PAGE_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # кнопка оформить заказ
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # кнопка перехода в личный кабинет
    LK_BUTTON = (By.XPATH, "//a[@href = '/account']")
    ENTER_BUTTON = (By.XPATH, "//a[@href = '/login']")
    PASS_RECOVERY_BUTTON = (By.XPATH, "//a[@href = '/forgot-password']")
    # кнопка Профиль в личном кабинете
    PROFILE_BUTTON = (By.XPATH, "//a[@href = '/account/profile']")
    # кнопка Конструктор в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//nav[@class = 'AppHeader_header__nav__g5hnF']/ul[1]/li[1]")
    # кнопка Лента заказов в личном кабинете
    BURGER_BUTTON = (By.XPATH, "//div/a[@href = '/']")
    # текст на странице контруктора Соберите бургер
    H1_TEXT_ON_MAIN_PAGE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    # выход из личного кабинета
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка перехода к булкам
    BULKA_BUTTON = (By.XPATH, "//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    # Кнопка перехода к соусам
    SOUS_BUTTON = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    # Кнопка перехода к начинкам
    FILLING_BUTTON = (By.XPATH,"//span[contains(text(), 'Начинки')]/parent::div")
    # текст у вкладки булки
    H2_BULKI = (By.XPATH, "//h2[contains(text(),'Булки')]")
    # текст у вкладки соусы
    H2_SOUS = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    # текст у вкладки начинки
    H2_FILLING = (By.XPATH, "//h2[contains(text(),'Начинки')]")


