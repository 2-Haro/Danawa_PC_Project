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

def choose_one(text, options): # 선택 함수
  print(text)
  for i in range(len(options)):
    print(f"{i + 1}. {options[i]}")
  choose = input("-> ")
  return int(choose) - 1

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
  c: "dd.category_" + category[c] + " a" for c in category
}

chrome.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# CPU 카테고리 선택
find_visible(category_css["cpu"]).click()
time.sleep(1)

# CPU 제조사 선택
options = finds_visible("div.search_option_wrap div.search_option_item:first-child span.item_text")
i = choose_one("CPU 제조사를 선택해주세요.", [x.text for x in options]) # CPU 제조사 출력
options[i].click() # CPU 제조사 선택

# CPU 종류 선택
if i == 0: # 인텔
  find_visible("div.search_option_wrap div.search_option_item:nth-child(2) button.btn_item_more").click() # 더보기 버튼 클릭
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) ul.search_cate_list span.item_text") # 인텔 CPU 종류 불러오기
elif i == 1:
  find_visible("div.search_option_wrap div.search_option_item:nth-child(3) button.btn_item_more").click() # 더보기 버튼 클릭
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(3) ul.search_cate_list span.item_text") # AMD CPU 종류 불러오기
i = choose_one("CPU 종류를 선택해주세요.", [x.text for x in options]) # CPU 종류 출력
options[i].click()

chrome.quit()