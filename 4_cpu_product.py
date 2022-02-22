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

def parse_products(): # 상품 목록 불러오기 함수
  products = [] # 상품 목록(리스트)
  for p in finds_visible("div.scroll_box tr[class^=productList_]"):
    name = p.find_element_by_css_selector("p.subject a").text # 광고가 아닌 목록
    try:
      price = p.find_element_by_css_selector("span.prod_price").text # 광고가 아닌 가격
    except:
      continue
    products.append((name, price)) # 상품 목록(리스트)에 append
  return products

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
i = choose_one("CPU 제조사를 선택해주세요.", [x.text for x in options])
options[i].click()

# CPU 종류 선택
if i == 0:
  find_visible("div.search_option_wrap div.search_option_item:nth-child(2) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) ul.search_cate_list span.item_text")
elif i == 1:
  find_visible("div.search_option_wrap div.search_option_item:nth-child(3) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(3) ul.search_cate_list span.item_text")
i = choose_one("CPU 종류를 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# 선택한 CPU 목록
cpus = parse_products()
for cpu in cpus:
  print(cpu) # CPU 이름과 가격 출력

chrome.quit()