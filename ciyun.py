import jieba
from wordcloud import WordCloud


#读取目标文本文件
def get_str(path):
  f = open(path,encoding="utf-8")  
  data = f.read()
  f.close()
  return data

#设置分词
def lcut(str):
  jieba.del_word('人民战争')
  jieba.suggest_freq('人民')
  jieba.suggest_freq('安全')
  jieba.suggest_freq('现代化')
  return jieba.lcut(str)

#计算频率，返回频次最高的15个
def count(words):
  counts = {}
  for word in words:
    if len(word) == 1:
      continue
    else:
      counts[word] = counts.get(word,0) + 1

  items = list(counts.items())
  items.sort(key=lambda x:x[1], reverse=True) 
  newtxts = []
  for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
    newtxts.append(word)
  
  newtxt = ' '.join(newtxts)    #空格拼接

  return newtxt

##画词云图片
def drawWordCloud(word, outfile):
  wordcloud = WordCloud(font_path="data/test.ttf",background_color="white",width=800,height=600).generate(word)
  wordcloud.to_file(outfile)

if __name__ == "__main__":
  str = get_str("data/20.txt")
  slcut = lcut(str)
  word = count(slcut)
  drawWordCloud(word, "output/20da.jpg")