# coding=utf-8
from collections import defaultdict
from selenium import webdriver
import time
import re
import pickle

d = defaultdict(list)

for i in range(1,11):
    driver = webdriver.Firefox()
    driver.get("https://weibo.com/ayawawa?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={}\
    #feedtop".format(i))
    time.sleep(10)

    # 将页面滚动条拖到底部
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(5)
    driver.execute_script(js)
    time.sleep(5)

    target = re.compile(r'^key=profile_feed.*?comment:(\d*)$')
    elems = driver.find_elements_by_class_name('S_txt2')

    for elem in elems:
        if elem.get_attribute('suda-uatrack'):
            mid = re.search(target,str(elem.get_attribute('suda-uatrack')))
            if mid:
                d[i].append(mid.groups()[0])
    driver.quit()

with open('mids.plk','wb') as f:
    pickle.dump(d,f)
