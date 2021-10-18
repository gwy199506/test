# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import ui
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
ui.WebDriverWait(browser, 10).until(lambda driver: browser.find_element('class name', "bg.s_btn"))
time.sleep(1)
browser.find_element("class name", "s_ipt").send_keys("新闻")
time.sleep(1)
# browser.find_element('css selector', "#su").click()
browser.find_element('class name', "bg.s_btn").click()
