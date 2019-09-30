# В файл test_items.py напишите тест, который проверяет,
# что страница товара на сайте содержит кнопку добавления в корзину.
# Например, можно проверять товар, доступный по
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

import pytest
from selenium import webdriver
import time


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_btn_exists(browser):
    browser.get(LINK)
    browser.implicitly_wait(10)
    time.sleep(30)
    selector = '.add-to-basket button[class$="btn-add-to-basket"]'
    add_to_basket = browser.find_element_by_css_selector(selector)
    assert add_to_basket.is_displayed(),\
        'Button "Add to basket" is not found'