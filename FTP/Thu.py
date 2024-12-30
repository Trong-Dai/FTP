import openpyxl
import pandas as pd
import os.path
from datetime import datetime
from ftplib import FTP
from pandas import *
# hostname="'"+"172.16.3.48"+"'";user="'"+"vnunet"+"'";pwd="'"+"vnunet@#2017"+"'";link="'"+"D:/Backup/"+"'"
# print(hostname)
# print(user)
# print(pwd)
# print(link)
# def prodata():
#     data = pd.read_excel('./TTD.xlsx')
#     df=pd.DataFrame(data)
#     dc=df.to_dict()
#     print(dc)
#     for x, obj in dc.items():
#         # print(x)
#         hostname="'"+str(x)+"'"
#         for y in obj:
#             user="'"+obj[0]+"'"
#             pwd="'"+obj[1]+"'"
#             link="'"+obj[2]+"'"
#     print(hostname,user,pwd,link)

def dowload(hostname,user,pwd,link,soluongfile):
    ftp=FTP(str(hostname))
    ftp.login(str(user),str(pwd))
    files=ftp.nlst()
    start = datetime.now()
    print("Dang copy du lieu server "+hostname)
    print("====================================")
    for file in files[int(soluongfile):]:
        print("Downloading..." + file)
        ftp.retrbinary("RETR " + file ,open(str(link) + file, 'wb').write)
    ftp.close()
    end = datetime.now()
    diff = end - start
    print('All files downloaded for ' + str(diff.seconds) + 's'+" Da hoan thanh /n")
def main():
    data=pd.read_csv('./TTD.csv')
    df=pd.DataFrame(data)
    # print(df)

    for i in df:
        val=[]
        hostname=''
        user=''
        pwd=''
        link=''
        soluongfile=0
        for j in range(0,len(df)):
            val.append(df[i][j])
        # print(val)
        hostname=val[0]
        user=val[1]
        pwd=val[2]
        link=val[3]
        soluongfile=val[4]
        # print(hostname)
        # print(user)
        # print(pwd)
        # print(link)
        # print(soluongfile)
        dowload(hostname,user,pwd,link,soluongfile)
        os.system("python Thu.py | tee output.txt")
main()






