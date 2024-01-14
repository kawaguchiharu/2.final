import time
import glob
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

tmp_dir = Path(Path.cwd(), "tmp")
tmp_dir.mkdir(exist_ok=True, parents=True)
options = Options()
prefs = {"download.default_directory": str(tmp_dir)}
options.add_experimental_option("prefs", prefs)

driver_path = "/Users/kawaguchiharu/Downloads/chromedriver"
chrome_service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service, options=options)

url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00130002&tstat=000001032793&cycle=7&year=20230&month=0&tclass1val=0"
driver.get(url=url)


# コピーしたCSSセレクタを文字列に格納
selector = "body > div.dialog-off-canvas-main-canvas > div > main > div.row.l-estatRow > section > div.region.region-content > div > div > div.stat-content.fix > section > section > div > div.stat-dataset_list > div > article:nth-child(4) > div > ul > li:nth-child(2) > div > div:nth-child(4) > div > a.stat-dl_icon.stat-icon_1.stat-icon_format.js-dl.stat-download_icon_left"
element = driver.find_element(by=By.CSS_SELECTOR, value=selector)
# 取得したWeb要素のHTMLを表示
print(element.get_attribute("outerHTML"))