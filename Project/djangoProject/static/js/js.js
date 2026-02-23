/*   */
$(function () {
    //雷达图
    var data22 = [];
    var data23 = [];
    // 定义第一个 ajax 请求
$.ajax({
    type: "get",
    url: "/user/getkeywords/",
    data: null,
    success: function(msg){
         //定义数组
        for(var i=0; i<6;i++){
            data22.push(msg[i].frequency) ;
        }
        for(var i=6; i<msg.length;i++){
            data23.push(msg[i].frequency) ;
        }
        echarts_1();
    }
});

//动态柱状图
$.ajax({
    url: '/user/get_total/', // Django视图函数的url
    type: 'GET',
    success: function(response) {
        var Data = response;
        echarts_2(Data);
    }
});

//关系花图
$.ajax({
    url: '/user/relationdata/', // Django视图函数的url
    type: 'GET',
    success: function(response) {
        var Data1 = response;
        echarts_4();
    }
});


//折线图
$.ajax({
    url: '/user/Forecastdata/', // Django视图函数的url
    type: 'GET',
    success: function(response) {
        var Data2 = response;
        echarts_3();
    }
});

//echarts_3();
//echarts_4();
echarts_5();


//雷达图
function echarts_1() {
    //左上
        // 基于准备好的dom，初始化echarts实例
        data2022 = [data22]
        data2023 = [data23]
        var myChart = echarts.init(document.getElementById('echart1'));
        const lineStyle = {
          width: 1,
          opacity: 0.5
        };
        option = {
//  backgroundColor: '#f0f0f0',
  title: {
    text: 'Keyword',
    left: 'left',
//    textStyle: {
//      color: '#eee'
//    }
  },
  legend: {
    bottom: 5,
    left: 'right',
    data: ['2022', '2023'],
    itemGap: 20,
    textStyle: {
//      color: '#fff',
      fontSize: 14
    },
    selectedMode: 'single'
  },
  radar: {
    indicator: [
      { name: 'cs.LG', max: 30000 ,color: 'black'},
      { name: 'cs.CV', max: 15000 ,color: 'black'},
      { name: 'cs.AI', max: 15000 ,color: 'black'},
      { name: 'cs.CL', max: 15000 ,color: 'black'},
      { name: 'cs.RO', max: 12000 ,color: 'black'},
      { name: 'eess.SY', max: 10000 ,color: 'black'}
    ],
    shape: 'circle',
    splitNumber: 5,
    axisName: {
      color: 'rgb(238, 197, 102)'
    },
    splitLine: {
      lineStyle: {
        color: [
          'rgba(238, 197, 102, 0.1)',
          'rgba(238, 197, 102, 0.2)',
          'rgba(238, 197, 102, 0.4)',
          'rgba(238, 197, 102, 0.6)',
          'rgba(238, 197, 102, 0.8)',
          'rgba(238, 197, 102, 1)'
        ].reverse()
      }
    },
    splitArea: {
      show: false
    },
    axisLine: {
      lineStyle: {
        color: 'rgba(238, 197, 102, 0.5)'
      }
    }
  },
  series: [
    {
      name: '2022',
      type: 'radar',
      lineStyle: lineStyle,
      data: data2022,
      symbol: 'none',
      itemStyle: {
        color: '#F9713C'
      },
      areaStyle: {
        opacity: 0.1
      }
    },
    {
      name: '2023',
      type: 'radar',
      lineStyle: lineStyle,
      data: data2023,
      symbol: 'none',
      itemStyle: {
        color: '#FD666D'
      },
      areaStyle: {
        opacity: 0.05
      }
    }
  ]
};
      
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

var css = `
#main {
    width: 100%;
    height: 600px;
}
`;



//动态柱状图
function echarts_2(data1) {
        // Based on prepared DOM, initialize echarts instance
        var myChart = echarts.init(document.getElementById('echart2'));
        data = data1
        // Accumulate and sort the data
        function accumulateData(data) {
            var accumulatedData = [];
            var totals = {};

            for (var i = 0; i < data.length; i++) {
                var monthData = JSON.parse(JSON.stringify(data[i])); // deep copy to avoid modifying original data

                for (var j = 0; j < monthData.length; j++) {
                    var name = monthData[j].name;
                    var Paper_Num = monthData[j].value;

                    if (totals[name]) {
                        totals[name] += Paper_Num;
                    } else {
                        totals[name] = Paper_Num;
                    }

                    monthData[j].Paper_Num = totals[name];
                }

                monthData.sort(function (a, b) {
                    return b.Paper_Num - a.Paper_Num;
                });

                accumulatedData.push(monthData);
            }

            return accumulatedData;
        }

        var data = accumulateData(data); // call this after data is defined

        var option = {
            title: {
                text: 'Published in ' + data[0][0].date,
            },
            dataset: {
                dimensions: ['name', 'Paper_Num'],
                source: data[0]
            },
            grid: {containLabel: true},
            xAxis: {type: 'value'}, // Use 'value' for xAxis type
            yAxis: {type: 'category', inverse: true}, // Reverse yAxis
            visualMap: {
                orient: 'horizontal',
                left: 'center',
                min: 0,
                max: 1e5,
                text: ['High Score', 'Low Score'],
                dimension: 1,
                inRange: {
                    color: ['#65B581', '#FFCE34', '#FD666D']
                }
            },
            series: [
                {
                    type: 'bar',
                    encode: {
                        x: 'Paper_Num',
                        y: 'name'
                    }
                }
            ],
            animationDuration: 3000,
            animationDurationUpdate: 3000,
            animationEasing: 'linear',
            animationEasingUpdate: 'linear'
        };

        // Using the specified configuration and data to show the chart.
        myChart.setOption(option);

        var currentIndex = -1;

        setInterval(function () {
            var dataLen = data.length;

            if (dataLen) {
                currentIndex = (currentIndex + 1) % dataLen;

                myChart.setOption({
                    dataset: {
                        source: data[currentIndex],
                    },
                    yAxis: {
                        data: data[currentIndex].map(function (d) {return d.name;}),
                        inverse: true
                    },
                    title: {
                        text: 'Published in ' + data[currentIndex][0].date,
                    },
                });
            }
        }, 3000);
    }



//预测折线图
function echarts_3() {
    var chart1 = echarts.init(document.getElementById('main3'));
    var chart2 = echarts.init(document.getElementById('main4'));
    var processedData = raw_data.map(function (item) {
      return {
        date: item.date,
        category: item.category,
        number: item.number
      };
    });

    var seriesData1 = [];
    var seriesData2 = [];

    // 分组处理数据
    var group1 = ['CS', 'Math'];

    // 处理第一组数据
    group1.forEach(function (category) {
      var groupData = processedData.filter(function (item) {
        return item.category === category;
      });

      if (groupData.length > 0) {
        seriesData1.push({
          type: 'line',
          name: category,
          data: groupData.map(function (item) {
            return [item.date, item.number];
          }),
          smooth: true // 添加平滑曲线
        });
      }
    });

    // 处理第二组数据
    var group2 = processedData.filter(function (item) {
      return !group1.includes(item.category);
    });

    if (group2.length > 0) {
      var categoryColors = {}; // 存储每个类别的颜色

      group2.forEach(function (item) {
        if (!categoryColors[item.category]) {
          categoryColors[item.category] = getRandomColor(); // 生成随机颜色
        }

        if (!seriesData2.some(function (series) {
          return series.name === item.category;
        })) {
          seriesData2.push({
            type: 'line',
            name: item.category,
            data: [],
            lineStyle: {
              color: categoryColors[item.category] // 设置线条颜色
            },
            smooth: true, // 添加平滑曲线
            connectNulls: true // 连接空值点
          });
        }

        seriesData2.forEach(function (series) {
          if (series.name === item.category) {
            series.data.push([item.date, item.number]);
          }
        });
      });
    }

    var option1 = {
      title: {
        text: 'Prediction'
      },
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: group1
      },
      xAxis: {
        type: 'category',
        name: 'Date'
      },
      yAxis: {
        type: 'value',
        name: 'Number'
      },
      series: seriesData1
    };

    var option2 = {
//      title: {
//        text: 'Group 2'
//      },
      tooltip: {
        trigger: 'axis'
      },
//      legend: {
//        data: group2.map(function (item) {
//          return item.category;
//        })
//      },
      xAxis: {
        type: 'category',
        name: 'Date'
      },
      yAxis: {
        type: 'value',
        name: 'Number'
      },
      series: seriesData2
    };

    chart1.setOption(option1);
    chart2.setOption(option2);

    function getRandomColor() {
      var letters = '0123456789ABCDEF';
      var color = '#';
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    }


//关系花
function echarts_4() {
    var myChart = echarts.init(document.getElementById('echart5'));

        // 指定图表的配置项和数据
        // 这个对象包含了图表的配置项和数据
        // 你可以在这个对象中指定图表的类型、标题、提示框等信息，也可以指定图表的数据
        var option = {
            title: {
                text: 'Computer Science Publications',
                subtext: 'From Jan 2022 to Jun 2023',
                top: 'bottom',
                left: 'right'
            },
            tooltip: {},
            legend: [{
                data: graphData.categories.map(function (a) {
                    return a.name;
                })
            }],
            animation: false,
            series : [
    {
        name: 'Publications',
        type: 'graph',
        layout: 'force',
        data: graphData.nodes,
        links: graphData.links,
        categories: graphData.categories,
        roam: true,  // 允许用户移动和缩放图表
        draggable: true,  // 允许拖拽节点
        zoom: 0.3,  // 设置图表的初始缩放级别为80%
        label: {
            position: 'right',
            formatter: '{b}'
        },
        force: {
            repulsion: 100
        }
    }
]

        };

        // 使用刚指定的配置项和数据显示图表
        // 这行代码将option对象传递给ECharts实例，ECharts实例根据option对象的配置和数据生成图表
        myChart.setOption(option);
}



//rose
function echarts_5() {
    var myChart = echarts.init(document.getElementById('echart6'));
    $.ajax({
    url: 'http://127.0.0.1:8000/user/get_chart_data/', // 替换为您的视图URL
    method: 'GET',
    success: function (result) {
    // 构建图表配置
    var option = {
     title: {
    text: 'Keyword Frequency'
      },
    legend: {
    top: 'bottom',
    itemWidth: 5, // 设置图例项的宽度
    itemHeight: 5, // 设置图例项的高度
    textStyle: {
//    color: '#fff', // 设置图例文字颜色为白色
    fontSize: 10
    }
    },
//    toolbox: {
//    show: true,
//    feature: {
//    mark: {show: true},
//    dataView: {show: true, readOnly: false},
//    restore: {show: true},
//    saveAsImage: {show: true}
//    }
//    },
    series: [
    {
    name: 'Nightingale Chart',
    type: 'pie',
    radius: [50, 150],
    center: ['50%', '50%'],
    roseType: 'area',
    itemStyle: {
    borderRadius: 8
    },
    labelLine: { // 添加这个属性
                            show: false
                 },
    label:{
    show:false
    },

    data: [] // 在这里传入循环取出的数据
    }
    ]
    };

    // 循环取出result的word和frequency，并添加到data数组中
    result.forEach(function (item) {
    option.series[0].data.push({
    value: item.frequency,
    name: item.word
    });
    });

    myChart.setOption(option);
    window.addEventListener("resize", function () {
    myChart.resize();
    });


    }
    })

    }


})



		
		
		


		









