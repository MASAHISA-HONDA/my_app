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
    start = time.time()
    get_date = str(datetime.datetime.now())
    date_data.append(get_date)
    rate_data.append(i)##暫定値###

    end =time.time()
    time.sleep(sampling_interval-(end-start))

##リストをファイル出力
start = time.time()

filename_list = [date_data[0],date_data[5],date_data[10],date_data[15],date_data[20],\
    date_data[25],date_data[30],date_data[35],date_data[40],date_data[45]]

for k in filename_list:
    with open('%s.csv'% k, 'a',newline="") as f:
        for n in range(5):
            writer = csv.writer(f)
            writer.writerow([date_data[count+n],rate_data[count+n]])
    f.close()

    count = count+ 5

end =time.time()
new_data = copy.copy(rate_data)
print(end-start)

time.sleep(sampling_interval-(end-start))

##新規データを取得
new_data.append(1) ##新規データ
del new_data[0]
    
before = np.array(rate_data)
after = np.array(new_data)

delta_array = after - before
print(before)
print(after)
print(delta_array)
            
