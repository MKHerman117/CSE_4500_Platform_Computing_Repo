import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def find_keywords(driver, keywords):
    page_content = driver.page_source.lower()
    for keyword in keywords:
        if keyword.lower() in page_content:
            return True
    return False

def click_link(driver, link_text):
    try:
        link_element = driver.find_element(By.LINK_TEXT, link_text)
        link_element.click()
        return True
    except NoSuchElementException:
        return False

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get("http://localhost:3000/")

        # Define user preferences
        keywords = ["panama", "soccer", "trilingual"]
        preferred_links = ["GitHub"]
        preferred_image_src = "https://wallpaper.dog/large/10876668.jpg"

        # Reward time for engaging elements
        reward_time = 10
        total_reward_time = 0

        # Check for keywords
        if find_keywords(driver, keywords):
            print("Keywords found. Extending presence time by", reward_time, "seconds.")
            total_reward_time += reward_time

        # Click preferred links
        for link_text in preferred_links:
            if click_link(driver, link_text):
                print("Clicked on link:", link_text)
                total_reward_time += reward_time

        # Wait for the preferred image to be present and visible
        try:
            img_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//img[@src='{preferred_image_src}']"))
            )
            print("Preferred image found and visible. Extending presence time by", reward_time, "seconds.")
            total_reward_time += reward_time
        except TimeoutException:
            print("Preferred image not found within the specified time.")

        # Simulate staying on the site for the reward time
        time.sleep(total_reward_time)

    finally:
        # Close the browser
        driver.quit()

        print("Total Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()
    

