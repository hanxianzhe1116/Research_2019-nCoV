import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'size': 14}


def progress_date(date):
    date_to_str = ['0' + str(i) for i in date]
    for x in range(0, len(date_to_str)):
        if len(date_to_str[x]) == 4:
            date_to_str[x] += '0'
    # print(date_to_str)
    date_to_str = [i.replace('.', '-') for i in date_to_str]
    # print(date_to_str)
    return date_to_str


def import_data(day):
    data = pd.read_csv(day + '/historylist.csv')
    # print(historylist_data)
    date = data['date']
    date = list(reversed(date))
    date = progress_date(date)
    # 确诊人数
    wuhan_conNum = data['wuhan_conNum']
    wuhan_conNum = list(reversed(wuhan_conNum))
    return date, wuhan_conNum


def logistic(t, K, P0, r):  # logistic函数
    # print("t=", type(t))
    # print("K=", type(K))
    # print("P0=", type(P0))
    # print("r=", type(r))
    exp_value = np.exp(r * (t))
    return (K*exp_value*P0)/(K+(exp_value-1)*P0)


def prediction_data(day):
    plt.figure(figsize=(15, 9))
    plt.title("湖北疫情预测曲线")
    plt.xticks(rotation=45)
    plt.xlabel('日期', font1)
    date, wuhan_conNum = import_data(day)
    t = range(len(date))
    coef, pcov = curve_fit(logistic, t, wuhan_conNum)
    print(coef)
    y_values = logistic(t, coef[0], coef[1], coef[2])
    # for a, b in zip(date, expect_wuhan_conNum):
    #     plt.text(a, b, b, ha='center', va='bottom')
    values_line, = plt.plot(date, y_values, "r-o", label="拟合曲线")
    # 27天
    pre_date = ['02-17', '02-18', '02-19', '02-20', '02-21', '02-22', '02-23', '02-24', '02-25',
                '02-26', '02-27', '02-28', '02-29', '03-01', '03-02', '03-03', '03-04', '03-05',
                '03-06', '03-07', '03-08', '03-09', '03-10', '03-12', '03-13', '03-14', '03-15']
    x = np.linspace(37, 65, 27)
    y_predict = logistic(x, coef[0], coef[1], coef[2])
    # print(y_predict)
    y_predict_to_int = y_predict.astype(int)
    print(y_predict_to_int)
    # for a, b in zip(pre_date, y_predict_to_int):
    #     plt.text(a, b, b, ha='center', va='bottom')
    prediction_line, = plt.plot(pre_date, y_predict, "g-*", label="预测曲线")
    plt.legend(handles=[values_line, prediction_line],
               labels=["拟合曲线", "预测曲线"], loc="upper left", fontsize=15)
    plt.show()


if __name__ == '__main__':
    day = '2020-02-17'
    prediction_data(day)