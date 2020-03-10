# -*- coding: utf-8 -*-
import numpy as np
import copy
import time
import datetime
import threading
import csv

#初期条件
sampling_interval = 0.2 ##[s]
N = 2048 
count = 0

#空行列を作成
date_data = []
rate_data = []
    
##データリストを作成
for i in range(50):
    #########計測開始###########
    start = time.time() 
    date_data.append(str(datetime.datetime.now())) #計測時間を取得
    rate_data.append(i) #計測データを取得
    end =time.time()
    time.sleep(sampling_interval-(end-start)) #一回のループが0.2秒になるように調整
    #########計測終了###########


########計測開始##########
start = time.time()

#ファイルを10個に分割
filename_list = [date_data[0],date_data[5],date_data[10],date_data[15],date_data[20],\
    date_data[25],date_data[30],date_data[35],date_data[40],date_data[45]]

#取得したリストをファイル出力
for k in filename_list:
    with open('%s.csv'% k, 'a',newline="") as f:
        #一つのファイルに5個記載
        for n in range(5):
            writer = csv.writer(f)
            writer.writerow([date_data[count+n],rate_data[count+n]])
    f.close()
    count = count+ 5

new_data = copy.copy(rate_data) #配列をコピー
new_date = copy.copy(date_data) #配列をコピー

end =time.time()
time.sleep(sampling_interval-(end-start))
########計測終了(この間0.2秒)##########


##新規データを取得
new_data.append(1) ##新規データ
del new_data[0]
new_date.append(str(datetime.datetime.now()))
del new_date[0]
    
before = np.array(rate_data)
after = np.array(new_data)

delta_array = after - before
print(before)
print(after)
print(delta_array)
print(len(delta_array))
            
