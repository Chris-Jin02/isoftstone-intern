# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/8 15:11
# 文件名：map.py

from pyecharts import options as opts
from pyecharts.charts import Map
provinces = ['湖北省','广东省','河南省','浙江省','湖南省','安徽省','江西省','山东省','江苏省',
'重庆省','四川省','北京市','黑龙江省','上海市','福建省','河北省','香港省','广西省',
'陕西省','云南省','海南省','贵州省','天津省','山西省','辽宁省','台湾省','甘肃省',
'吉林省','内蒙古省','新疆省','宁夏省','澳门省','青海省','西藏省']

nums = [169676,96206,86965,86054,70372,67140,63565,48626,42882,39773,
36575,32154,32132,27081,21559,21084,19425,17333,17073,12336,
11504,9670,9632,9333,8924,8464,7904,6320,5719,5006,4949,1315,
1300,74]

map_chaina = (
   Map()
   .add("省份", [list(z) for z in zip(provinces, nums)], "china")
   .set_global_opts(
       title_opts=opts.TitleOpts(title="全国各省确诊人数",subtitle="数据来源于网络"),
       visualmap_opts=opts.VisualMapOpts(max_=169676, is_piecewise=False),
   )
   .render("../html/全国各省确诊人数_地图.html")
)