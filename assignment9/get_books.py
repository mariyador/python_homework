from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd
import json
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

# Task 3: Write a Program to Extract this Data

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
sleep(2)

book_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

results = []

for li in book_items:
    try:
        # Title
        title_elem = li.find_element(By.CSS_SELECTOR, 'span.title-content')
        title = title_elem.text.strip()

        # Author
        author_links = li.find_elements(By.CSS_SELECTOR, 'a.author-link')
        authors = "; ".join([a.text.strip() for a in author_links]) if author_links else "Unknown"

        # Format and year
        format_div = li.find_element(By.CSS_SELECTOR, 'div.cp-format-info > span')
        format_year = format_div.text.strip()

        # Results
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    except Exception as e:
        print("Skipping one item due to error: {e}")

driver.quit()

df = pd.DataFrame(results)
print(df)


#Task 4: Write out the Data
# Save to CSV
df.to_csv("get_books.csv", index=False)
print("Data saved to get_books.csv")

# Save to JSON
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
print("Data saved to get_books.json")
