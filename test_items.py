from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_languages(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket'"), 'There is no button to add the product into the basket'
    
    