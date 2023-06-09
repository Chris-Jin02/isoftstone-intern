#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 15:22
"""
from pyecharts.charts import Bar
from pyecharts.charts import Funnel
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import  pyecharts.charts as charts
from pyecharts.charts import Map
from pyecharts.charts import Page

# 1、柱状图
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

# 2、漏斗图
x_data = [ '西藏自治区','青海省','澳门特别行政区','宁夏回族自治区','新疆维吾尔自治区','内蒙古自治区','吉林省','甘肃省','台湾省','辽宁省']
y_data =[ 74,1300,1315,4949,5006,5719,6320,7904,8464,8924]
data = [[x_data[i], y_data[i]] for i in range(len(x_data))]
funnel=(
    Funnel()
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts())
)

# 3、地图
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
)
# 4、饼图
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
# 5、词云图
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
)

# 大屏展示
page = Page(layout= Page.DraggablePageLayout, page_title= "全国新冠数据展示大屏")
page.add(bar,pie,funnel,wordCloud,map_chaina)
page.render("/Users/steve/Desktop/项目/实习/Day 8 work/html/全国新冠数据展示大屏.html")
