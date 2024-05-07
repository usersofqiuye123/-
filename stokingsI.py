import requests
import csv



#打开一个文件并命名
file = open('data.csv', mode='a', encoding='utf-8', newline='')
#使用DictWriter方法以字典形式写入
csv_write = csv.DictWriter(file, fieldnames=['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今', '成交量', '成交额', '换手率', '市盈率(TTM)',
                                             '股息率', '市值'])

csv_write.writeheader()   #写入一次表头数据


#原本网页一页最多只能显示90支股票数据，通过查看 结合页数计算 一共有4432支股票数据  修改url中的size 以达到获取全部股票数据
url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=4432&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1623304455997'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}#遭遇反爬 加请求参数
# 发送网络请求
response = requests.get(url=url, headers=headers)
json_data = response.json()

# 数据筛选
data_list = json_data['data']['list']
for data in data_list:      #建立for循环 把列表数据遍历出来
    # print(data) #解析数据
    #设置data取键值对
    data1 = data['symbol']
    data2 = data['name']
    data3 = data['current']
    data4 = data['chg']
    if data4:
        if float(data4) > 0:
            data4 = '+' + str(data4)
        else:
            data4 = str(data4)
    data5 = str(data['percent']) + '%'
    data6 = str(data['current_year_percent']) + '%'
    data7 = data['volume']
    data8 = data['amount']
    data9 = str(data['turnover_rate'])+'%'
    data10 = data['pe_ttm']
    data11 =data['dividend_yield']
    if data11:
        data11 = str(data['dividend_yield'])+'%'
    else:
        data11 = None
    data12 = data['market_capital']
    print(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12,)

    #数据保存
    data_dict = {'股票代码': data1, '股票名称': data2, '当前价': data3, '涨跌额': data4, '涨跌幅': data5, '年初至今': data6,
                 '成交量': data7, '成交额':data8, '换手率': data9, '市盈率(TTM)': data10, '股息率': data11, '市值': data12, }
    csv_write.writerow(data_dict)



import pandas as pd
import numpy as np
#加载csv数据
data_df = pd.read_csv('data1.csv')
#显示头文件
data_df.head()
#判断数据行中书是否存在缺失值
data_df.isnull().any(axis=1)
#将缺失值都补为0
data_df = data_df.fillna(0)
#再次查看数据行中书是否修改成功
data_df.isnull().any(axis=1)
#再次查看数据行
data_df.head()
#统计每一列空值的个数：
data_df.isnull().any().sum()
#让值从大到小进行排序
df = data_df.sort_values(by='成交量',ascending=False)
data_df.head(10)
#保存处理后的数据
import pandas as pd
df = df.set_index('股票名称')
df.to_csv("data1.csv",encoding='utf-8')
data_df = pd.read_csv("data1.csv")

from pyecharts import options as opts

#读取处理后的数据
data_df = pd.read_csv('data1.csv')
df = data_df.dropna()
df1 = df[['股票名称', '成交量']]
data_df.sort_values(by='成交量',ascending=False)
#取前10条股票
df2 = df1.iloc[:10]
#打印出来显示检查结果是否正确
print(df2['股票名称'].values)
print(df2['成交量'].values)

from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
#设置风格
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
#x轴数据
bar.add_xaxis(list(df2['股票名称'].values))
#x轴数据
bar.add_yaxis("股票成交量情况",list(df2['成交量'].values))
#设置标签配置项
bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))
#设置标题
bar.set_global_opts(title_opts=opts.TitleOpts(title="成交量图表"))
#直接在notebook显示图表
bar.render_notebook()

from pyecharts.globals import CurrentConfig, NotebookType
# 配置对应的环境类型
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
CurrentConfig.ONLINE_HOST='https://assets.pyecharts.org/assets/'
from pyecharts import options as opts
from pyecharts.charts import Bar

#读取表
data_df = pd.read_csv('data1.csv')
df = data_df.dropna()
df1 = df[['股票名称', '成交额']]
data_df.sort_values(by='成交额',ascending=False)
df2 = df1.iloc[:10]
print(df2['股票名称'].values)
print(df2['成交额'].values)
#设置风格
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
#x轴数据
bar.add_xaxis(list(df2['股票名称'].values))
#y轴数据
bar.add_yaxis("股票成交额情况",list(df2['成交额'].values))
#设置标签配置项
bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))
#设置标题
bar.set_global_opts(title_opts=opts.TitleOpts(title="成交额图表"))
#直接在notebook显示图表
bar.render_notebook()

from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
from pyecharts.globals import ThemeType
#读取表
data_df = pd.read_csv('data1.csv')
df = data_df.dropna()
df1 = df[['股票名称', '市值']]
data_df.sort_values(by='市值',ascending=False)
df2 = df1.iloc[:10]
#打印出股票名称与市值 查看数据是否正确
print(df2['股票名称'].values)
print(df2['市值'].values)

#设置风格
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
#导入Y轴数据
y_data = [212966200430,9248273205,107335530969,73391902563,949878874875,317276616395,281115930557,12651913335,92773567583,12646728429]
#x轴数据，导入数据
bar.add_xaxis(list(df2['股票名称'].values))
#y轴数据，导入数据
bar.add_yaxis("股票市值情况",y_data)
#设置数字显示位置
bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
#设置标题
bar.set_global_opts(title_opts=opts.TitleOpts(title="市值图表"))
bar.reversal_axis()#翻转xy轴
#直接在notebook显示图表
bar.render_notebook()

import pyecharts.options as opts
from pyecharts.charts import Line



#查看数据得知涨跌幅情况，设置Y轴参数
y_data = [3.03,10.15,2,0,5.7,3.4,-0.63,2.31,6.03,3.39]

line=(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="单位(%)", pos_left="left"),
    )
    .add_xaxis(list(df2['股票名称'].values))
    .add_yaxis(
        series_name="涨跌幅折线图",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),

    )
)
line.render_notebook()


import pyecharts.options as opts
from pyecharts.charts import Line


df = data_df.dropna()
df1 = df[['股票名称', '年初至今']]
data_df.sort_values(by='年初至今',ascending=False)
#取前10条股票
df2 = df1.iloc[:10]
#打印出股票名称与年初至今查看数据
print(df2['股票名称'].values)
print(df2['年初至今'].values)
#查看数据得知各股票年初至今的涨幅情况，设置Y轴参数
y_data = [3.65,104.72,9.55,37.61,25.06,111.96,18.41,-2.21,50.14,89.51]

line=(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        #设置单位标题，并且显示在左上方
        title_opts=opts.TitleOpts(title="单位(%)", pos_left="left"),
    )
        #设置x轴
    .add_xaxis(list(df2['股票名称'].values))
    #设置y轴
    .add_yaxis(
        #标题名称
        series_name="年初至今涨幅情况折线图",
        #赋值数据
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),

    )
)
line.render_notebook()

 

from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
from pyecharts.globals import ThemeType
#读取表
data_df = pd.read_csv('data1.csv')
df = data_df.dropna()
df1 = df[['股票名称', '当前价']]
data_df.sort_values(by='当前价',ascending=False)
df2 = df1.iloc[:10]
#打印出股票名称与市值 查看数据是否正确
print(df2['股票名称'].values)
print(df2['当前价'].values)
#设置data_x数据
data_x = ["京东方A", "中银绒业", "TCL科技",]
#设置data_y数据
data_y = [6.12, 2.17, 7.65,1.61,5.19,25.88, 11, 2.21, 5.45, 8.85]
inner_data_pair = [list(z)for z in zip(data_x, data_y)]

outer_data_x = ["包钢股份","中国石油","中远海控","紫金矿业","二三四五","中国铝业","数码视讯"]
outer_data_y = [1.61, 5.19, 25.88, 11, 2.21, 5.45, 8.85]
outer_data_pair = [list(z) for z in zip(outer_data_x, outer_data_y)]

c = (
        Pie(init_opts=opts.InitOpts(width="1200px", height="800px"))
#设置内圈数据
    .add(
                series_name="当前价",
                data_pair= inner_data_pair,
                radius=[0, "30%"],
                label_opts=opts.LabelOpts(position="inner"),
        )
#设置外圈数据
        .add(
                series_name="当前价",
                radius=["40%","55%"],
                data_pair=outer_data_pair,
                label_opts=opts.LabelOpts(
                            position="outside",
                            formatter="{a|{a}}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}   ",
                            background_color="#eee",
                            border_color="#aaa",
                            border_width=1,
                            border_radius=4,

                            rich={
                                "a": {"color": "#999", "LineHeight": 22, "align": "center" },
                                "abg": {
                                                "backgroundColor": "#e3e3e3",
                                                "width": "100%",
                                                "align": "right",
                                                "height": 22,
                                                "borderRadius": [4, 4, 0, 0]
                                },
                                "hr": {
                                                "borderColor": "#aaa",
                                                "width" :"100%",
                                                "borderWidth": 0.5,
                                                "height": 0,
                                },
                                "b": {"fontSize": 16,"LineHeight": 33},
                                "per": {
                                                "color": "#eee",
                                                "backgroundColor": "#334455",
                                                "padding": [2, 4],
                                                "borderRadius": 2,
                                             },
                            },
                ),
        )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical",))
    .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)",

            )

        ).set_global_opts(title_opts=opts.TitleOpts(title='当前价位饼图', subtitle='元/股'))
        )
pie=Pie()
c.render_notebook()
