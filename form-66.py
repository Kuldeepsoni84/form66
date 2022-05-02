import pandas as pd

import csv
import format_file
df=pd.read_csv('dummy.csv')
total_stu=list(df['roll'])
present_stu=list(df[df['absent']!='ABS']['roll'])
absent_stu=list(df[df['absent']=='ABS']['roll'])
file=open('form66.txt','w')
date=input('Enter Exam Date:')
sub=input('Enter Sub Cde And Name:')
f=open('dummy.csv')
def l_len(reg_stu,b_stu):
    if ab_stu.count('---')==0:
        return len(reg_stu)-len(ab_stu)
    else:
        return len(reg_stu)-len(ab_stu)+1
w=format_file.series(f,absent_stu)
for line in range(0,len(w),20):
    format_file.header(file,line//20+1)
    for i in range(line,line+20):
        if i<len(w):
            mask=(df['roll']>=int(w[i][0]))&(df['roll']<=int(w[i][-1]) )
            x=df.loc[mask]
            reg_stu=list(x['roll'])
            ab_stu=list(x[x['absent']=='ABS']['roll'])
            if len(ab_stu)== 0:
                ab_stu.append('---')
            #print(type(w[i][0]),i,",".join([str(item) for item in ab_stu]))
            if len(ab_stu)<=4:
                file.write('\n')
                file.write(('|'+date).ljust(12,' ')+sub.ljust(26,' ')+w[i][0]+'-'+w[i][-1].ljust(9,' ')+str(len(reg_stu)).rjust(4,' ')+"|"+",".join([str(item) for item in ab_stu]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+str(l_len(reg_stu,ab_stu))).ljust(25,' ')+'|')
                file.write('\n')
                file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
            else:
                #print(ab_stu)
                for r in range(0,len(ab_stu),4):
                    if r==0:
                        #print(r)
                        file.write('\n')
                        file.write(('|'+date).ljust(12,' ')+sub.ljust(26,' ')+w[i][0]+'-'+w[i][-1].ljust(9,' ')+str(len(reg_stu)).rjust(4,' ')+"|"+",".join([str(item) for item in ab_stu[r:r+4]]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+str(l_len(reg_stu,ab_stu))).ljust(25,' ')+'|')
                        #file.write('\n')
                        #file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                    else:
                        #print(r)
                        file.write('\n')
                        file.write('|'.ljust(12,' ')+''.ljust(26,' ')+"".rjust(22,' ')+"|"+",".join([str(item) for item in ab_stu[r:r+4]]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+"").ljust(25,' ')+'|')
                        file.write('\n')
                        file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                    
                
        else:
            file.write('\n')
            file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
    #format_file.middle(file,total_stu,absent_stu,present_stu)
    file.write('\n')
    file.write('|'+'-'*141+'|')
    if len(w)-line<=20:
        format_file.middle(file,total_stu,absent_stu,present_stu)
    format_file.footer(file)
    file.write('\n\n')
file.close()
