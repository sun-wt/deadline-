#!/usr/bin/python3
import sys,json,re
sys.path.append("../../../NTNU_TextProcessing_2020/week09/deadline/")
from ArticutAPI import ArticutAPI
def txtReader(File):
    with open(File,encoding='utf-8') as f:
        result=f.read()
    return result
def jsonReader(File):
    with open(File,'r',encoding='utf-8') as f:
        result = json.load(f)
    return result
def repl(target,replaceLIST,replacements):
    for i in range(len(target)):
        if target[i] in replaceLIST and target[i-1]=='[':
            continue
        elif target[i] in replaceLIST:
            n=replaceLIST.index(target[i])
            target=target.replace(target[i],replacements[n])
            i+=len(target)
    return target

def cut(target):
    articut=ArticutAPI.Articut()
    result=""
    for i in range(0, len(target), 2000):
        resultDICT=articut.parse(target[i:i+2000])
        result=result + resultDICT["result_segmentation"]
    return result
    
def addnote(target,con):
    for i in range(len(target)):
        if target[i] in con:
            # n=con.index(target[i])
            target.insert(i+1,'*')
            i=i+1
    return target

if __name__ == "__main__":
    articut=ArticutAPI.Articut()
    txt = txtReader('../民法.txt')
    # txt=txt.replace('\n','')
    # 先將文本中的換行去掉，因為法律條文並沒有用自動排版，而是手動換行
    replaceLIST=jsonReader('./replace.json')["Replace"]
    replacementsLIST=jsonReader('./replace.json')["replacements"]
    replaceNoun=jsonReader('./replace.json')["replaceNoun"]
    inputSTR=repl(txt,replaceLIST,replacementsLIST)
    result=cut(inputSTR)
    # result=articut.parse(inputSTR, level="lv1")
    # nounStemLIST = articut.getNounStemLIST(result)
    ReResulLIST=re.findall(r"(?<=\/).+?(?=\/)",result)
    noteResult=addnote(ReResulLIST,replaceNoun)
    resultSTR="".join(noteResult)
    print(resultSTR)
    # print(txt)