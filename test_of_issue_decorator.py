import allure
from selene import by, be
from selene import browser

def test_decorator_steps():
    open_browser()
    find_repo('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    find_issues_button()
    find_element()


@allure.step('Открываем браузер')
def open_browser():
    browser.open_url("https://github.com")

@allure.step('Ищем репозиторий {repo}')
def find_repo(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()

@allure.step('Переходим по ссылке репозитория')
def go_to_repo(repo):
    browser.element('.text-normal .v-align-middle').click()


@allure.step('Выбираем раздел "issues" в репозитории')
def find_issues_button():
    browser.element("#issues-tab").click()

@allure.step('Ищем элемент по номеру')
def find_element():
    browser.element(by.partial_text("#76")).should(be.visible)