'''
    DataSource：https://news.sina.cn/
    Created on：2020-02-15
    Author：hanxianzhe1116
    Email：2019221839@nwnu.edu.cn
    Remarks：The overall data can be obtained basically, but the daily changes of each city have not been obtained yet.
             I will update it later.
'''
import requests
import re
import json
import pandas as pd
'''
    获取url页面信息
'''
def get_page(url):
    try:
        response = requests.get(url)
        # print(response.status_code)
        if response.content:  # 返回成功
            # print(response.content)
            return response
    except requests.ConnectionError as e:
        print('url出错', e.args)
'''
    获取页面json文件
'''
def get_detail(page):
    # print(page.text)
    text = re.compile(r'[(](.*?)[)]', re.S)
    transformData = json.loads(re.findall(text, page.text)[0])
    # print(type(transformData))
    return transformData
'''
    获取国内历史信息
    parameter:  historylist , historylist_type = list
                list in historylist , list_type = dict
                    keys:日期：date
                         国内确诊总数：cn_conNum
                         国内死亡总数：cn_deathNum
                         国内治愈总数：cn_cureNum
                         国内疑似总数：cn_susNum
                         国内死亡率：cn_deathRate
                         国内治愈率：cn_cureRate
                         无用：is_show
                         疑似较昨日增加：wjw_susNum
                         武汉确诊总数：wuhan_conNum
                         武汉死亡总数：wuhan_deathNum
                         武汉治愈总数：wuhan_cureNum
                         武汉疑似总数：wuhan_susNum
'''
def get_historylist_data(historylist, day):
    # 获取historylist中字典的key值
    # for key in historylist[0].keys():
    #     print(key)
    data_of_date = pd.DataFrame(historylist)
    data_of_date.to_csv(day + '/historylist.csv')
    print('write the info to historylist.csv over!')
    # print(data_of_date)
'''
    获取全国各省市当前（包括过往）数据
    parameter：list, list_type = list
                l in list , l_type = dict
                    keys：name：省（直辖市）名称（中文）
                          ename：省（直辖市）名称（英文）
                          value：确诊总人数（包括过往）
                          susNum：疑似（数据有点问题，好多都是0）
                          deathNum：死亡总人数（包括过往）
                          cureNum：治愈总人数（包括过往）
                          city：省（直辖市）下属市（区）情况
                                这是个列表，里面是字典
                                name: "武汉"
                                conNum: "37914"
                                susNum: "0"
                                cureNum: "2519"
                                deathNum: "1123"
                                mapName: "武汉市"
'''
def get_list_data(list, day):
    # print(type(list))
    city_list = []
    provence_name = []
    for l in list:
        city_list.append(l['city'])  # 获取市（区）级情况
        provence_name.append(l['name'])  # 存储省份名称
        l.pop('city')  # 列表中的字典里嵌套的列表，不能写入csv，因此做pop()操作，上面已经存储了相应信息
    # print(list)
    # print(city_list)
    # print(len(provence_name))
    # 将省份对应的市的情况（包括过往）写入csv
    # print(provence_name)
    for i in range(0, len(provence_name)):
        data_of_city = pd.DataFrame(city_list[i])
        data_of_city.to_csv(day + '/' + str(i) + '_' + provence_name[i] + '.csv')
    print('write the info to i_ProvenceName.csv over!')
    # 将各省（直辖市）当天总体情况（包括过往）写入csv
    data_of_provence = pd.DataFrame(list)
    data_of_provence.to_csv(day + '/list.csv')
    print('write to list.csv over!')
'''
    获取全世界各国家总体情况
'''
def get_worldlist_data(worldlist, day):
    data_of_worldlist = pd.DataFrame(worldlist)
    data_of_worldlist.to_csv(day + '/worldlist.csv')
    print('write to worldlist.csv over!')
if __name__ == '__main__':
    url = 'https://gwpre.sina.cn/interface/fymap2020_data.json?random=0.655044413123367&_=1581749886687&callback=blankCallBack'
    page = get_page(url)
    data = get_detail(page)['data']
    # ---------------------------------------------
    day = '2020-02-16'
    # 获取国内历史信息
    get_historylist_data(data['historylist'], day)
    # 获取全国各省市当前（包括）数据
    get_list_data(data['list'], day)
    # 获取全世界各国家总体情况
    get_worldlist_data(data['worldlist'], day)









