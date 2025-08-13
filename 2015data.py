import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from matplotlib.pyplot import figure

my_url="C:\\Users\\SmileTech\\Downloads\\2015.csv"
print(os.path.exists(my_url))  # it works when i give any wrong path it aware me

my_df=pd.read_csv(my_url)


my_df1=pd.DataFrame(my_df)

my_df2=pd.concat([my_df1["Country"],my_df1["Region"],my_df1["Happiness Rank"],my_df1["Happiness Score"],my_df1["Economy (GDP per Capita)"],my_df1["Year"],my_df1["Freedom"],my_df1["Health (Life Expectancy)"]],axis=1)
#I filtered  some main columns  of the data


pd.set_option("display.max_rows",100)  #it helps me to give the highest rows of the data but now  i only take 100 rows
pd.set_option("display.max_columns",None)  #it helps me to give the highest columns of the data
pd.set_option("display.width",1200)  #it  increases the width of the termninal by which i can see all columns in the data when i cannot see all the columns  of the data

print(my_df2)

top_100=my_df2.sort_values("Happiness Rank",ascending=True).head(100)






plt.figure(figsize=(22,15))
sns.barplot(data=top_100,x="Country",y="Happiness Rank",saturation=0.75,errorbar=("ci",95),err_kws={"color":"blue"})
plt.xticks(rotation=90,fontsize=8,color="green")
plt.yticks(color="green",fontsize=8)
plt.xlabel("Country",color="blue",fontsize=12)
plt.ylabel("Happiness_Rank",color="red",fontsize=12)



plt.grid(True,color="gray",alpha=0.5)
plt.tight_layout()

plt.show()


sns.barplot(data=top_100,x="Country",y="Happiness Score",hue="Region",saturation=0.80,errorbar=None,err_kws={"color":"blue"})
plt.xlabel("Country(Region)",color="blue",fontsize=15)
plt.ylabel("Happiness Score of the  Country",color="red",fontsize=15)

plt.xticks(color="green",fontsize=8,rotation=90)
plt.yticks(color="green",fontsize=8)
sns.set_style("darkgrid")
plt.grid(True,alpha=0.5)
plt.title("The Happiness Score of top 100 Countries in the different Region",color="green",fontsize=18)
plt.tight_layout()
plt.show()








my_df3=pd.DataFrame(my_df2).head(100)
plt.figure(figsize=(10,6))
my_df3=my_df3.drop("Year",axis=1)
pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",1200)



correlation=my_df3.corr(numeric_only=True)
x5=sns.heatmap(data=correlation,annot=True,cmap="rocket_r",linecolor="black",vmin=-1,vmax=1,cbar=False,linewidths=2)
plt.xticks(color="green",fontsize=8,rotation=0)
plt.yticks(color='green',fontsize=8)
plt.title("Correlation Heatmap of Numeric Features",fontsize=15,color="green")
sns.set_style("darkgrid")
plt.show()

my_df4=pd.concat([my_df3["Happiness Score"],my_df3["Health (Life Expectancy)"],my_df3["Freedom"]],axis=1)


plt.figure(figsize=(10,6))
corr_matrix=my_df4.corr()

sns.heatmap(corr_matrix,vmin=-1,vmax=1,annot=True,cmap="rocket_r",linecolor="black",linewidths=2,cbar=False)
plt.xticks(color="green",fontsize=10)
plt.yticks(color="green",fontsize=10)
plt.title("Happness Score vs Freedom &Health",size=15,color="blue")

sns.set_style("darkgrid")

plt.show()


my_africa=my_df2[my_df2["Region"]=="Sub-Saharan Africa"].head(10)
my_westerEurope=my_df2[my_df2["Region"]=="Western Europe"].head(10)
my_northamerica=my_df2[my_df2["Region"]=="North America"].head(20)
my_middleafrica=my_df2[my_df2["Region"]=="Middle East and Northern Africa"].head(10)
my_southeastern=my_df2[my_df2["Region"]=="Southeastern Asia"].head(10)
my_asnw=my_df2[my_df2["Region"]=="Central and Eastern Europe"].head(10)
my_ausnew=my_df2[my_df2["Region"]=="Australia and New Zealand"].head(10)
my_latin=my_df2[my_df2["Region"]=="Latin America and Caribbean"].head(10)
my_eaternasia=my_df2[my_df2["Region"]=="Eastern Asia"].head(10)
my_southeasternasia=my_df2[my_df2["Region"]=="Southern Asia"].head(10)


print(f"The data of the region african \n :{my_africa}")
print(f"The data of the region african \n :{my_westerEurope}")
print(f"The data of the region \n {my_northamerica}")
print(f"The data of the region \n {my_middleafrica}")
print(f"The data of the region \n {my_southeastern}")
print(f"The data of the region \n {my_asnw}")
print(f"The data of the region \n {my_ausnew}")
print(f"The data of the region \n {my_latin}")
print(f"The data of the region \n {my_eaternasia}")
print(f"The data of the region \n {my_southeasternasia}")

#making sub-1(Region:Africa)
sns.set_style("darkgrid")

fig,axes=plt.subplots(5,2,figsize=(45,30))
sns.barplot(data=my_africa,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"blue"},saturation=0.75,ax=axes[0,0])



axes[0,0].set_xlabel("Region(Africa)",color="purple",fontsize=10)
axes[0,0].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[0,0].xaxis.set_tick_params(labelsize=7,labelcolor="green",length=1,width=1)
axes[0,0].yaxis.set_tick_params(labelsize=8,labelcolor="blue")


plt.tight_layout(pad=8)


#sub-2(Region:NorthAmerica)
sns.barplot(data=my_northamerica,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.80,ax=axes[0,1])



axes[0,1].set_xlabel("Region(North_America)",color="purple",fontsize=10)
axes[0,1].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[0,1].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)
axes[0,1].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)

plt.tight_layout(pad=8)


#sub-3(Region:SouthAsia)
sns.barplot(data=my_southeasternasia,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[1,0])
axes[1,0].set_xlabel("Region(South Asia)",color="purple",fontsize=10)
axes[1,0].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[1,0].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[1,0].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)


#sub-4(Region_Europe)



sns.barplot(data=my_westerEurope,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[1,1])
axes[1,1].set_xlabel("Region(Europe)",color="purple",fontsize=10)
axes[1,1].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[1,1].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[1,1].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)



#sub-5(Region:Australia and Newzealand)



sns.barplot(data=my_ausnew,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[2,0])
axes[2,0].set_xlabel("Region(Australia and Newzealand)",color="purple",fontsize=10)
axes[2,0].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[2,0].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[2,0].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)


#sub-6(Region:Latin_America)


sns.barplot(data=my_latin,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[2,1])
axes[2,1].set_xlabel("Region(Latin America)",color="purple",fontsize=10)
axes[2,1].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[2,1].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[2,1].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)




#sub-7 (Region:Southern Asia)

sns.barplot(data=my_southeastern,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[3,0])
axes[3,0].set_xlabel("Region(South EasternAsia)",color="purple",fontsize=10)
axes[3,0].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[3,0].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[1,0].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)


#sub-8 (Region:Middle Afirca)



sns.barplot(data=my_middleafrica,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[3,1])
axes[3,1].set_xlabel("Region(Middle Africa)",color="purple",fontsize=10)
axes[3,1].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[3,1].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[3,1].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)


plt.tight_layout(pad=8)


#sub-9 (Region-Central and Eastern Europe)





sns.barplot(data=my_asnw,x="Country",y="Happiness Score",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[4,0])
axes[4,0].set_xlabel("Region(Central and Eastern Europe)",color="purple",fontsize=10)
axes[4,0].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[4,0].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[4,0].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)


#sub_-10(Region:Eastern Asia)


sns.barplot(data=my_eaternasia,x="Country",y=f"{"Happiness Score"}",errorbar=None,err_kws={"color":"green"},saturation=0.70,ax=axes[4,1])
axes[4,1].set_xlabel("Region(Eastern Asia)",color="purple",fontsize=10)
axes[4,1].set_ylabel("Happiness Score",color="blue",fontsize=10)
axes[4,1].xaxis.set_tick_params(labelsize=8,labelcolor="green",length=1,width=1)

axes[4,1].yaxis.set_tick_params(labelsize=8,labelcolor="blue",length=1,width=1)



plt.tight_layout(pad=8)

plt.show()






