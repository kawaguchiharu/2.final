from selenium import webdriver

# ChromeDriverのパスを指定
chrome_driver_path = "/path/to/chromedriver"

# ChromeOptionsを作成し、ChromeDriverのパスを設定
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_driver_path

