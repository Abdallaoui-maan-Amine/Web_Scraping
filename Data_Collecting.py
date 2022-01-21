#Requirements
# il est possible de lancer l'execution du code a partir du cmd (Windows Prompt) 


##############################################################################
################# NB:Please specify the output file name #####################
##############################################################################
file='Essai.csv'




import os
try:
    import selenium
except ImportError:
    print('[+] installing Selenium Library ...')
    os.system('python -m pip install selenium')
    import selenium
    
    
try:
    import pandas as pd
except ImportError:
    print('[+] Installing Pandas library ...')
    os.system('python -m pip install pandas')
    import pandas as pd

try:
    import requests
except ImportError:
    print('[+] installing requests Library...')
    os.system('python -m pip install pandas')
    import requests  

try:
    import bs4
except ImportError:
    print('[+] installing beautifulsoup4 Library...')
    os.system('python -m pip install beautifulsoup4')
    import bs4     


    
    
# import selenium
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
start_time = time.time()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
os.system('cls')

option = webdriver.ChromeOptions()
chrome_prefs = {}
os.system('cls')
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
os.system('cls')

PATH = "chromedriver.exe"

PATH = "E:\Amine PC\PFE\BigData\chromedriver.exe"

driver = webdriver.Chrome(PATH,chrome_options=option)
os.system('cls')
driver.get("https://www.goud.ma/topics/%d8%a2%d8%b4-%d9%88%d8%a7%d9%82%d8%b9/")

time.sleep(1)

ActionChains(driver).move_by_offset (10, 200).click().perform ()
ActionChains(driver).move_by_offset (10, 200).click().perform ()



##############################################################################
############## NB:Please specify number 'n' of page content ##################
########################### In this case n =2 ################################
##############################################################################

i=0
print('\n   [+] Loading ...')
while i<2:
    
    button = driver.find_element(By.XPATH, '//button[text()="المزيد"]')
    time.sleep(1.5)
    driver.execute_script("arguments[0].click();", button)
    i=i+1
    #print(i)
    

RM_links=driver.find_elements_by_class_name('read-more')
links=[]
for a in RM_links:
    links.append(a.get_attribute('href'))
    
links=links[:-1]   

print("--- %s seconds ---\n\n" % (time.time() - start_time))

driver.quit()



import time
start_time = time.time()
df=pd.DataFrame(columns=['Post_text','Polarite','Time','Date'])
#T=[]
os.system('cls')
index=df.shape[0]
print('\n   [+] Saving Data ...')
for page in links:
    Response_General = requests.get(page)
    CodePage_General = bs4.BeautifulSoup(Response_General.text, 'lxml' )
    Balise_Review = CodePage_General.select('div.content p')
    Balise_time = CodePage_General.select('span.date')
    Time=((Balise_time[0].text).split(" "))[1]
    Date=((Balise_time[0].text).split(" "))[0]
    Balise_Review = Balise_Review[1:]
    for tag in Balise_Review:
        df.at[index,'Post_text']=tag.get_text()
        df.at[index,'Time']=Time
        df.at[index,'Date']=Date
        index=index+1
    
#df
print("--- %s seconds ---\n\n" % (time.time() - start_time))
df.to_csv(file, index=False, encoding='utf-8-sig')
os.system(file)
