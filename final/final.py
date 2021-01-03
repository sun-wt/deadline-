#!/usr/bin/python3
import json
def txtReader(File):
    with open(File,encoding='utf-8') as f:
        result=f.read()
    return result
def jsonReader(File):
    with open(File,'r',encoding='utf-8') as f:
        result = json.load(f)
    return result
if __name__ == "__main__":
    txt = txtReader('../民法.txt')
    txt=txt.replace('\n','')
    # 先將文本中的換行去掉，因為法律條文並沒有用自動排版，而是手動換行

    # json=jsonReader('./replace.json')["replace"].replace_in_list(jsonReader('./replace.json')["replace"],jsonReader('./replace.json')["replacements"])
    # txtRaplace=txt.replace(txt, json["replacements"])
    #這邊是想要將DICT中的詞替換掉，不過還沒找到方法，上面是失敗的例子XD

    # print(json)