import json
import time
import schedule
from asciichartpy import plot
from datetime import datetime
import os

# 你的函数，获取BTC数量和价格
def get_btc_data():
    # 这里使用了模拟数据，你需要替换成你的函数
    return 0.1, 50000

# 初始数据
def init_history():
    f= open("btc_data.json", "r")
    # read from json and but into data
    data = json.load(f)
    return data
data = init_history()
def job():
    # load data 
    # 获取数据
    btc, price = get_btc_data()
    # 获取当前时间
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 3将数据添加到字典中
    data["time"].append(now)
    data["price"].append(price)
    # 写入json文件
    with open("btc_data.json", "w") as f:
        json.dump(data, f)

    # 清除屏幕
    os.system('cls' if os.name == 'nt' else 'clear')

    # 绘制价格曲线
    print(plot(data["price"], {"height": 10}))

def plot(): 
    #data = init_history()
    schedule.every(1).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

plot()