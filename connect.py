from nltk.corpus import words
from itertools import permutations
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://127.0.0.1:5600')
browser.maximize_window()

#logging into my dc hub

login = browser.find_element_by_xpath('//*[@id="background-wrapper"]/div/div/form/div/div[1]/div/input')
login.send_keys("param")
password = browser.find_element_by_xpath('//*[@id="background-wrapper"]/div/div/form/div/div[2]/div/input')
password.send_keys("param")
btn = browser.find_element_by_xpath('//*[@id="background-wrapper"]/div/div/form/div/button')
btn.click()
browser.implicitly_wait(10)

#going to my hub

hub = browser.find_element_by_xpath('//*[@id="side-menu"]/div[1]/div/a[1]')
hub.click()
game = browser.find_element_by_xpath('//*[@id="sidebar-container"]/div/div[1]/div/a[3]/span')
game.click()

#successfully reached to anagram game

browser.implicitly_wait(10)
mid = browser.find_element_by_xpath('//*[@id="sidebar-container"]/div/div[2]/div/div[3]/div[1]/div[1]/div/div[92]/div[2]/div[2]').text

#function to get the substring required. It slices from start to end
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#function to get the substring required. It slices from end to start
def find_between_rev( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

#different functions will give different results in case of repitition of strings,
#so we know when to use which function

text = find_between( mid, "[", "]" )
text = text.replace(' ', '')

#now finally got all the words that I need
def check_ana(s):
    F = "".join(sorted(s))#-->i have the sorted list now
    # loop through comparison list
    perms = set([''.join(p) for p in permutations(F)])
    print(s)
    for p in perms:
        if(p in words.words()):
            print(p)
            break

check_ana("".join(sorted(text)))
