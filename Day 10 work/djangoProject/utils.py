# 小组：01
# 作者：金石
# 创建时间：2023/6/13 09:08
# 文件名：utils.py
import json


def querySetToJson(para):
    res = []
    for i in para:
        res.append(i)
    return json.dumps(res, ensure_ascii=False)