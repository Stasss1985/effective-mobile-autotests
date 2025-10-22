from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def get_current_url(self) -> str:
        return self.page.url

    def click_element(self, selector: str):
        self.page.click(selector)

    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def wait_for_url_change(self, original_url: str):
        self.page.wait_for_function(f'window.location.href !== "{original_url}"')
