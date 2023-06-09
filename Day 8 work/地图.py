#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 15:05
"""
from pyecharts import options as opts
from pyecharts.charts import Map
provinces=['湖北','广东','河南','浙江','湖南','安徽','江西','山东','江苏',
          '重庆','四川','北京','黑龙江','上海','福建','河北','香港','广西',
          '陕西','云南','海南','贵州','天津','山西','辽宁','台湾','甘肃',
          '吉林','内蒙古','新疆','宁夏','澳门','青海','西藏']
nums=[4169676,96206,86965,86054,70372,67140,63565,48626,42882,39773,
      36575,32154,32132,27081,21559,21084,19425,17333,17073,12336,
      11504,9670,9632,9333,8924,8464,7904,6320,5719,5006,4949,1315,
      1300,74]
map_chaina = (
    Map()
    # 双引号之间一定要有个空格
    .add("省份", [list(z) for z in zip(provinces, nums)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各省确诊人数",subtitle="数据来源于网络"),
        # 将4169676中的4删掉会看到颜色差别--差量级很难显示，is_piecewise：左下角的数量
        visualmap_opts=opts.VisualMapOpts(max_=169676, is_piecewise=False),
    )
    .render("/Users/steve/Desktop/项目/实习/Day 8 work/html/全国各省确诊人数_地图2.html")
)


