#Web Scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:8989")


url = 'https://www.youtube.com/c/NikolajMitrofanov'
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:/Users/clib_/Desktop/UNIVERSE/PROGRAMMING/PYTHON/GIT-WEBSCRAPE/webscrape_clicker/chromedriver/chromedriver.exe")
driver.get(url)


element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="items"]/ytd-grid-video-renderer[5]'))
)

#using ActionChains instead to click
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
