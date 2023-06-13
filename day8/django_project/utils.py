# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/12 21:13
# 文件名：utils.py

import json


def querySetToJson(para):
    res = []
    for i in para:
        res.append(i)
    return json.dumps(res, ensure_ascii=False)

