#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/5/28 1:16
"""
import json

def querySetToJson(para):
    res = []
    for i in para:
        res.append(i)
    return json.dumps(res, ensure_ascii=False)
