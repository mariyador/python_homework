from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
results = []

try:
    driver.get('https://owasp.org/www-project-top-ten/')
    body = driver.find_element(By.CSS_SELECTOR,'body') 
    section = body.find_element(By.ID, 'sec-main')

    ul_lists = section.find_elements(By.TAG_NAME, 'ul')
    if len(ul_lists) >= 2:
        ul_with_vulnerabilities = ul_lists[1]
        links = ul_with_vulnerabilities.find_elements(By.TAG_NAME, 'a')

        for link in links:
            title = link.text.strip()
            url = link.get_attribute("href")
            if title and url:
                results.append({"title": title, "link": url})
    else:
        print("Could not find the second <ul> with vulnerabilities.")

except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
finally:
    driver.quit()

print(results)

with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for result in results:
        writer.writerow([result["title"], result["link"]])

print("Data saved to owasp_top_10.csv")