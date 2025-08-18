from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = driver.find_elements(By.CSS_SELECTOR, "#customers tr")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if cells:
        print([cell.text for cell in cells])

driver.quit()
