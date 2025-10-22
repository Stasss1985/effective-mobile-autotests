from playwright.sync_api import Page
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Инициализация локаторов
        self.about_link = page.get_by_role("link", name="[ О нас ]")
        self.services_link = page.get_by_role("link", name="[ Услуги ]")
        self.projects_link = page.get_by_role("link", name="[ Проекты ]")
        self.reviews_link = page.get_by_role("link", name="[ Отзывы ]")
        self.contacts_link = page.get_by_role("link", name="[ Контакты ]")
        self.specialists_link = page.get_by_role("link", name="Выбрать специалиста")
        self.logo_link = page.locator("#rec573054532").get_by_role("link", name="Effective Mobile")

    def navigate_to_home(self):
        self.navigate("https://effective-mobile.ru")
        self.page.wait_for_load_state("networkidle")

    def open_about_section(self):
        self.about_link.click()
        self.page.wait_for_url("**/#about")

    def open_services_section(self):
        self.services_link.click()
        self.page.wait_for_url("**/#moreinfo")

    def open_projects_section(self):
        self.projects_link.click()
        self.page.wait_for_url("**/#cases")

    def open_reviews_section(self):
        self.reviews_link.click()
        self.page.wait_for_url("**/#Reviews")

    def open_contacts_section(self):
        self.contacts_link.click()
        self.page.wait_for_url("**/#contacts")

    def open_specialists_section(self):
        self.specialists_link.click()
        self.page.wait_for_url("**/#specialists")

    def return_to_main_via_logo(self):
        self.logo_link.click()
        self.page.wait_for_url("**/#main")
