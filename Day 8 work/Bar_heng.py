#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 11:09
"""
from pyecharts.charts import Bar
from pyecharts import options as opts
bar=Bar( init_opts=opts.InitOpts(width="600px", height="400px"))#图大小
#标题设置
bar.set_global_opts(
      title_opts=opts.TitleOpts(
        title="确诊人数最多的10个省份",subtitle="数据来源于网络",
        # pos_left="center"   #设置标题为中间
        ))
xdata=[ '西藏自治区','青海省','澳门特别行政区','宁夏回族自治区','新疆维吾尔自治区','内蒙古自治区','吉林省','甘肃省','台湾省','辽宁省']
ydata=[ 74,1300,1315,4949,5006,5719,6320,7904,8464,8924]
xdata=list(reversed(xdata)) #反转--达到降序的目的
ydata=list(reversed(ydata))
bar.add_xaxis(xdata)
bar.add_yaxis('省份', ydata)
bar.reversal_axis()#X，Y轴互换
bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))#数字在右边
bar.render("/Users/steve/Desktop/项目/实习/Day 8 work/html/确诊人数最少的10个省份_横向柱状图.html")

