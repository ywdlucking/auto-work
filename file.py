from json.tool import main
import re

#读取目标文本文件
def get_str(path):
    f = open(path,encoding="utf-8")  
    data = f.read()
    f.close()
    return data

#正则获取文本号码
def get_phone_number(str):
    res = re.findall(r'(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', str)
    return res

#保存
def save_res(res,save_path):
    save_file = open(save_path, 'w') 
    for phone in res: 
        save_file.write(phone) 
        save_file.write('\n') 
    save_file.write('\n号码共计：'+str(len(res)))
    save_file.close() 
    print('号码读取OK，号码共计：'+str(len(res)))


if __name__ == "__main__":

  st = get_str("data/金额错误.csv")
  rs = get_phone_number(st)
  save_res(rs, "output/金额错误.csv")