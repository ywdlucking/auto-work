import json
import pandas as pd

def ReadLogFile(filename):
    f = open(filename)
    line = f.readline()
    list = []
    while line:
        ls = json.loads(line)
        if ls["level"] == "ERROR" :
            list.append(ls)
        line = f.readline()
    f.close()
    df = pd.DataFrame(list)
    print(df.shape)
    df.to_csv(filename+".csv", index=False, sep=",")
    return df

def divideFile(df, org):
    #通过机构org划分
    orgDf = df.loc[df['org'] == org].sort_values(by=['time', 'trace'])
    orgDf.to_csv(org+".csv", index=False, sep=",")
    print(org, "总异常数", orgDf.shape)
    contractEx = orgDf[orgDf.stack_trace.str.match(r'(.*)ContractCallException(.*)')]
    contractEx.to_csv(org+"_contract.csv", index=False, sep=",")
    print(org, "合约执行异常",contractEx.iloc[0]['time'],contractEx.shape[0])
    connectEx = orgDf[orgDf.stack_trace.str.match(r'(.*)ConnectException(.*)')]
    connectEx.to_csv(org+"_connect.csv", index=False, sep=",")
    print(org, "连接异常", connectEx.iloc[0]['time'], connectEx.shape[0])
    timeoutEx = orgDf[orgDf.stack_trace.str.match(r'(.*)SocketTimeoutException(.*)')]
    timeoutEx.to_csv(org+"_timeout.csv", index=False, sep=",")
    print(org, "超时异常", timeoutEx.iloc[0]['time'],timeoutEx.shape[0])
    sequenceEx = orgDf[orgDf.stack_trace.str.match(r'(.*)Error invalid sequence(.*)')]
    sequenceEx.to_csv(org+"_sequence.csv", index=False, sep=",")
    print(org, "sequenceEx异常", sequenceEx.iloc[0]['time'], sequenceEx.iloc[-1]['time'],sequenceEx.shape[0])
    ioEx = orgDf[orgDf.stack_trace.str.match(r'(.*)IOException(.*)')]
    ioEx.to_csv(org+"_ioex.csv", index=False, sep=",")
    print(org, "ioEx异常", ioEx.iloc[0]['time'], ioEx.iloc[-1]['time'],ioEx.shape[0])
    diff = orgDf.append(contractEx).append(connectEx).append(timeoutEx).append(sequenceEx).append(ioEx).drop_duplicates(subset=['time','org','trace'],keep=False)
    print(org, "剩余", diff.shape[0])
    diff.to_csv(org+"_diff.csv", index=False, sep=",")
    return orgDf

if __name__ == '__main__':
    rf = ReadLogFile('/home/ywd/workspace/python/excel/data/logs/log1.log')
    orglist = list(set([i for i in rf['org']]))
    print(orglist)
    for org in orglist:
        orgDf = divideFile(rf, org)