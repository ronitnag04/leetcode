"""
0. Make sure to complete S1_get_submitted_problems step first
1. a. Make sure chrome driver from https://chromedriver.chromium.org/downloads is installed in the sync_work_path
   b. Update root_path, sync_work_path, and driver_path variables below
2. Run script, and login to leetcode when browser opens. 
3. Wait for scraper to parse through all solved problems. This step takes about 2s per problem
4. Ensure sync_values_distributions.csv file is in sync work path
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import numpy as np

root_path = ""  # Replace with your working directory (e.g 'C:/Users/<YOUR_USER_NAME>/OneDrive/Desktop/leetcode/' )
sync_work_path = '' # default sync-problems-template/

driver_path = root_path + sync_work_path + "chromedriver" 
time_delay = 10 # Set higher if you have a slow connection


df_sync_values = pd.read_csv(root_path + sync_work_path + 'sync_values.csv')


print('Starting Scraper')
chrome_options = Options()
chrome_options.add_argument("start-maximized")
print('Built Options')
driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=chrome_options)
print('Driver Installed')


def getPercentages(link):
    driver.get(link)

    try:
        WebDriverWait(driver, time_delay).until(
            EC.title_contains('Submission Detail')
        )
    except:
        raise Exception('Make sure the Login quickly! Try again')

    try:
        runtime_element = WebDriverWait(driver, time_delay).until(
            EC.presence_of_element_located((By.ID, "runtime_detail_plot_placeholder"))
        )
    except:
        raise Exception('Runtime element not found')

    try:
        memory_element = WebDriverWait(driver, time_delay).until(
            EC.presence_of_element_located((By.ID, "memory_detail_plot_placeholder"))
        )
    except:
        raise Exception('Memory element not found')

    runtime_text = runtime_element.text
    runtime_percentage = runtime_text

    memory_text = memory_element.text
    memory_percentage = memory_text

    return runtime_percentage, memory_percentage

def getRuntimePercentage(text):
    splits = text.split('Your runtime beats ')
    if len(splits) == 2:
        return splits[1][0:5] + '%'
    else:
        return np.nan

def getMemoryPercentage(text):
    splits = text.split('Your memory usage beats ')
    if len(splits) == 2:
        return splits[1][0:5] + '%'
    else:
        return np.nan

runtime = []
memory = []
total_questions = len(df_sync_values)

for i, row in df_sync_values.iterrows():
    link = row['Best Score Url']
    runtime_percentage_element, memory_percentage_element = getPercentages(link)
    runtime_percentage = getRuntimePercentage(runtime_percentage_element)
    memory_percentage = getMemoryPercentage(memory_percentage_element)
    print(f'{i+1}/{total_questions} Extracted -- Runtime: {runtime_percentage}, Memory: {memory_percentage}')
    runtime.append(runtime_percentage)
    memory.append(memory_percentage)

df_sync_values['Best Runtime Percentage'] = runtime
df_sync_values['Best Memory Percentage'] = memory
df_sync_values.to_csv(root_path + sync_work_path + 'sync_values_distributions.csv')