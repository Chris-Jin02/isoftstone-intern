#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 15:15
"""
from pyecharts.charts import Funnel
from pyecharts import options as opts

x_data = [ '西藏自治区','青海省','澳门特别行政区','宁夏回族自治区','新疆维吾尔自治区','内蒙古自治区','吉林省','甘肃省','台湾省','辽宁省']
y_data =[ 74,1300,1315,4949,5006,5719,6320,7904,8464,8924]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel()
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="纯属虚构"))
    .render("/Users/steve/Desktop/项目/实习/Day 8 work/html/确诊人数最少的10个省份_漏斗图.html")
)