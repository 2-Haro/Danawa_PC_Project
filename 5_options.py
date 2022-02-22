from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

category = {
  "cpu": "873",
  "mainboard": "875",
  "memory": "874",
  "graphic_card": "876",
  "ssd": "32617",
  "case": "879",
  "power": "880"
}

category_css = {
  c: "dd.category_" + category[c] + " a" for c in category
}

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
  products = []
  for p in finds_visible("div.scroll_box tr[class^=productList_]"):
    name = p.find_element_by_css_selector("p.subject a").text
    try:
      price = p.find_element_by_css_selector("span.prod_price").text
    except:
      continue
    products.append((name, price))
  return products

def go_to_category(category_name): # 카테고리 이동 함수
  find_visible(category_css[category_name]).click()
  time.sleep(1)
  
def choose_maker(text): # 제조사 선택 함수(더보기 버튼 X)
  options = finds_visible("div.search_option_wrap div.search_option_item:first-child span.item_text")
  i = choose_one(f"{text} 제조사를 선택해주세요.", [x.text for x in options])
  options[i].click()
  return i

def choose_maker_button(text): # 제조사 선택 함수(더보기 버튼 O)
  find_visible("div.search_option_wrap div.search_option_item:first-child button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:first-child span.item_text")
  i = choose_one(text, [x.text for x in options])
  options[i].click()

chrome.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# CPU 카테고리 선택
go_to_category("cpu")

# CPU 제조사 선택
maker_idx = choose_maker("CPU 제조사를 선택해주세요.")

# CPU 종류 선택
is_intel = False
is_AMD = False
if maker_idx == 0:
  is_intel = True
  find_visible("div.search_option_wrap div.search_option_item:nth-child(2) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) ul.search_cate_list span.item_text")
elif maker_idx == 1:
  is_AMD = True
  find_visible("div.search_option_wrap div.search_option_item:nth-child(3) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(3) ul.search_cate_list span.item_text")
i = choose_one("CPU 종류를 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# CPU 목록
cpus = parse_products()

# 메인보드 카테고리 선택
go_to_category("mainboard")

# 메인보드 제조사 선택
choose_maker_button("메인보드 제조사를 선택해주세요.")

# 메인보드 제품 분류 선택
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
if is_intel:
  options[0].click()
elif is_AMD:
  options[1].click()

time.sleep(1)

# 메인보드 목록
mainboards = parse_products()

# 메모리 카테고리 선택
go_to_category("memory")

# 메모리 제조사 선택
choose_maker_button("메모리 제조사를 선택해주세요.")

# 메모리 사용 장치 선택(데스크탑용)
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
options[0].click()

# 메모리 제품 분류 선택(DDR5)
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(3) span.item_text")
options[0].click()

# 메모리 용량 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(4) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(4) span.item_text")
i = choose_one("메모리 용량을 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# 메모리 목록
memories = parse_products()

# 그래픽카드 카테고리 선택
go_to_category("graphic_card")

# 그래픽카드 제조사 선택
choose_maker_button("그래픽카드 제조사를 선택해주세요.")

# 그래픽카드 칩셋 제조사
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
if is_intel:
  options[0].click()
elif is_AMD:
  options[1].click()

# 그래픽카드 칩셋 선택
if is_intel:
  find_visible("div.search_option_wrap div.search_option_item:nth-child(5) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(5) span.item_text")
elif is_AMD:
  find_visible("div.search_option_wrap div.search_option_item:nth-child(6) button.btn_item_more").click()
  options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(6) span.item_text")
i = choose_one("칩셋을 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# 그래픽카드 목록
graphic_cards = parse_products()

# SSD 카테고리 선택
go_to_category("ssd")

# SSD 제조사 선택
choose_maker_button("SSD 제조사를 선택해주세요.")

# SSD 제품분류 선택(내장형SSD)
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
options[0].click()

# SSD 용량 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(5) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(5) span.item_text")
i = choose_one("용량을 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# SSD 목록
ssds = parse_products()

# 케이스 카테고리 선택
go_to_category("case")

# 케이스 제조사 선택
choose_maker_button("케이스 제조사를 선택해주세요.")

# 케이스 제품 분류 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(2) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
i = choose_one("제품을 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# 케이스 목록
cases = parse_products()

# 파워 카테고리 선택
go_to_category("power")

# 파워 제조사 선택
choose_maker_button("파워 제조사를 선택해주세요.")

# 파워 제품 분류 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(2) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(2) span.item_text")
i = choose_one("제품을 선택해주세요.", [x.text for x in options])
options[i].click()

# 파워 정격출력 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(3) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(3) span.item_text")
i = choose_one("정격출력을 선택해주세요.", [x.text for x in options])
options[i].click()

# 파워 80PLUS인증 선택
find_visible("div.search_option_wrap div.search_option_item:nth-child(4) button.btn_item_more").click()
options = finds_visible("div.search_option_wrap div.search_option_item:nth-child(4) span.item_text")
i = choose_one("80PLUS인증을 선택해주세요.", [x.text for x in options])
options[i].click()

time.sleep(1)

# 파워 목록
powers = parse_products()

chrome.quit()