import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'size': 14}
font2 = {'size': 14}
today = '2020-02-18'

def progress_historylist_date(date):
    date_to_str = ['0' + str(i) for i in date]
    for x in range(0, len(date_to_str)):
        if len(date_to_str[x]) == 4:
            date_to_str[x] += '0'
    # print(date_to_str)
    date_to_str = [i.replace('.', '-') for i in date_to_str]
    # print(date_to_str)
    return date_to_str


def import_historylist_data(today):
    historylist_data = pd.read_csv(today + '/historylist.csv')
    # print(historylist_data)
    date = historylist_data['date']
    date = list(reversed(date))
    date = progress_historylist_date(date)
    # print(date)
    # 确诊人数
    cn_conNum = historylist_data['cn_conNum']
    cn_conNum = list(reversed(cn_conNum))
    # 治愈人数
    cn_cureNum = historylist_data['cn_cureNum']
    cn_cureNum = list(reversed(cn_cureNum))
    # 死亡人数
    cn_deathNum = historylist_data['cn_deathNum']
    cn_deathNum = list(reversed(cn_deathNum))
    # 疑似人数
    cn_susNum = historylist_data['cn_susNum']
    cn_susNum = list(reversed(cn_susNum))
    # 治愈率
    cn_cureRate = historylist_data['cn_cureRate']
    cn_cureRate = list(reversed(cn_cureRate))
    # 死亡率
    cn_deathRate = historylist_data['cn_deathRate']
    cn_deathRate = list(reversed(cn_deathRate))
    # 确诊人数
    wuhan_conNum = historylist_data['wuhan_conNum']
    wuhan_conNum = list(reversed(wuhan_conNum))
    # 治愈人数
    wuhan_cureNum = historylist_data['wuhan_cureNum']
    wuhan_cureNum = list(reversed(wuhan_cureNum))
    # 死亡人数
    wuhan_deathNum = historylist_data['wuhan_deathNum']
    wuhan_deathNum = list(reversed(wuhan_deathNum))
    return date, cn_conNum, cn_cureNum, cn_deathNum, cn_susNum, cn_cureRate, cn_deathRate, wuhan_conNum, wuhan_cureNum, wuhan_deathNum


def show_historylist_rate_pic(date, cn_cureRate, cn_deathRate):
    plt.figure(figsize=(15, 9))
    plt.xticks(rotation=45)
    plt.xlabel('日期', font1)
    plt.ylabel('比例（%）', font1)
    plt.title('2019-nCoV 治愈率-死亡率变化图', font1)
    cn_cureRate_line, = plt.plot(date, cn_cureRate, 'r-o')
    # print(date, cn_cureRate)
    for a, b in zip(date, cn_cureRate):
        plt.text(a, b, b, ha='center', va='bottom')
    cn_deathRate_line, = plt.plot(date, cn_deathRate, 'k-x')
    # for a, b in zip(date, cn_deathRate):
    #     plt.text(a, b, b, ha='center', va='bottom')
    plt.legend(handles=[cn_cureRate_line, cn_deathRate_line],
               labels=["治愈率", "死亡率"], loc="upper left", fontsize=15)
    plt.savefig("img_" + today + "/historylist_rate.jpg")
    plt.show()


def show_historylist_pic(today):
    date, cn_conNum, cn_cureNum, cn_deathNum, cn_susNum, cn_cureRate, cn_deathRate, wuhan_conNum, wuhan_cureNum, wuhan_deathNum = import_historylist_data(today)
    # plt.figure(figsize=(1000, 700))
    plt.figure(figsize=(15, 9))
    # plt.figure()
    plt.xticks(rotation=45)
    plt.xlabel('日期', font1)
    plt.ylabel('人数', font1)
    plt.title('2019-nCoV 情况变化图', font1)
    # plt.ylim((-1000, 70000))
    # 确诊
    cn_conNum_line, = plt.plot(date, cn_conNum, 'r-o')
    # print(date, cn_conNum)
    for a, b in zip(date, cn_conNum):
        plt.text(a, b, b, ha='center', va='bottom')
    # 治愈
    cn_cureNum_line, = plt.plot(date, cn_cureNum, 'c-*')
    # for a, b in zip(date, cn_cureNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    # 死亡
    cn_deathNum_line, = plt.plot(date, cn_deathNum, 'k--')
    # for a, b in zip(date, cn_deathNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    # 疑似
    cn_susNum_line, = plt.plot(date, cn_susNum, 'g-x')
    # for a, b in zip(date, cn_susNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    # 图例
    plt.legend(handles=[cn_conNum_line, cn_cureNum_line, cn_deathNum_line, cn_susNum_line], labels=["确诊", "治愈", "死亡", "疑似"], loc="upper left", fontsize=15)
    plt.savefig("img_" + today + "/historylist.jpg")
    plt.show()
    show_historylist_rate_pic(date, cn_cureRate, cn_deathRate)


def show_provence_data(today):
    provence_name = ['北京', '湖北', '广东', '浙江', '河南', '湖南', '重庆', '安徽', '四川', '山东', '吉林', '福建', '江西', '江苏', '上海', '广西', '海南', '陕西', '河北', '黑龙江', '辽宁', '云南', '天津', '山西', '甘肃', '内蒙古', '台湾', '澳门', '香港', '贵州', '西藏', '青海', '新疆', '宁夏']
    provence_data = []
    conSum = []
    cureSum = []
    deathSum = []
    for i in range(0, 34):
        try:
            provence_data.append(pd.read_csv(today + '/' + str(i) + '_' + provence_name[i] + '.csv'))
            # if provence_data[i] is None:
            #     continue
            name = provence_data[i]['name']
            # print(name)
            conNum = provence_data[i]['conNum']
            cureNum = provence_data[i]['cureNum']
            deathNum = provence_data[i]['deathNum']
            show_each_provence_pic(provence_name[i], name, conNum, cureNum, deathNum)
            conSum.append(conNum.sum())
            cureSum.append(cureNum.sum())
            deathSum.append(deathNum.sum())
        except Exception:
            conSum.append(0)
            cureSum.append(0)
            deathSum.append(0)
            print("data is none")
    show_cn_provence_bar_pic(provence_name, conSum, cureSum, deathSum)


def show_each_provence_pic(provence_name, name, conNum, cureNum, deathNum):
    # plt.figure(figsize=(1000, 700))
    plt.figure(figsize=(15, 9))
    city_name = name
    # 确诊
    conNum_left = range(len(city_name))
    conNum_height = conNum
    conNum_bar = plt.bar(x=conNum_left, height=conNum_height, width=0.3, alpha=1, color='red', label="确诊")
    # 治愈
    cureNum_left = range(len(city_name))
    cureNum_height = cureNum
    cureNum_bar = plt.bar(x=[i + 0.3 for i in cureNum_left], height=cureNum_height, width=0.3, alpha=1, color='green', label="治愈")
    # 死亡
    deathNum_left = range(len(city_name))
    deathNum_height = deathNum
    deathNum_bar = plt.bar(x=[i + 0.6 for i in deathNum_left], height=deathNum_height, width=0.3, alpha=1, color='black', label="死亡")

    plt.xlabel("市（区）")
    plt.ylabel("数量")
    plt.title(provence_name + "省（市） 确诊-治愈-死亡 情况")
    plt.xticks([index + 0.3 for index in conNum_left], city_name)
    plt.legend(loc="upper right", fontsize=15)
    for rect in conNum_bar:
        height = rect.get_height()
        # print(height)
        # print(rect.get_x())
        # print(rect.get_width())
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in cureNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in deathNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    plt.savefig("img_" + today + "/" + provence_name + ".jpg")
    plt.show()


def show_hubei_bar_pic(provence_name, conSum, cureSum, deathSum):
    conNum_left = 1
    conNum_height = conSum
    conNum_bar = plt.bar(x=conNum_left, height=conNum_height, width=0.3, alpha=1, color='red', label="确诊")
    # 治愈
    cureNum_left = 1
    cureNum_height = cureSum
    cureNum_bar = plt.bar(x=1.3, height=cureNum_height, width=0.3, alpha=1, color='green',
                          label="治愈")
    # 死亡
    deathNum_left = 1
    deathNum_height = deathSum
    deathNum_bar = plt.bar(x=1.6, height=deathNum_height, width=0.3, alpha=1,
                           color='black', label="死亡")

    # plt.xlabel("市（区）")
    plt.ylabel("数量")
    # plt.title(provence_name + "省（市） 确诊-治愈-死亡 情况")
    plt.title("湖北省 确诊-治愈-死亡 情况")
    # plt.xticks(provence_name)
    plt.legend(loc="upper right", fontsize=15)
    for rect in conNum_bar:
        height = rect.get_height()
        # print(height)
        # print(rect.get_x())
        # print(rect.get_width())
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in cureNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in deathNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    plt.savefig("img_" + today + "/hubei.jpg")
    plt.show()


def show_cn_provence_bar_pic(provence_name, conSum, cureSum, deathSum):
    hubei = provence_name[1]
    hubei_conSum = conSum[1]
    hubei_cureSum = cureSum[1]
    hubei_deathSum = deathSum[1]
    show_hubei_bar_pic(hubei, hubei_conSum, hubei_cureSum, hubei_deathSum)
    plt.figure(figsize=(15, 9))
    provence_name.pop(1)
    conSum.pop(1)
    cureSum.pop(1)
    deathSum.pop(1)
    conNum_left = range(len(conSum))
    conNum_height = conSum
    conNum_bar = plt.bar(x=conNum_left, height=conNum_height, width=0.3, alpha=1, color='red', label="确诊")
    # 治愈
    cureNum_left = range(len(conSum))
    cureNum_height = cureSum
    cureNum_bar = plt.bar(x=[i + 0.3 for i in cureNum_left], height=cureNum_height, width=0.3, alpha=1, color='green',
                          label="治愈")
    # 死亡
    deathNum_left = range(len(conSum))
    deathNum_height = deathSum
    deathNum_bar = plt.bar(x=[i + 0.6 for i in deathNum_left], height=deathNum_height, width=0.3, alpha=1,
                           color='black', label="死亡")

    plt.xlabel("市（区）")
    plt.ylabel("数量")
    # plt.title(provence_name + "省（市） 确诊-治愈-死亡 情况")
    plt.title("全国 确诊-治愈-死亡 情况")
    plt.xticks([index + 0.3 for index in conNum_left], provence_name)
    plt.legend(loc="upper right", fontsize=15)
    for rect in conNum_bar:
        height = rect.get_height()
        # print(height)
        # print(rect.get_x())
        # print(rect.get_width())
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in cureNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in deathNum_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    plt.savefig("img_" + today + "/cn.jpg")
    plt.show()


def show_cn_provence_pic(provence_name, conSum, cureSum, deathSum):
    # print(conSum)
    # print(type(conSum[0]))
    label_list = provence_name  # 各部分标签
    # size = [55, 35, 10]  # 各部分大小
    # color = ["red", "green", "blue"]  # 各部分颜色
    explode = [0.4, 0.1, 0.5, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]  # 各部分突出值
    """
    绘制饼图
    explode：设置各部分突出
    label:设置各部分标签
    labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
    autopct：设置圆里面文本
    shadow：设置是否有阴影
    startangle：起始角度，默认从0开始逆时针转
    pctdistance：设置圆内文本距圆心距离
    返回值
    l_text：圆内部文本，matplotlib.text.Text object
    p_text：圆外部文本
    """
    # patches, l_text, p_text = autopct="%.1f%%", labels=label_list,
    plt.pie(conSum, explode=explode, autopct="%.1f%%", labels=label_list, labeldistance=1.1, shadow=False, startangle=-180, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.legend(labels=label_list)

    plt.show()


def show_cn_expect_wuhan_pic(today):
    date, cn_conNum, cn_cureNum, cn_deathNum, cn_susNum, cn_cureRate, cn_deathRate, wuhan_conNum, wuhan_cureNum, wuhan_deathNum = import_historylist_data(today)
    plt.figure(figsize=(15, 9))
    # plt.figure()
    plt.xticks(rotation=45)
    plt.xlabel('日期', font1)
    plt.ylabel('人数', font1)
    plt.title('2019-nCoV 情况变化图', font1)
    # plt.ylim((-1000, 70000))
    expect_wuhan_conNum = [cn_conNum[i] - wuhan_conNum[i] for i in range(len(cn_conNum))]
    expect_wuhan_cureNum = [cn_cureNum[i] - wuhan_cureNum[i] for i in range(len(cn_cureNum))]
    expect_wuhan_deathNum = [cn_deathNum[i] - wuhan_deathNum[i] for i in range(len(cn_deathNum))]
    # print(expect_wuhan_conNum)
    # print(expect_wuhan_cureNum)
    # print(expect_wuhan_deathNum)

    # 确诊
    expect_wuhan_conNum_line, = plt.plot(date, expect_wuhan_conNum, 'r-o')
    # print(date, cn_conNum)
    for a, b in zip(date, expect_wuhan_conNum):
        plt.text(a, b, b, ha='center', va='bottom')
    # 治愈
    expect_wuhan_cureNum_line, = plt.plot(date, expect_wuhan_cureNum, 'c-*')
    # for a, b in zip(date, cn_cureNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    # 死亡
    expect_wuhan_deathNum_line, = plt.plot(date, expect_wuhan_deathNum, 'k--')
    # for a, b in zip(date, cn_deathNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    # 图例
    plt.legend(handles=[expect_wuhan_conNum_line, expect_wuhan_cureNum_line, expect_wuhan_deathNum_line],
               labels=["确诊", "治愈", "死亡"], loc="upper left", fontsize=15)
    plt.savefig("img_" + today + "/cn_expect_wuhan.jpg")
    plt.show()

if __name__ == '__main__':
    show_historylist_pic(today)
    show_provence_data(today)
    show_cn_expect_wuhan_pic(today)