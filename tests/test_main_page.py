import allure
import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage


@allure.suite("Главная страница effective-mobile.ru")
@allure.feature("Проверка навигации")
class TestMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, page):
        self.main_page = MainPage(page)
        self.main_page.navigate_to_home()
        yield

    @allure.title("Проверка заголовка главной страницы")
    def test_home_page_title(self):
        expect(self.main_page.page).to_have_title("Effective Mobile | Разработка мобильных приложений")

    @allure.title("Переход в раздел 'О нас'")
    def test_about_section(self):
        self.main_page.open_about_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#about")
        expect(self.main_page.page.locator("body")).to_contain_text("О нас")

    @allure.title("Переход в раздел 'Услуги'")
    def test_services_section(self):
        self.main_page.open_services_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#moreinfo")
        expect(self.main_page.page.locator("body")).to_contain_text("Услуги")

    @allure.title("Переход в раздел 'Проекты'")
    def test_projects_section(self):
        self.main_page.open_projects_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#cases")
        expect(self.main_page.page.locator("body")).to_contain_text("Проекты")

    @allure.title("Переход в раздел 'Отзывы'")
    def test_reviews_section(self):
        self.main_page.open_reviews_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#Reviews")
        expect(self.main_page.page.locator("body")).to_contain_text("ОТЗЫВЫ КЛИЕНТОВ")

    @allure.title("Переход в раздел 'Контакты'")
    def test_contacts_section(self):
        self.main_page.open_contacts_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#contacts")
        expect(self.main_page.page.locator("body")).to_contain_text("ОТЗЫВЫ КЛИЕНТОВ")

    @allure.title("Переход в раздел 'Выбрать специалиста'")
    def test_specialists_section(self):
        self.main_page.open_specialists_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#specialists")
        expect(self.main_page.page.locator("body")).to_contain_text("Наш стек")

    @allure.title("Проверка возврата на главную через логотип")
    def test_return_to_home_via_logo(self):
        self.main_page.open_about_section()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#about")
        self.main_page.return_to_main_via_logo()
        expect(self.main_page.page).to_have_url("https://effective-mobile.ru/#main")
        expect(self.main_page.page.locator("body")).to_contain_text("Разработка")
