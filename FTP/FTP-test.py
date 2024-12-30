
import os
import ftplib
from datetime import datetime
# from ftplib import FTP
import datetime
import pathlib
import shutil
# # from dateutil import parser
# server = ftplib.FTP()
# server.connect('172.16.3.52')
# server.login('vnunet','vnunet@#2017')
# # filename=server.nlst()
# # print(filename)
# # ds=server.retrlines('LIST')
# # print(ds)
# # print(server.dir())
# # print(date.today())
# print(server.nlst())
# for i in server.nlst():
#     print(i)
import os
import sys
import math
import pandas as pd
import time
import datetime
from datetime import datetime
import os.path,time
from ftplib import FTP
# hostname="172.16.3.52"
# response = os.system("ping -n 1 "+hostname)
# print(response)
# for i in range(10,15):
#     print(i)
# os.system("python FTP-test.py > output.txt")
# shutil.copy2('output.txt','log.txt')
# # with open('log.txt','a+') as log:
# #     log.close()
# # with open("output.txt",'r') as op:
# #     op.close()

def process():
    # print(curr_today+"  "+curr_time)
    print('******************************************')
    data=pd.read_csv('./TTD.csv')
    df=pd.DataFrame(data)
    for i in df:
        val=[]
        hostname=''
        user=''
        pwd=''
        link=''
        soluongfile=0
        for j in range(0,len(df)):
            val.append(df[i][j])
        hostname=val[0]
        user=val[1]
        pwd=val[2]
        link=val[3]
        soluongfile=val[4]
        print(val)
        print(hostname,user,pwd,link)
        # check_host(hostname,user,pwd,timeout=5)
        # if check_host(hostname,user,pwd,timeout=5)==True:
        #     print(str(SGREEN)+"Server"+str(END),str(SBLUE)+hostname+str(END),str(SGREEN)+"Kết nối thành công!"+str(END))
        #     download(hostname,user,pwd,link,soluongfile)
        # else:
        #     print(str(CRED)+"Server "+str(END)+str(SBLUE)+hostname+str(END)+str(CRED)+" Không kết nối...."+str(END))
        #     ping=os.system('ping '+str(hostname))
        #     print("===========================================")
        #     continue
        val.clear()
        print(val)
# def Delete_file():
#     path='D:/tftp/FTP/Backup/172.16.3.52/'
#     datenow = datetime.now().month
#     for x in os.listdir(path):
#         create_date=os.path.getctime(path)
#         modify_date = datetime.fromtimestamp(create_date).month
#         ts=datenow-modify_date
#         print(ts)
        # if datenow-modify_date>1:
        #     os.remove(str(path+x))
        # modify_date=time.strftime("%m")
        # print("Ngay modi kieu int:",int(modify_date))
       
        # sl=datenow-int(modify_date)
        # print("Ngay hien tai:",datenow)
        # os.remove(str(path+x))
        # print(datenow)
        # print(int(datenow)-int(create_date))
        # if datenow-int(create_date)>1:
            
    # print(os.listdir(path))
    
    # for i in :
    #     b=os.path.getctime(path)
    #     c=time.ctime(b)
    #     # print(c)
    #     print(i,c)
        # os.remove(str(path+i))
    # print(os.listdir(path))
def Delete_file():
    path='D:/1. VNU-DUAC/1. Document/01. Main job/1. Hệ thống mạng/'
    dem=0
    Crr_month = datetime.now().month
    Crr_year=datetime.now().year
    Crr_day=datetime.now().day
    
    # ftp=FTP('172.16.3.48')
    # ftp.login('vnunet','vnunet@#2017')
    # files=ftp.nlst()
    # print(files)
    # for x in range(0,len(os.listdir(path))):
    #     create_date=os.path.getctime(path)
    #     print(x,"Ngày tạo")
    #     # print(create_date,"Create time")
    #     modify_date = datetime.fromtimestamp(create_date).month
    #     print(modify_date)
    #     if datenow-modify_date>3:
    #         # os.remove(str(path+x))
    #         dem+=1
    #     break
    # if dem==0:print("Không có dữ liệu vượt quá 3 tháng")
    # else:print("Đã xóa",dem,"files dữ liệu vượt quá 3 tháng!")
    path='112.137.132.67'
    print(os.listdir(path))
    for x in os.listdir(path):
        File_month = time.strftime('%m', time.localtime(os.path.getmtime(path+x)))
        File_year=time.strftime('%Y', time.localtime(os.path.getmtime(path+x)))
        File_day=time.strftime('%d', time.localtime(os.path.getmtime(path+x)))
        date1 = datetime(int(File_year),int(File_month),int(File_day))
        date2 = datetime(int(Crr_year),int(Crr_month),int(Crr_day))
        delta = date2 - date1
        print(x,File_year,File_month,File_day,"=",delta.days,"ngày")
        if delta.days>90:
            os.remove(str(path+x))
            dem+=1
    print(os.listdir(path))
        
        # print(File_month,File_year,File_day)
        # print(type(File_day),type(File_month),type(File_year))
        
        
        # print(formatted_time)

# Delete_file()
# hostname=''
# now=datetime.now().strftime('%p')
# ftp=FTP('112.137.132.67')
# ftp.login('adminbackup','')
# files=ftp.nlst()
# for i in files:
#     print(i)
#     print(ftp.size(str(i)))
# print(os.path.getsize('D:/tftp/FTP/Backup/112.137.132.67/'+str(i),'   1'))
# print(now,type(now))

# import os.path, time
# def modifile():
#     path='D:/1. VNU-DUAC/1. Document/01. Main job/1. Hệ thống mạng'
#     for x in os.listdir(path):
#         print(x)
#         file = pathlib.Path(str(x))
#         print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
#         print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))
# # process()
# modifile()
print(12/(1+2)+2**2)