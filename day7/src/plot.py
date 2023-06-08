# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/8 10:14
# 文件名：plot.py

from pyecharts.charts import Bar
from pyecharts import options as opts
bar = Bar(init_opts=opts.InitOpts(width="600px", height="400px"))
# 标题设置为中间
bar.set_global_opts(title_opts=opts.TitleOpts(title="确诊人数最少的 10 个省份", subtitle="数据来源于网络"))
xdata = ['西藏自治区', '青海省', '澳门特别行政区', '宁夏回族自治区', '新疆维吾尔自治区', '内蒙古自治区', '吉林省', '甘肃省', '台湾省', '辽宁省']
ydata = [74, 1300, 1315, 4949, 5006, 5719, 6320, 7904, 8464, 8924]
bar.add_xaxis(xdata)
bar.add_yaxis('省份', ydata)
bar.reversal_axis()
bar.render("D:\python work\day7\html\确诊人数最少的 10 个省份_横向柱状图.html")