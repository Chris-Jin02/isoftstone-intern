#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 14:53
"""
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
words = [
    ("武汉",2.64),("医院",4.03),("口罩",24.95),("硬核",4.04),("致敬",5.27),
    ("陪伴",5.800),("学习",3.09),("健康",24.71),("网课",6.33),("医生",2.55),
    ("战士",3.88),("娱乐",8.04),("购物",5.87),("短视频",6.97)
]
wordCloud = (
    WordCloud(init_opts=opts.InitOpts(width="600px", height="400px"))
    .add(
        "",
        words,
        word_size_range=[20, 100],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
#可选： circle,cardioid,diamond,triangle-forward,triangle,pentagon,star
#       “圆形”、“心形”、“菱形”、“三角形向前”、   “三角形”、“五角大楼”、“星形”
        # shape='cardioid'
        shape=SymbolType.DIAMOND #箭头型---没看出来
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="人们最关系的话题",pos_left="center"))
    .render("/Users/steve/Desktop/项目/实习/Day 8 work/html/疫情期间人们最关系的话题_词云图2.html")
)
