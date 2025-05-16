from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import logging

# === 設定 Logging ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("selenium_log.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# === Mobile Emulation 設定（可調整為桌面）===
mobile_emulation = {"deviceName": "Pixel 7"}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

# === 驅動初始化 ===
try:
    driver = webdriver.Chrome(options=options)
    logging.info("Chrome driver 啟動成功")
except Exception as e:
    logging.error(f"無法啟動 Chrome driver：{e}")
    raise

# === 導向目標網站 ===
try:
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(5)
    screenshot_path = os.path.join(os.getcwd(), "screenshot/cathay_homepage.png")
    driver.save_screenshot(screenshot_path)
    logging.info(f"首頁截圖已儲存：{screenshot_path}")
except Exception as e:
    logging.error(f"載入網站失敗：{e}")
    driver.quit()
    raise

# === 點擊展開選單 ===
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[1]/div/div[2]'))
    ).click()
    time.sleep(1)
except Exception as e:
    logging.error(f"展開選單失敗：{e}")

# === 點擊第一層級選單項目 ===
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[1]/div'))
    ).click()
    time.sleep(1)
except Exception as e:
    logging.error(f"點擊第一層項目失敗：{e}")

# === 點擊次選單與統計 a 元素 ===
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]'))
    ).click()
    time.sleep(1)
    
    parent = driver.find_element(By.XPATH, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]')
    links = parent.find_elements(By.TAG_NAME, 'a')
    logging.info(f"找到 {len(links)} 個項目")
    for i, link in enumerate(links, 1):
        logging.info(f"第 {i} 行文字：{link.text}")
except Exception as e:
    logging.error(f"處理次選單失敗：{e}")

# === 點擊「停發卡」項目 ===
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="spa-root"]/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/header/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/a[1]'))
    ).click()
    time.sleep(1)

    target = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[p[text()="停發卡"]]'))
    )
    driver.execute_script("arguments[0].click();", target)
    time.sleep(1)
except Exception as e:
    logging.error(f"點擊「停發卡」項目失敗：{e}")

# === 點擊每張卡片按鈕與截圖 ===
try:
    parent = driver.find_element(By.XPATH, '/html/body/div/main/article/section[6]/div/div[2]/div/div[2]')
    buttons = parent.find_elements(By.XPATH, './/span[@role="button"]')
    logging.info(f"共 {len(buttons)} 張信用卡")
    for index, btn in enumerate(buttons, 1):
        try:
            logging.info(f"嘗試點擊第 {index} 張信用卡")
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
            screenshot_path = os.path.join(os.getcwd(), f"screenshot/discard_card{index}.png")
            driver.save_screenshot(screenshot_path)
            logging.info(f"已儲存第 {index} 張信用卡的截圖：{screenshot_path}")
        except Exception as e:
            logging.warning(f"第 {index} 張卡片點擊失敗：{e}")
except Exception as e:
    logging.error(f"處理卡片按鈕區塊失敗：{e}")

# === 結束測試 ===
driver.quit()
logging.info("測試結束，driver 關閉。")
