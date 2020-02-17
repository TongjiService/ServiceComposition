import numpy as np
import time
import random
f = open(r"C:/graduate/数据集/WSdream/dataset1/zq.txt")
data=f.readlines()
xxx=np.array(data)
list=[]
task_name=[]
input=[]
output=[]
ResponseTime=[]
Availability=[]
ThroughPut=[]
QoS=[]
number=[]
t=0
for line in xxx:
    odom=line.split(' ')
    a=odom[2]
    input.append(a)
    b=odom[3]
    output.append(b)
    c=odom[1]
    task_name.append(c)
    d=float(odom[4])
    ResponseTime.append(d)
    e=float(odom[5])
    Availability.append(e)
    f=float(odom[6])
    ThroughPut.append(f)
w=[]
service=[]
start=time.clock()
rt_min=min(ResponseTime)
tp_max=max(ThroughPut)
av_max=max(Availability)
for i in range(len(ResponseTime)):#每一个的指标
    ResponseTime[i]=rt_min/ResponseTime[i]
for i in range(len(ThroughPut)):
    ThroughPut[i]=ThroughPut[i]/tp_max
for i in range(len(Availability)):
    Availability[i]=Availability[i]/av_max
for i in range(len(task_name)):
    QoS.append((ResponseTime[i]+ThroughPut[i]+Availability[i])/3)
#print(QoS)
ServiceSet_av=[]#符合这些的点集
ServiceSet_rt=[]
ServiceSet_tp=[]
ServiceSet_qos=[]
for iii in range(0,55):
    w.append(iii)
for i in range(55):
    if w==[]:
        break
    if i in w:
        best=i
        w.remove(best)
        for j in range(55):
            if task_name[j]==task_name[best]and j!=best:
                if j in w:
                    w.remove(j)
                if float(QoS[j])>float(QoS[best]):
                    best=j
        if best not in ServiceSet_qos:
            ServiceSet_qos.append(best)
for iii in range(0,55):
    w.append(iii)
for i in range(55):
    if w==[]:
        break
    if i in w:
        best=i
        w.remove(best)
        for j in range(55):
            if task_name[j]==task_name[best]and j!=best:
                if j in w:
                    w.remove(j)

                if float(Availability[j])>float(Availability[best]):#对比特大案件
                    best=j
        if best not in ServiceSet_av:
            ServiceSet_av.append(best)
for iii in range(0,55):
    w.append(iii)
for i in range(55):
    if w==[]:
        break
    if i in w:
        best=i
        w.remove(best)
        for j in range(55):
            if task_name[j]==task_name[best]and j!=best:
                if j in w:
                    w.remove(j)
                if float(ThroughPut[j]>ThroughPut[best]):#对比普通案件
                    best=j
        if best not in ServiceSet_tp:
            ServiceSet_tp.append(best)
for iii in range(0,55):
    w.append(iii)
for i in range(55):
    if w==[]:
        break
    if i in w:
        best=i
        w.remove(best)
        for j in range(55):
            if task_name[j]==task_name[best]and j!=best:
                if j in w:
                    w.remove(j)
                if float(ResponseTime[j] > ResponseTime[best]):#对比紧急案件
                    best=j
        if best not in ServiceSet_rt:
            ServiceSet_rt.append(best)





ServiceArray_qos=np.zeros([len(ServiceSet_qos),len(ServiceSet_qos)])
for i in range(len(ServiceSet_qos)):
    for j in range(len(ServiceSet_qos)):
        if i!=j and output[ServiceSet_qos[i]]==input[ServiceSet_qos[j]]:
	        ServiceArray_qos[i,j]=QoS[ServiceSet_qos[j]]

ServiceArray_av=np.zeros([len(ServiceSet_av),len(ServiceSet_av)])
for i in range(len(ServiceSet_av)):
    for j in range(len(ServiceSet_av)):
        if i!=j and output[ServiceSet_av[i]]==input[ServiceSet_av[j]]:
	        ServiceArray_av[i,j]=Availability[ServiceSet_av[j]]

ServiceArray_rt=np.zeros([len(ServiceSet_rt),len(ServiceSet_rt)])
for i in range(len(ServiceSet_rt)):
    for j in range(len(ServiceSet_rt)):
        if i!=j and output[ServiceSet_rt[i]]==input[ServiceSet_rt[j]]:
	        ServiceArray_rt[i,j]=ResponseTime[ServiceSet_rt[j]]

ServiceArray_tp=np.zeros([len(ServiceSet_tp),len(ServiceSet_tp)])
for i in range(len(ServiceSet_tp)):
    for j in range(len(ServiceSet_tp)):
        if i!=j and output[ServiceSet_tp[i]]==input[ServiceSet_tp[j]]:
	        ServiceArray_tp[i,j]=ThroughPut[ServiceSet_tp[j]]
#print(ServiceSet_qos)
#print(ServiceArray_qos)

def youhua_av(input_,num):
    i = 0
    j = 0
    step=0
    qqos = 0
    aav=1

    rrt=0
    for i in range(len(ServiceSet_av)):
        if input[ServiceSet_av[i]]==input_:
            #print("state in ",ServiceSet_rt[i])
            break
    qqos=qqos+ float(QoS[ServiceSet_av[i]])
    aav=aav*float(Availability[ServiceSet_av[i]])
    ttp=float(ThroughPut[ServiceSet_av[i]])
    rrt=rrt+float(ResponseTime[ServiceSet_av[i]])
    while step != num:
        if ServiceArray_av[i][j] != 0:
            #print("service goes to ", ServiceSet_rt[j] )
            qqos = qqos + float(QoS[ServiceSet_av[j]])
            aav = aav * float(Availability[ServiceSet_av[j]])
            ttp = min(ttp ,float(ThroughPut[ServiceSet_av[j]]))
            rrt = rrt + float(ResponseTime[ServiceSet_av[j]])
            i = j
            j = 0
            step = step + 1

        elif ServiceArray_av[i][j] == 0:
            j = j + 1
            if j >= len(ServiceArray_av):
                break
    #print('服务综合指标',qqos)
    #print('可用性',aav*av_max)
    #print('响应时间',rt_min/rrt)
    #print('吞吐量',ttp*tp_max)
    return qqos,aav*av_max,rt_min/rrt,ttp*tp_max

def youhua_rt(input_,num):
    i = 0
    j = 0
    step=0
    qqos = 0
    aav=1

    rrt=0
    for i in range(len(ServiceSet_rt)):
        if input[ServiceSet_rt[i]]==input_:
            #print("state in ",ServiceSet_rt[i])
            break
    qqos=qqos+ float(QoS[ServiceSet_rt[i]])
    aav=aav*float(Availability[ServiceSet_rt[i]])
    ttp=float(ThroughPut[ServiceSet_rt[i]])
    rrt=rrt+float(ResponseTime[ServiceSet_rt[i]])
    while step != num:
        if ServiceArray_rt[i][j] != 0:
            #print("service goes to ", ServiceSet_rt[j] )
            qqos = qqos + float(QoS[ServiceSet_rt[j]])
            aav = aav * float(Availability[ServiceSet_rt[j]])
            ttp = min(ttp ,float(ThroughPut[ServiceSet_rt[j]]))
            rrt = rrt + float(ResponseTime[ServiceSet_rt[j]])
            i = j
            j = 0
            step = step + 1

        elif ServiceArray_rt[i][j] == 0:
            j = j + 1
            if j >= len(ServiceArray_rt):
                break
    #print('服务综合指标',qqos)
    #print('可用性',aav*av_max)
    #print('响应时间',rt_min/rrt)
    #print('吞吐量',ttp*tp_max)
    return qqos,aav*av_max,rt_min/rrt,ttp*tp_max

def youhua_tp(input_,num):
    i = 0
    j = 0
    step=0
    qqos = 0
    aav=1

    rrt=0
    for i in range(len(ServiceSet_tp)):
        if input[ServiceSet_tp[i]]==input_:
            #print("state in ",ServiceSet_rt[i])
            break
    qqos=qqos+ float(QoS[ServiceSet_tp[i]])
    aav=aav*float(Availability[ServiceSet_tp[i]])
    ttp=float(ThroughPut[ServiceSet_tp[i]])
    rrt=rrt+float(ResponseTime[ServiceSet_tp[i]])
    while step != num:
        if ServiceArray_tp[i][j] != 0:
            #print("service goes to ", ServiceSet_rt[j] )
            qqos = qqos + float(QoS[ServiceSet_tp[j]])
            aav = aav * float(Availability[ServiceSet_tp[j]])
            ttp = min(ttp ,float(ThroughPut[ServiceSet_tp[j]]))
            rrt = rrt + float(ResponseTime[ServiceSet_rt[j]])
            i = j
            j = 0
            step = step + 1

        elif ServiceArray_rt[i][j] == 0:
            j = j + 1
            if j >= len(ServiceArray_rt):
                break
    #print('服务综合指标',qqos)
    #print('可用性',aav*av_max)
    #print('响应时间',rt_min/rrt)
    #print('吞吐量',ttp*tp_max)
    return qqos,aav*av_max,rt_min/rrt,ttp*tp_max

def youhua_qos(input_,num):
    i = 0
    j = 0
    step=0
    qqos = 0
    aav=1

    rrt=0
    for i in range(len(ServiceSet_qos)):
        if input[ServiceSet_qos[i]]==input_:
            #print("state in ",ServiceSet_rt[i])
            break
    qqos=qqos+ float(QoS[ServiceSet_qos[i]])
    aav=aav*float(Availability[ServiceSet_qos[i]])
    ttp=float(ThroughPut[ServiceSet_qos[i]])
    rrt=rrt+float(ResponseTime[ServiceSet_qos[i]])
    while step != num:
        if ServiceArray_qos[i][j] != 0:
            #print("service goes to ", ServiceSet_rt[j] )
            qqos = qqos + float(QoS[ServiceSet_qos[j]])
            aav = aav * float(Availability[ServiceSet_qos[j]])
            ttp = min(ttp ,float(ThroughPut[ServiceSet_qos[j]]))
            rrt = rrt + float(ResponseTime[ServiceSet_qos[j]])
            i = j
            j = 0
            step = step + 1

        elif ServiceArray_qos[i][j] == 0:
            j = j + 1
            if j >= len(ServiceArray_qos):
                break
    #print('服务综合指标',qqos)
    #print('可用性',aav*av_max)
    #print('响应时间',rt_min/rrt)
    #print('吞吐量',ttp*tp_max)
    return qqos,aav*av_max,rt_min/rrt,ttp*tp_max
#1:qos   2:av   3:rt   4:tp
#qqos,aav*av_max,rt_min/rrt,ttp*tp_max
def youhua(input1,input2,num,leixing):
    if leixing==1:#qos
        print("综合QoS为",youhua_qos(input1, num)[0]+youhua_qos(input2, num)[0])
        print("综合可靠性为",youhua_qos(input1, num)[1]*youhua_qos(input2, num)[1])
        print("综合响应时间为",max(youhua_qos(input1, num)[2],youhua_qos(input2, num)[2]))
        print("综合吞吐量为",min(youhua_qos(input1, num)[3],youhua_qos(input2, num)[3]))

    elif leixing==2:#av
        print("综合QoS为",youhua_av(input1, num)[0]+youhua_av(input2, num)[0])
        print("综合可靠性为",youhua_av(input1, num)[1]*youhua_av(input2, num)[1])
        print("综合响应时间为",max(youhua_av(input1, num)[2],youhua_av(input2, num)[2]))
        print("综合吞吐量为",min(youhua_av(input1, num)[3],youhua_av(input2, num)[3]))
    elif leixing==3:#rt
        if youhua_rt(input1,num)[2]>youhua_rt(input2,num)[2]:
            print("综合QoS为", youhua_rt(input1, num)[0] + youhua_qos(input2, num)[0])
            print("综合可靠性为", youhua_rt(input1, num)[1] * youhua_qos(input2, num)[1])
            print("综合响应时间为", max(youhua_rt(input1, num)[2], youhua_qos(input2, num)[2]))
            print("综合吞吐量为", min(youhua_rt(input1, num)[3], youhua_qos(input2, num)[3]))
        else:
            print("综合QoS为", youhua_qos(input1, num)[0] + youhua_rt(input2, num)[0])
            print("综合可靠性为", youhua_qos(input1, num)[1] * youhua_rt(input2, num)[1])
            print("综合响应时间为", max(youhua_qos(input1, num)[2], youhua_rt(input2, num)[2]))
            print("综合吞吐量为", min(youhua_qos(input1, num)[3], youhua_rt(input2, num)[3]))
    elif leixing==4:#tp
        if youhua_tp(input1,num)[3]<youhua_tp(input2,num)[3]:
            print("综合QoS为", youhua_tp(input1, num)[0] + youhua_qos(input2, num)[0])
            print("综合可靠性为", youhua_tp(input1, num)[1] * youhua_qos(input2, num)[1])
            print("综合响应时间为", max(youhua_tp(input1, num)[2], youhua_qos(input2, num)[2]))
            print("综合吞吐量为", min(youhua_tp(input1, num)[3], youhua_qos(input2, num)[3]))
        else:
            print("综合QoS为", youhua_qos(input1, num)[0] + youhua_tp(input2, num)[0])
            print("综合可靠性为", youhua_qos(input1, num)[1] * youhua_tp(input2, num)[1])
            print("综合响应时间为", max(youhua_qos(input1, num)[2], youhua_tp(input2, num)[2]))
            print("综合吞吐量为", min(youhua_qos(input1, num)[3], youhua_tp(input2, num)[3]))
    elif leixing==5:#对比rt
        print("综合QoS为",youhua_rt(input1, num)[0]+youhua_rt(input2, num)[0])
        print("综合可靠性为",youhua_rt(input1, num)[1]*youhua_rt(input2, num)[1])
        print("综合响应时间为",max(youhua_rt(input1, num)[2],youhua_rt(input2, num)[2]))
        print("综合吞吐量为",min(youhua_rt(input1, num)[3],youhua_rt(input2, num)[3]))
    elif leixing==6:#对比tp
        print("综合QoS为",youhua_tp(input1, num)[0]+youhua_tp(input2, num)[0])
        print("综合可靠性为",youhua_tp(input1, num)[1]*youhua_tp(input2, num)[1])
        print("综合响应时间为",max(youhua_tp(input1, num)[2],youhua_tp(input2, num)[2]))
        print("综合吞吐量为",min(youhua_tp(input1, num)[3],youhua_tp(input2, num)[3]))


    return 1,1,1,1

#1:qos   2:av   3:rt   4:tp   5:对比rt   6:对比tp
#qqos,aav*av_max,rt_min/rrt,ttp*tp_max

print(1)
youhua('A','B',2,4)
print(2)
youhua('A','B',2,6)
print(3)
youhua('A','B',2,1)