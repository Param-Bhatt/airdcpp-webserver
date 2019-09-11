from itertools import permutations
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def check_ana(s):
    s = s.lower()
    # loop through comparison list
    perms = set([''.join(p) for p in permutations(s)])
    for p in perms:
        p = p + "\n"
        with open('Words.txt') as f:
            if p in f.read():
                print(p)
                return p
    f.close()

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def execute():
    i=72
    while ( i ):
        mid = browser.find_element_by_xpath('//*[@id="sidebar-container"]/div/div[2]/div/div[3]/div[1]/div[1]/div/div['+str(i)+']/div[2]/div[2]/span').text
        if ( "Anagram Game was stopped" in mid ):
            exit()
        elif ( "New" in mid):
            text = find_between(mid, "[", "]")
            text = text.replace(' ', '')

        # now finally got all the words that I need

            ans = check_ana("".join(sorted(text)))
            print(ans)
            #send = browser.find_element_by_xpath("//*[@id='sidebar-container']/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/textarea")
            #send.send_keys(ans)
            #click = browser.find_element_by_xpath("//*[@id='sidebar-container']/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/i")
            #click.click()
            i+=1
        else :
            i+=1
            continue

#function to get the substring required. It slices from end to start
def find_between_rev( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

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
browser.implicitly_wait(10)

game = browser.find_element_by_xpath('//*[@id="sidebar-container"]/div/div[1]/div/a/span')
game.click()

#successfully reached to anagram game

browser.implicitly_wait(10)

''' -----------------Start the for loop from here----------------
mid = browser.find_element_by_xpath('//*[@id="sidebar-container"]/div/div[2]/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div[2]/span').text
''<!--   Function definition around here -->''
#function to get the substring required. It slices from start to end

#different functions will give different results in case of repitition of strings,
#so we know when to use which function

text = find_between( mid, "[", "]" )
text = text.replace(' ', '')

#now finally got all the words that I need

ans = check_ana("".join(sorted(text)))
send = browser.find_element_by_xpath("//*[@id='sidebar-container']/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/textarea")
send.send_keys(ans)
click = browser.find_element_by_xpath("//*[@id='sidebar-container']/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/i")
click.click()
'''
execute()