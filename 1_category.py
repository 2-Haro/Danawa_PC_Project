from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)

def find_present(css_selector): # 보이지는 않아도 페이지상에 존재하는 element를 반환하는 함수
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_present(css_selector): # 보이지는 않아도 페이지상에 존재하는 element를 모두 반환하는 함수
  find_present(css_selector)
  return chrome.find_elements_by_css_selector(css_selector)

def find_visible(css_selector): # 페이지상에 보이는 element를 반환하는 함수
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_visible(css_selector): # 페이지상에 보이는 element를 모두 반환하는 함수
  find_visible(css_selector)
  return chrome.find_elements_by_css_selector(css_selector)

category = { # 각각의 카테고리에 부여되어 있는 코드 내의 고유한 번호(category_000)
  "cpu": "873",
  "mainboard": "875",
  "memory": "873",
  "graphic_card": "873",
  "ssd": "32617",
  "case": "879",
  "power": "880"
}

chrome.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")
mainboard = find_visible("dd.category_" + category["mainboard"] + " a") # 메인보드 카테고리
mainboard.click() # 메인보드 카테고리 클릭

time.sleep(5)

chrome.quit()