import os
import re
import pandas as pd
import numpy as np
from functools import reduce
import time
import requests
import json
import csv


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

def statistics_err_money_sql_update():
  ins_update = []
  order_update = []
  holder_name = {}
  err_pd = get_pd_excel('data/最终修改订单.xlsx')
  ceti_codes = err_pd['参保人身份证'].to_numpy()
  # print(ceti_codes)
  main_order = get_pd_csv('data/修改订单.csv')
  ins_order = get_pd_csv('data/修改保单.csv')
  sql_o = "UPDATE t_ihc_order_main SET sum_premium =(sum_premium + 50) ,sum_amount =(sum_amount +50),proposal_json='{0}' WHERE order_no ='{1}';"
  json_map = {}
  for order in main_order:
    # print(order[23], order[24])
    # proposal_json = {}
    json_map[order[1]] = json.loads(order[26])
  
  for ins in ins_order:
    proposal_json = json_map[ins[1]]
    for key in range(len(proposal_json["issureds"])):
      ins_obj = proposal_json["issureds"][key]
      if ins_obj['certiCode'] in  ceti_codes:
        ins_obj['orderFee'] = 150
        ins_obj['payFee'] = 150
        proposal_json["issureds"][key] = ins_obj
    json_map[ins[1]] = proposal_json

  sql_i = "UPDATE t_ihc_order_insured SET pay_fee=pay_fee+50, order_fee=order_fee+50  WHERE order_no='{0}' AND certi_code='{1}';"
  for ins in ins_order:
    sql = sql_i.format(ins[1], ins[5])
    ins_update.append(sql)
    proposal_str = json.dumps(json_map[ins[1]], ensure_ascii=False)
    sql2 = sql_o.format(proposal_str, ins[1])
    order_update.append(sql2)
  dataframe = pd.DataFrame({'ins_update':ins_update})
  dataframe.to_excel("output/ins_update.xlsx",index=False,header=False)
  dataframe2 = pd.DataFrame({'order_update':order_update})
  dataframe2.to_excel("output/order_update.xlsx",index=False,header=False)

if __name__ == "__main__":
  statistics_err_money_sql_update()
