from selene import by, be
from selene import browser
import allure



def test_github():
    with allure.step('Открываем браузер'):
        browser.open_url("https://github.com")
    with allure.step('Кликаем на поиск'):
        browser.element(".header-search-input").click()
    with allure.step('Вводим адрес в поиск'):
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    with allure.step('Кликаем "подтвердить"'):
        browser.element(".header-search-input").submit()
    with allure.step('Кликаем на нужный нам репозиторий'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Кликаем на issues'):
        browser.element("#issues-tab").click()
    with allure.step('Ищем наличие элемента по цифрам в названии'):
        browser.element(by.partial_text("#76")).should(be.visible)