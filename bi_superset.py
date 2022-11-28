from pickle import TRUE
import statistics
import requests
import json
import random
import string
import pandas as pd

def post(url, data):
  headers = {
        'Connection': 'keep-alive',
        'content-type': 'application/json;charset=UTF-8',
        'Cookie': 'session=.eJwtj81qAzEMhN_F5xxk_XitvMwi2RIpDQ3sJpeGvntdKDOXYfhg5l32POK8levzeMWl7B-zXEtNzAmgU6yRUFPiigDY66AYzFAJrM8GozfG7qG-GRMHxgwbqxERYjXJ5cBq3cCjyVDNnMFS1agLIAT9KSu4-RwOTaxjuZRxHrk_H5_xtfaQkmndfHOtZNaSGaEi5jbBFdw9nK3B4u6PYfdYzPdtpdcZx_-lXn5-ARM9QyU.Y3XdKA.TDBvKNTEzDRuhIYx9JqxtwR9JR4',
        'Host': 'bi.shie.com.cn',
        'Origin':'http://bi.shie.com.cn',
        'Referer':'http://bi.shie.com.cn/superset/sqllab/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-CSRFToken':'IjM5M2E5MTdiN2I5MTNhYTZmNDQyMDEyMmY3ZDBiOTBiYmJlYjRhNjAi.Y3XdKQ.o2VI1hzdejahyxu-7IU_Wgei5u8'
    }
  # print(json.dumps(data))
  return requests.post(url, data=json.dumps(data), headers=headers)


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def build_click_house_body(client_id, sql):
  data = {
  'client_id': client_id,
  'ctas_method': 'TABLE',
  'database_id': 19,
  'expand_data': True,
  'json': True,
  'queryLimit': 1000,
  'runAsync': False,
  'schema': 'zbkl',
  'select_as_cta': False,
  'sql': sql,
  'sql_editor_id': 'u2p1H6ibM',
  'tab': "1",
  'tmp_table_name': ''
  }
  return data

if __name__ == "__main__":
  url = 'http://bi.shie.com.cn/superset/sql_json/'
  # sql = "select sum(insured_number) from hzihc_gw_prod2023_t_ihc_order_main where com_name like '%个账%' and order_status='3' and bizinfo1='01' and create_time <('2022-11-15 23:59:00')"
  
  hmb = pd.read_excel("data/hmb统计.xlsx")
  stat = []
  for index, row in hmb.iterrows():
    sql = row[0]
    client_id = random_string_generator(9, string.ascii_letters)
    # print('Random String of length 9 =', client_id)
    data = build_click_house_body(client_id, sql)
    rs = post(url, data)
    result = rs.json()
    print(result['data'][0])
    stat.append(result['data'][0][row[1]])
  
  hmb['2020-11-17'] = stat
  hmb.to_excel("output/hmb统计.xlsx")