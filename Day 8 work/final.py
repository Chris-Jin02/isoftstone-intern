#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/8 15:36
"""
from pyecharts.charts import Page
page = Page(layout= Page.DraggablePageLayout, page_title= "全国新冠数据展示大屏")
page.save_resize_html( '/Users/steve/Desktop/项目/实习/Day 8 work/html/全国新冠数据展示大屏.html', cfg_file= '/Users/steve/Desktop/项目/实习/Day 8 work/html/chart_config.json', dest= '/Users/steve/Desktop/项目/实习/Day 8 work/html/全国新冠数据展示大屏_final.html')
