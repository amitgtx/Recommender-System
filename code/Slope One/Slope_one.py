
# coding: utf-8

# In[63]:

import numpy as np
import pandas as pd
# l=["google","facebook","yahoo","youtube","wikipedia","flipkart","amazon"]
# n=7 #no. of sites
# m=20 #no. of users
# s=600 #no. of data
# av_diff=[[(-1,-1) for _ in xrange(n)]for _ in xrange(n)]
# d={}
# a=[[-1 for _ in xrange(n)]for _ in xrange(m)]
# r1=np.random.randint(0,n,s) #generating random sites
# r2=np.random.randint(0,m,s) #generating random users
# r3=[(r2[i],r1[i]) for i in xrange(s)] #merging users and sites


# In[64]:

l=["Item A","Item B","Item C"]
n=3 #no. of sites
m=3 #no. of users
av_diff=[[(-1,-1) for _ in xrange(n)]for _ in xrange(n)]
a=[[5,3,2],[3,4,-1],[-1,2,5]]


# In[65]:

# for i in xrange(s):
#     user="User "+str(r3[i][0])
#     site=l[r3[i][1]]
#     key=user,site
#     tmp=a[r3[i][0]][r3[i][1]]
#     if(tmp==-1):
#         a[r3[i][0]][r3[i][1]]=1
#     else:
#         a[r3[i][0]][r3[i][1]]+=1
#     if key in d:
#         d[key]+=1
#     else:
#         d[key]=1


# In[66]:

df1=pd.DataFrame(a)
df1.columns=l
df1


# In[67]:

for i in xrange(n):
    for j in xrange(n):
        tmp=0.0
        cnt=0.0
        for k in xrange(m):
            if(a[k][i]==-1 or a[k][j]==-1):
                continue
            tmp+=(a[k][i]-a[k][j])
            cnt+=1
        tmp_av=round(tmp/cnt,2)
        av_diff[i][j]=(tmp_av,cnt) #Storing pair(average difference,no. of users who rated both i & j site)


# In[68]:

df2=pd.DataFrame(av_diff)


# In[69]:

df2 #Item similarity matrix


# In[70]:

for i in xrange(m):
    for j in xrange(n):
        if(a[i][j]!=-1):continue #skipping those sites which are already rated
        num=0.0
        den=0.0
        for k in xrange(n):
            if(a[i][k]==-1):continue #skipping those site which are not rated
            num+=(av_diff[j][k][0]+a[i][k])*av_diff[j][k][1] #Weighted sum
            den+=av_diff[j][k][1]
        a[i][j]=int(num/den)
df3=pd.DataFrame(a)
df3.columns=l
df3


# In[ ]:



