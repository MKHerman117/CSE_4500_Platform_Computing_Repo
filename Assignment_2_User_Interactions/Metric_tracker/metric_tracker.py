import time
from selenium import webdriver
import collections
import csv 

def writeToCSV(filename : str, metrics : dict):
    with open(file=filename, mode="w", newline="") as fp:
   # Create a writer object
        writer = csv.DictWriter(fp, fieldnames=metrics.keys())

        #write the header row
        writer.writeheader()

        #Write the data row
        writer.writerow(metrics)     

def main():
# Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    #Initialize variables
    metrics = collections.defaultdict(list) #{Presence Time (Seconds) or Scrolling (Pixels) : Presence Time or Scroll}
    SAMPLE_SIZE = 5
    count = 0
    start_time = time.time()
    while count < SAMPLE_SIZE:             
        # Track presence time 
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        metrics["Presence time (Seconds)"].append(presence_time)

        # TIMESTAMP : "Presence Time (Seconds)" : Presence Time
        # TIMESTAMP : "Scrolling (Pixels)" : Scroll
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        metrics["Scrolling (Pixels)"].append(current_scroll/scroll_height)

        count += 1
        time.sleep(2) 

    # Track clicks   
    buttons = driver.find_elements(By.TAG_NAME,"button")
    num_clicks = 0

    for button in buttons:
        button.click()
    print(f"Number of clicks: {num_clicks}")
    num_clicks += 1
        
    driver.quit()
    print(metrics)
    writeToCSV("metrics.csv", metrics)

if __name__ == "__main__":
    main()    