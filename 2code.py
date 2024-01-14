import time
import glob
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ダウンロードファイルの一時保存フォルダを作成
tmp_dir = Path(Path.cwd(), "tmp")
tmp_dir.mkdir(exist_ok=True, parents=True)

# webdriverにオプションを追加
options = Options()
prefs = {"download.default_directory": str(tmp_dir)}
options.add_experimental_option("prefs", prefs)

# chromedriverのパスを指定
driver_path = "/Users/kawaguchiharu/Downloads/chromedriver"
chrome_service = Service(executable_path=driver_path)

# 追加したオプションを設定してwebdriverを起動
driver = webdriver.Chrome(service=chrome_service, options=options)

# e-Statsのcsvダウンロードページにアクセス
url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00130002&tstat=000001032793&cycle=7&year=20230&month=0&tclass1val=0"
driver.get(url=url)