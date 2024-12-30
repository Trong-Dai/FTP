import os
import pandas as pd
import os.path
from datetime import datetime,timedelta
from ftplib import FTP
from pandas import *
import ftplib
from datetime import time
import schedule
from time import sleep
import shutil
import math


# def Create_log():
#     os.system("python DUAC.py > output.txt")
#     source_file=open('output.txt', 'rb')
#     destination_file=open('log.txt','ab')
#     shutil.copy2(source_file,destination_file)
#     source_file.close()
#     destination_file.close()  
# def my_code():
#     schedule.every().day.at('14:02').do(process)
#     while True:
#         schedule.run_pending()
#         sleep(1)
CRED = '\033[31m'
END = '\033[0m'
SBLUE='\033[34m'
SGREEN='\033[32m'
SYELLOW = '\033[93m'
now=datetime.now()
curr_today=now.strftime('%A')
curr_time=datetime.today().strftime('%d-%m-%Y %H:%M:%S')
tomorrow = now+timedelta(1)
hostname=''
user=''
pwd=''
link=''
soluongfile=0
tgstart="07:14"

def download(hostname,user,pwd,link,soluongfile):
    ftp=FTP(str(hostname))
    ftp.login(str(user),str(pwd))
    files=ftp.nlst()
    start = datetime.now()
    count=1
    filetai=-1*int(soluongfile)
    print("Đang tải "+str(SGREEN)+str(filetai)+" files "+str(END)+"dữ liệu của server",str(SBLUE)+hostname+str(END))
    for file in files[int(soluongfile):]:
        print(count,".Downloading..." + file)
        ftp.retrbinary("RETR " + file ,open(str(link) + file, 'wb').write)
        count=count+1
    ftp.close()
    end = datetime.now()
    diff = end - start
    filethieu=filetai-(count-1)
    if filethieu==0:
        print(str(SGREEN)+"Tất cả các file được tải trong vòng " + str(diff.seconds) + "s"+". Đã hoàn thành!"+str(END))
    else:
        print("File tải còn thiếu"+str(CRED),filethieu,"files."+str(END))
    
def check_host(hostname,user,pwd,timeout=5):
     try:
         ftp = ftplib.FTP(hostname, timeout=timeout)
         ftp.login(str(user),str(pwd))
         ftp.quit()
         return True
     except ftplib.all_errors:
         return False
def process():
    print(curr_today+"  "+curr_time)
    print('******************************************')
    data=pd.read_csv('./TTD.csv')
    df=pd.DataFrame(data)
    for i in df:
        val=[]
        for j in range(0,len(df)):
            val.append(df[i][j])
        hostname=val[0]
        user=val[1]
        pwd=val[2]
        link=val[3]
        soluongfile=val[4]
        check_host(hostname,user,pwd,timeout=5)
        if check_host(hostname,user,pwd,timeout=5)==True:
            print(str(SGREEN)+"Server"+str(END),str(SBLUE)+hostname+str(END),str(SGREEN)+"Kết nối thành công!"+str(END))
            download(hostname,user,pwd,link,soluongfile)
        else:
            print(str(CRED)+"Server "+str(END)+str(SBLUE)+hostname+str(END)+str(CRED)+" Không kết nối...."+str(END))
            ping=os.system('ping '+str(hostname))
            print("===========================================")
    

    print("===========================================")
    print("Finished!")
    print(str(SYELLOW)+"Thời gian tải dữ liệu tiếp theo:",tgstart,":AM"+" ngày",tomorrow.strftime('%d-%m-%Y')+str(END))
    print(str(SYELLOW)+"Không được tắt chương trình!"+str(END))
def Create_log():  
    os.system("python DUAC.py > output.txt")
    with open('output.txt','r') as firstfile, open('log.txt','a') as secondfile: 
    # read content from first file 
        for line in firstfile: 
                # append content to second file 
                secondfile.write(line)
        firstfile.close()
        secondfile.close()

def main():
    print("****************DUAC-VNU*****************")
    schedule.every().day.at(tgstart).do(process)
    while True:
        schedule.run_pending()
        sleep(1)
main()






