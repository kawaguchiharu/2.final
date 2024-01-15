import time
import glob
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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

# コピーしたCSSセレクタを文字列に格納
selector = "body > div.dialog-off-canvas-main-canvas > div > main > div.row.l-estatRow > section > div.region.region-content > div > div > div.stat-content.fix > section > section > div > div.stat-search_result-files > div.stat-resource_download_filed > div:nth-child(2) > a.stat-dl_icon.stat-icon_1.stat-icon_format.js-dl.stat-download_icon_top"
element = driver.find_element(by=By.CSS_SELECTOR, value=selector)

# 取得したWeb要素のHTMLを表示
print(element.get_attribute("outerHTML"))

#スクレイピング完了

#DBに格納

import csv
import sqlite3

# ダウンロードファイルのパスを指定
downloaded_file_path = tmp_dir / "downloaded_file.csv"

# CSVファイルからデータを読み込み
with open(downloaded_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  

# データベースに接続   
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

# テーブルの作成
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS your_table_name (
        column1_type,
        column2_type,
        ...
    )
    '''
    cursor.execute(create_table_query)

# データの挿入
    insert_data_query = f'INSERT INTO your_table_name VALUES ({", ".join(["?"] * len(header))})'
    for row in csv_reader:
        cursor.execute(insert_data_query, row)

# コミットしてclose
    conn.close()
