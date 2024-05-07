import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def find_keywords(driver, keywords):
    found_keywords = []
    page_content = driver.page_source.lower()
    for keyword in keywords:
        if keyword.lower() in page_content:
            found_keywords.append(keyword)
    return found_keywords

def click_links(driver, links):
    clicked_links = []
    for link_text in links:
        try:
            link_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, link_text))
            )
            link_element.click()
            clicked_links.append(link_text)
            time.sleep(2)  # wait for page reactions
        except (NoSuchElementException, TimeoutException):
            continue
    return clicked_links

def check_image_presence(driver, image_src):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//img[@src='{image_src}']"))
        )
        return True
    except TimeoutException:
        return False

def generate_report(found_keywords, clicked_links, image_found, total_time):
    report = f"User Preferences:\n- Keywords found: {found_keywords}\n- Links clicked: {clicked_links}\n- Image presence: {'Found' if image_found else 'Not Found'}\nTotal Reward Time: {total_time} seconds"
    return report

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")

    keywords = ["art", "probation", "music", "instruments"]
    links = ["About Us", "Contact"]
    image_src = "http://localhost:3000/path/to/image.jpg"
    reward_time = 10  # Time added per interaction
    total_reward_time = 0

    found_keywords = find_keywords(driver, keywords)
    total_reward_time += reward_time * len(found_keywords)

    clicked_links = click_links(driver, links)
    total_reward_time += reward_time * len(clicked_links)

    image_found = check_image_presence(driver, image_src)
    if image_found:
        total_reward_time += reward_time

    report = generate_report(found_keywords, clicked_links, image_found, total_reward_time)
    print(report)

    driver.quit()

if __name__ == "__main__":
    main()