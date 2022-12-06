from multiprocessing.connection import wait
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery

import time

import pandas as pd
import json 
from pandas import json_normalize

KEYWORD='iPad'
# 指定driver的绝对路径
driver = webdriver.Chrome('/home/ywd/tool/chromedriver')
# df = pd.DataFrame() # DataFrame数据格式，用于保存到本地

#设置等待时间10s
wait=WebDriverWait(driver, 30)

def crawl_page(page):
  try:
    url='https://s.taobao.com/search?q='+quote(KEYWORD)
    driver.get(url)

    #沉睡5s，用手机app扫码登录
    time.sleep(15)

    if page>1:
      page_box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input.J_Input')))
      submit_btn=wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, 'span.btn.J_Submit'))

      page_box.clear()
      page_box.send_keys(page)
      submit_btn.click()
    
    wait.until(
      ##定位元素
      EC.presence_of_element_located(
        (By.CSS_SELECTOR,'.m-itemlist .items .item')
      )
    )

    get_products()
  except Exception as e:
    print('发生了异常：',e)
    crawl_page(1)

def get_products():
  #获取源码
  html=driver.page_source
  #解析
  doc=PyQuery(html)
  items=doc('#mainsrp-itemlist .items .item').items()
  products=[]
  for item in items:
    product={
      'image': item.find('.pic .img').attr('data-src'),
      'price': item.find('.price').text(),
      'deal': item.find('.deal-cnt').text(),
      'title': item.find('.title').text(),
      'shop': item.find('.shop').text(),
      'location': item.find('.location').text()
    }
    # print(product)
    # data = pd.DataFrame(product)
    products.append(product)

  df = json_normalize(products)
  #保存到本地
  df.to_excel("output/products.xlsx",encoding='utf-8-sig',index=False)

crawl_page(1)