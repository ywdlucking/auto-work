import json
import pandas as pd

def ReadLogFile(filename, trace):
    f = open(filename)
    line = f.readline()
    list = []
    while line:
        ls = json.loads(line)
        if ls["trace"] == trace :
            list.append(ls)
        line = f.readline()
    f.close()
    df = pd.DataFrame(list)
    print(df.shape)
    df.to_csv(filename+"_"+trace+".csv", index=False, sep=",")
    return df

if __name__ == '__main__':
    rf = ReadLogFile('/home/ywd/workspace/python/excel/data/logs/log1.log', "5fdcce788ace4a249dce655af6333008")
