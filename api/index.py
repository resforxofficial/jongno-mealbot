from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def joiner(value):
    return value.get_attribute("outerHTML") if hasattr(value, "get_attribute") else "\n".join(str(i) for i in value)

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://jongno.sen.hs.kr/8920/subMenu.do")

content = WebDriverWait(driver, 10)
html = content.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents_375673"]/div[2]/div[2]/div/table')))

with open("../dist/index.html", "w", encoding="utf-8") as f:
    f.write(joiner(html))