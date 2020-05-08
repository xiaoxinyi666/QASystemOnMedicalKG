import requests
from bs4 import BeautifulSoup
import jieba
import jieba.posseg as pseg  # 词性标注
import synonyms


def visit_baidu(msg):
    try:
        jieba.load_userdict("dict.txt")
        n_flags = ["ns", "n", "nr", "nz", "nt", "nw", "t"]
        words = pseg.cut(msg, use_paddle=True)
        task = []
        for word, flag in words:
            print(word, flag)
            if flag in n_flags:
                task.append(word)
        print("分词结果如下:", task)
        headers = {
            "User-Agent": "Mozilla/5.0 "
        }

        if len(task) == 1:
            word = task[0]
            api = 'https://baike.baidu.com/search/word?word=' + word
            r = requests.get(api, headers=headers, timeout=10)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            content = soup.findAll(name='meta', attrs={"name": "description"})
            content = content[0]['content']
            return content

        if len(task) > 1:
            word = task[0]
            target = ""
            for i in task:
                target = target + i
            target = target.replace(word, "")
            print(target)
            api = 'https://baike.baidu.com/search/word?word=' + word
            r = requests.get(api, headers=headers, timeout=10)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            names = []
            for i in soup.select(".basicInfo-item.name"):
                if i.text.replace("\xa0", ""):
                    names.append(i.text.replace("\xa0", ""))
            values = []
            for i in soup.select(".basicInfo-item.value"):
                if i.text.replace("\xa0", ""):
                    values.append(i.text.replace("\xa0", ""))
            info_items = []
            for i in range(len(names)):
                item = {
                    "name": names[i],
                    "value": values[i]
                }
                info_items.append(item)
            similarity = -1
            result = "什么也没有找到~~"
            for item in info_items:
                compare = synonyms.compare(target, item["name"], seg=False)
                if compare > similarity:
                    similarity = compare
                    print(item["name"])
                    result = item["value"]
            return "已经为你找到如下信息:\r" + result
    except Exception as e:
        print(e)
        return "抱歉出错了什么也没找到~"


