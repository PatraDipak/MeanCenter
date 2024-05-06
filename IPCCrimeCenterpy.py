import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
plt.rcParams["font.family"] = "Arial"

Nd=36
Numbers=[str(i+1) for i in range(Nd)]
dy1=[]
ty1=0
dy2=[]
ty2=0
dy3=[]
ty3=0
File="IPCrimeStatewise2020_2022Py"
sl=0
with open(File+'.txt',mode='r') as file:
     for lines in file:
         if sl>4:
           First=""
           Second=""
           Third=""
           X=lines.split()
           if X[0] in Numbers:
              #print(X)
              cy1=int(X[2])
              cy2=int(X[3])
              cy3=int(X[4])
              dy1.append(cy1) # 
              dy2.append(cy2)
              dy3.append(cy3)
              ty1+=cy1
              ty2+=cy2
              ty3+=cy3
         sl+=1
         #if sl>50:
         #   break
         
##print("2020 cases = ", dy1)
##print("2021 cases = ", dy2)
##print("2022 cases = ", dy3)

#print("2020 total cases = ", ty1)
#print("2021 total cases = ", ty2)
#print("2022 total cases = ", ty3)


Long=[]
Lat=[]
Population=[]
with open("IndiaCapitalAdharData.txt","r") as file:
     ## IndiaCapitalAdharData     IndiaCapital
     for txt in file.readlines():
         line=txt.split()
         n=len(line)
         if n!=0:
            if line[0]=="#":
               break
            else:
               if line[0]!="City":
                  Long.append(float(line[1]))
                  Lat.append(float(line[3]))
                  Population.append(float(line[5]) )


def Point(Long,Lat,Rad):
    d=np.pi/180 #1degree eqivalent to .... pi
    lat=d*Lat
    long=d*Long
    x=Rad*np.cos(long)*np.cos(lat)
    y=Rad*np.sin(long)*np.cos(lat)
    z=Rad*np.sin(lat)
    return x,y,z

def LongLat(X,Y,Z,Rad):
    a=180/np.pi #pi to degree eqivalent
    lat=np.arcsin(Z/Rad)
    long=np.arctan(Y/X)
    LAT=a*lat
    LONG=a*long
    return LONG,LAT


#N=len(Long)
N=Nd

Cm=np.zeros(3)
R=6371

gc=[1 for i in range(Nd)] #for middle point
dp=dy3#Population #gc, Population,  dy1, dy2, dy3
dpsum=sum(dp)
NodesR=np.zeros((N,3))
K=np.zeros(N)
for i in range(N):
    x,y,z=Point(Long[i],Lat[i],Rad=R)
    Cm[0]+=x*dp[i]
    Cm[1]+=y*dp[i]
    Cm[2]+=z*dp[i]
    NodesR[i][0]=x 
    NodesR[i][1]=y
    NodesR[i][2]=z
    K[i]=dp[i]/dpsum
Cm[:]=Cm[:]/dpsum
CmLong,CmLat=LongLat(Cm[0],Cm[1],Cm[2],Rad=R)
print("CM long lat ", CmLong,CmLat)


