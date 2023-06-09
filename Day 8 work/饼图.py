#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 14:37
"""
import  pyecharts.charts as charts
from pyecharts import options as opts
pie=charts.Pie(init_opts=opts.InitOpts(width="600px", height="400px"))
pie.set_global_opts(
        title_opts={"text":"七大区域确诊人数","subtext":"数据来源于网络"},
        # 添加为纵向的类别----默认横向
        legend_opts=opts.LegendOpts(type_="scroll",pos_top="20%", pos_left="left", orient="vertical")
    )
# catalog=["西北", "东北", "西南", "华北", "华南", "华东","华中"]
# # percent=[36232, 47376, 98428, 141487, 145783, 301806, 4327013]
# percent=[36232, 47376, 98428, 145783, 301806, 327013, 141487]
# data_pair=[list(d) for d in zip(catalog, percent)]
# pie.add("类别",data_pair, rosetype="radius",radius=["30%", "75%"])#南丁格尔玫瑰图
#民间写法更方便
data = [
 ['西北', 36232],
 ['东北', 47376],
 ['西南', 98428],
 ['华北', 141487],
 ['华南', 145783],
 ['华东', 301806],
 ['华中', 4327013]
]
pie.add("类别", data, rosetype="radius", radius=["30%", "75%"])
pie.render("/Users/steve/Desktop/项目/实习/Day 8 work/html/七大区域确诊人数_饼图_南丁格尔玫瑰图3.html")
