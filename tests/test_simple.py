import allure
import pytest
from playwright.sync_api import Page, expect


def test_run(page: Page) -> None:
    # Навигация и авторизация
    page.goto("https://effective-mobile.ru/#specialists")
