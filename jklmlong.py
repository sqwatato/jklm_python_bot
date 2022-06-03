from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager# Initiate the browser
from selenium.webdriver.common.keys import Keys
import time
import random

browser  = webdriver.Chrome(ChromeDriverManager().install())
code = input("Enter lobby code: ")
browser.get(f'https://jklm.fun/{code.upper()}')

words = []
with open("dict.txt","r") as data:
    words = data.readlines()
words = list(map(str.strip,words))
lengths = {}
for word in words:
    try:
        lengths[len(word)].append(word)
    except:
        lengths[len(word)] = [word]
key = sorted(lengths.keys(),reverse=True)
used = set()
let = set()

def rank(word:str):
    wlet = set(word)
    score = len(wlet.difference(let))
    return score


while True:
    WebDriverWait(browser, 100000).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@src=\"https://phoenix.jklm.fun/games/bombparty\"]")))
    wait = WebDriverWait(browser, 1000000)
    if browser.find_element(By.XPATH,"//div[@class=\"selfTurn\"]").is_displayed():
        elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='styled'][@type='text']")))
        time.sleep(0.4)
        prompt = browser.find_element(By.XPATH,"//div[@class=\"syllable\"]").text
        for i in key:
            ranked = []
            for word in random.sample(lengths[i],len(lengths[i])):
                if prompt in word and word not in used:
                    ranked.append((word,rank(word)))
            ranked.sort(key=lambda x: x[1],reverse=True)
            if len(ranked) != 0:
                word = ranked[0][0]
                if browser.find_element(By.XPATH,"//input[@class='styled'][@type='text']").is_displayed():
                    time.sleep(0.3)
                    #elem = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='styled'][@type='text']")))
                    elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='styled'][@type='text']")))
                    elem.send_keys(word)
                    elem.send_keys(Keys.ENTER)
                    used.add(word)
                    let = let.union(set(word))
                    if len(let) == 26:
                        let.clear()
                    break
                
            else:
                continue
            break
       
    browser.switch_to.default_content()
    #time.sleep(0.3)



