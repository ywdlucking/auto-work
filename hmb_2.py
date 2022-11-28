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
  err_pd = get_pd_excel('data/最终扣款人员.xlsx')
  # print(holder_name)
  for index,row in err_pd.iterrows():
    # print(row['投保人身份证'], row['投保人姓名'])
    if row['投保人身份证'] == None:
      remain.append(" ")
      return
    json_data = { 
                  # "name": "曹杨", 
                  # "certiCode": "320125198708235811", 
                  "queryType": "1",
                  "certiType":"1",
                  "pcFlag": "1" 
                }
    json_data['name'] = row['投保人姓名']
    json_data['certiCode'] =  row['投保人身份证']
    # print(json_data)
    rs = post('http://hznihc-mdis.zkprod.shie.com.cn/hznihc-mdis/v1/hzyb/checkBalance', json_data)
    result=rs.json()#转化
    # print(result['data']['accountBalance'])
    if result['code'] == '00000' :
      remain.append(result['data']['accountBalance'])
    else:
      remain.append(0)
      print(json_data)
      print("error:", result)
    # remain.append(123)

  err_pd['投保人余额'] = remain

  print(err_pd)

  err_pd.to_excel('output/最终扣款人员.xlsx', index=False)

if __name__ == "__main__":
  statistics_err_money()
