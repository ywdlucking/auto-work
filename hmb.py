import os
import re
import pandas as pd
import numpy as np
from functools import reduce
import time
import requests
import json


def get_pd_excel(path):
  return pd.read_excel(path)

def get_pd_csv(path):
  # 读取表头
  head_row = pd.read_csv(path, nrows=0)
  print(list(head_row))
  # 表头列转为 list
  head_row_list = list(head_row)
  return pd.read_csv(path, usecols=head_row_list).values.tolist()

def post(url, data):
  headers = {
        'content-type': "application/json;charset=UTF-8",
        'internaltoken': '4023b357470e4604994fcb6683cc74f7',
        'x-trailer-biz-product-line': 'k12'
    }
  return requests.post(url, data=json.dumps(data), headers=headers)

def statistics_err_money():
  remain = []
  holder_name = {}
  err_pd = get_pd_excel('data/金额错误.xlsx')
  holderAndName = get_pd_csv('data/错误金额对应投保人信息.csv')
  for holder in holderAndName:
    holder_name[holder[2]] = holder[1]
  # print(holder_name)
  for holder_no in err_pd['投保人证件号码']:
    json_data = { 
                  # "name": "曹杨", 
                  # "certiCode": "320125198708235811", 
                  "queryType": "1",
                  "certiType":"1",
                  "pcFlag": "1" 
                }
    json_data['name'] = holder_name[holder_no]
    json_data['certiCode'] =  holder_no
    # print(json_data)
    rs = post('http://hznihc-mdis.zkprod.shie.com.cn/hznihc-mdis/v1/hzyb/checkBalance', json_data)
    result=rs.json()#转化
    # print(result['data']['accountBalance'])
    if result['code'] == '00000' :
      remain.append(result['data']['accountBalance'])
    else:
      remain.append(0)
      print(json_data)

  err_pd['投保人余额'] = remain

  print(err_pd)

  err_pd.to_excel('output/金额错误.xlsx')

if __name__ == "__main__":
  statistics_err_money()
