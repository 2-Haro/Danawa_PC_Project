from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)

def find_present(css_selector):
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_present(css_selector):
  find_present(css_selector)
  return chrome.find_elements_by_css_selector(css_selector)

def find_visible(css_selector):
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_visible(css_selector):
  find_visible(css_selector)
  return chrome.find_elements_by_css_selector(css_selector)

category = {
  "cpu": "873",
  "mainboard": "875",
  "memory": "873",
  "graphic_card": "873",
  "ssd": "32617",
  "case": "879",
  "power": "880"
}

category_css = {
  c: "dd.category_" + category[c] + " a" for c in category # 딕셔너리 comprehension
}

chrome.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# cpu 카테고리 클릭
find_visible(category_css["cpu"]).click()
time.sleep(1)

# cpu 제조사 불러오기
options = finds_visible("div[class=search_option_wrap] div[class=search_option_item]:first-child span[class=item_text]")
print("CPU 제조사를 선택해주세요.")
for i in range(len(options)):
  print(str(i + 1) + ". " + options[i].text)

chrome.quit()