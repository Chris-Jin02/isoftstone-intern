# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/8 14:38
# 文件名：pie.py

import pyecharts.charts as charts
from pyecharts import options as opts
pie = charts.Pie(init_opts=opts.InitOpts(width="600px", height="400px"))
pie.set_global_opts(
 title_opts={"text": "七大区域确诊人数", "subtext":"数据来源于网络"},
 # 添加为纵向的类别----默认横向
 legend_opts=opts.LegendOpts(type_="scroll", pos_top="20%", pos_left="left",
 orient="vertical")
 )
# catalog=["西北", "东北", "西南", "华北", "华南", "华东","华中"]
# percent=[36232, 47376, 98428, 141487, 145783, 301806, 4327013]
catalog = ["西北", "东北", "西南", "华南", "华东", "华中", "华北"]
# 4327013 删一位数字，纯粹为了图好看（相差量级）
percent = [36232, 47376, 98428, 145783, 301806, 327013, 141487]
data_pair = [list(d) for d in zip(catalog, percent)]
# pie.add("类别",data_pair)#普通会动的饼图
# radius--可选参数 --环形的里外半径
# rosetype="radius"和"area"
# radius：扇区圆心角展现数据的百分比，半径展现数据的大小
# area：所有扇区圆心角相同，仅通过半径展现数据大小
# 南丁格尔玫瑰图
pie.add("类别", data_pair, rosetype="radius", radius=["30%", "75%"])
# 民间写法更方便
# data = [
# ['西北', 36232],
# ['东北', 47376],
# ['西南', 98428],
# ['华北', 141487],
# ['华南', 145783],
# ['华东', 301806],
# ['华中', 4327013]
# ]
# pie.add("类别",data, rosetype="radius",radius=["30%", "75%"])#南丁格尔玫瑰图
#=================================================================
pie.render("D:\python work\day7\html\七大区域确诊人数_饼图_南丁格尔玫瑰图.html")