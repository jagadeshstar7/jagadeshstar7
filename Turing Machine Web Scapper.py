from bs4 import BeautifulSoup
import requests
import pandas as pd

##Generating the required links
fill=[]
for i in range(2009,2019):
    for j in range(1,13):
        if j<10:
            f=str(i)+str(0)+str(j)
            fill.append(f)
        else:
            f=str(i)+str(j)
            fill.append(f)
links=[]
link="http://www.estesparkweather.net/archive_reports.php?date="
for i in fill:
    temp = link+str(i)
    links.append(temp)

total_data=[]
for i in links:
    url=i
    zoo = requests.get(url)
    soup = BeautifulSoup(zoo.text,'lxml')
    extracted_text=[]
    for i in soup.find_all("td"):
        #print(i.get_text())
        extracted_text.append(i.get_text())
    position=0
    for i in extracted_text:
    
        if "for Month of" and "up to" not in i:
            position=position+1
        else:
            break           
    
    #print(position)

    extracted_text=extracted_text[:position]
    total_data.extend(extracted_text)

#df=pd.DataFrame(total_data,columns=["data"])
#dxl=df.to_csv("big.csv")



#Date generations
date=[]
for i in total_data:
    if "Average and Extremes" in i:
        x=i[:-21]
        date.append(x)

dddd=[]
year=2009
count1=0
for i in date:
    if "Jan" in i:
        i=i[-2:]
        dd=str(year)+"-01-"+str(i)
        dddd.append(dd)
        
    if "Feb" in i:
        i=i[-2:]
        dd=str(year)+"-02-"+str(i)
        dddd.append(dd)
        
    if "Mar" in i:
        i=i[-2:]
        dd=str(year)+"-03-"+str(i)
        dddd.append(dd)   
        
    if "Apr" in i:
        i=i[-2:]
        dd=str(year)+"-04-"+str(i)
        dddd.append(dd)   
        
    if "May" in i:
        i=i[-2:]
        dd=str(year)+"-05-"+str(i)
        dddd.append(dd)   
        
    if "Jun" in i:
        i=i[-2:]
        dd=str(year)+"-06-"+str(i)
        dddd.append(dd)   
        
    if "Jul" in i:
        i=i[-2:]
        dd=str(year)+"-07-"+str(i)
        dddd.append(dd)    
        
    if "Aug" in i:
        i=i[-2:]
        dd=str(year)+"-08-"+str(i)
        dddd.append(dd)    
        
    if "Sep" in i:
        i=i[-2:]
        dd=str(year)+"-09-"+str(i)
        dddd.append(dd)   
        
    if "Oct" in i:
        i=i[-2:]
        dd=str(year)+"-10-"+str(i)
        dddd.append(dd)   
        
    if "Nov" in i:
        i=i[-2:]
        dd=str(year)+"-11-"+str(i)
        dddd.append(dd)    
        
    if "Dec" in i:
        i=i[-2:]
        dd=str(year)+"-12-"+str(i)
        dddd.append(dd)    
    
    count1=count1+1
    if 331<count1<=691:
        year=2010
    if 692<count1<=941:
        year=2011   
    if 942<count1<=1269:
        year=2012   
    if 1270<count1<=1598:
        year=2013   
    if 1599<count1<=1955:
        year=2014  
    if 1956<count1<=2306:
        year=2015  
    if 2307<count1<=2672:
        year=2016   
    if 2673<count1<=3008:
        year=2017   
    if count1>=3009:
        year=2018  
        
dddd = [x.replace(r' ','') for x in dddd]#removing blank spaces


##########CONVERTING STRING TO DATETIME FORMAT
from datetime import datetime
date=[]
for i in dddd:
    s=datetime.strptime(i,'%Y-%m-%d')
    date.append(s.date())#date()-removes the null time and keeps only the  date 

#generating column nmes  
columns=[]
for i in extracted_text[:38]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall"):
        columns.append(i)
    else:
        pass       

#generatind data values in seperate data frames
        
raw=[]
for i in total_data:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan") or i.startswith("Feb")or i.startswith("Mar")or i.startswith("Apr")or i.startswith("May")or i.startswith("Jun")or i.startswith("Jul")or i.startswith("Aug")or i.startswith("Sep")or i.startswith("Oct")or i.startswith("Nov")or i.startswith("Dec"):
        pass
    else:
        raw.append(i)

#################################################



       

#defining columns
Average_temperature= []
Average_humidity= []
Average_dewpoint= []
Average_barometer = []
Average_windspeed =[]
Average_gustspeed =[]
Average_direction = []
Rainfall_for_month =[]
Rainfall_for_year =[]
Maximum_rain_per_minute = []
Maximum_temperature = []
Minimum_temperature = []
Maximum_humidity = []
Minimum_humidity=[]
Maximum_pressure =[]
Minimum_pressure =[]
Maximum_windspeed =[]
Maximum_gust_speed =[]
Maximum_heat_index =[]

##slicing the data from total
count2=0   
for i in raw:
    try:
        Average_temperature.append(raw[count2])
        count2+=19
    except(IndexError):
        pass
    
        
count3=1  
for i in raw:
    try:
        Average_humidity.append(raw[count3])
        count3=count3+19 
    except(IndexError):
        pass
    
    
count4=2
for i in raw:
    try:
        Average_dewpoint.append(raw[count4])
        count4=count4+19
    except(IndexError):
        pass
    
    
count5=3
for i in raw:
    try:
        Average_barometer.append(raw[count5])
        count5=count5+19
    except(IndexError):
        pass
    
count6=4
for i in raw:
    try:
        Average_windspeed.append(raw[count6])
        count6=count6+19
    except(IndexError):
        pass
    
    
count7=5
for i in raw:
    try:
        Average_gustspeed.append(raw[count7])
        count7=count7+19   
    except(IndexError):
        pass
    
count8=6
for i in raw:
    try:
        Average_direction.append(raw[count8])
        count8=count8+19 
    except(IndexError):
        pass
    
count9=7
for i in raw:
    try:
        Rainfall_for_month.append(raw[count9])
        count9=count9+19
    except(IndexError):
        pass
    
    
count10=8
for i in raw:
    try:
        Rainfall_for_year.append(raw[count10])
        count10=count10+19
    except(IndexError):
        pass
    
count11=9
for i in raw:
    try:
        Maximum_rain_per_minute.append(raw[count11])
        count11=count11+19
    except(IndexError):
        pass
    
    
count12=10
for i in raw:
    try:
        Maximum_temperature.append(raw[count12])
        count12=count12+19
    except(IndexError):
        pass
    
count13=11
for i in raw:
    try:
        Minimum_temperature.append(raw[count13])
        count13=count13+19
    except(IndexError):
        pass
    
    
count14=12
for i in raw:
    try:
        Maximum_humidity.append(raw[count14])
        count14=count14+19
    except(IndexError):
        pass
    
count15=13
for i in raw:
    try:
        Minimum_humidity.append(raw[count15])
        count15=count15+19
    except(IndexError):
        pass
    
count16=14
for i in raw:
    try:
        Maximum_pressure.append(raw[count16])
        count16=count16+19
    except(IndexError):
        pass
    
count17=15
for i in raw:
    try:
        Minimum_pressure.append(raw[count17])
        count17=count17+19
    except(IndexError):
        pass
    
count18=16
for i in raw:
    try:
        Maximum_windspeed.append(raw[count18])
        count18=count18+19
    except(IndexError):
        pass
    
    
count19=17
for i in raw:
    try:
        Maximum_gust_speed.append(raw[count19])
        count19=count19+19
    except(IndexError):
        pass
    
count20=18
for i in raw:
    try:
        Maximum_heat_index.append(raw[count20])
        count20=count20+19
    except(IndexError):
        pass
    
#############################################    
dataframe=pd.DataFrame(columns=date)
dataframe=dataframe.T
dataframe.insert(0,"Average temperature (°F)",Average_temperature)
dataframe.insert(1,"Average humidity (%)",Average_humidity)        
dataframe.insert(2,"Average dewpoint (°F)",Average_dewpoint)         
dataframe.insert(3,"Average barometer (in)",Average_barometer)      
dataframe.insert(4,"Average windspeed (mph)",Average_windspeed)       
dataframe.insert(5,"Average gustspeed (mph)",Average_gustspeed)
dataframe.insert(6,"Average direction (°deg)",Average_direction) 
dataframe.insert(7,"Rainfall for month (in)",Rainfall_for_month) 
dataframe.insert(8,"Rainfall for year (in)",Rainfall_for_year) 
dataframe.insert(9,"Maximum rain per minute",Maximum_rain_per_minute) 
dataframe.insert(10,"Maximum temperature (°F)",Maximum_temperature) 
dataframe.insert(11,"Minimum temperature (°F)",Minimum_temperature) 
dataframe.insert(12,"Maximum humidity (%)",Maximum_humidity) 
dataframe.insert(13,"Minimum humidity (%)",Minimum_humidity) 
dataframe.insert(14,"Maximum pressure",Maximum_pressure) 
dataframe.insert(15,"Minimum pressure",Minimum_pressure) 
dataframe.insert(16,"Maximum windspeed (mph)",Maximum_windspeed) 
dataframe.insert(17,"Maximum gust speed (mph)",Maximum_gust_speed)   
dataframe.insert(18,"Maximum heat index (°F)",Maximum_heat_index)   

############  trimming the units and keeps only digit data

dataframe['Average temperature (°F)']=dataframe['Average temperature (°F)'].str.replace(r'�F', '')
dataframe['Average humidity (%)']=dataframe['Average humidity (%)'].str.replace(r'%', '')
dataframe['Average dewpoint (°F)']=dataframe['Average dewpoint (°F)'].str.replace(r'�F', '')
dataframe['Average barometer (in)']=dataframe['Average barometer (in)'].str.replace(r'in.', '')
dataframe['Average windspeed (mph)']=dataframe['Average windspeed (mph)'].str.replace(r'mph', '')
dataframe['Average gustspeed (mph)']=dataframe['Average gustspeed (mph)'].str.replace(r'mph', '')
dataframe['Average direction (°deg)']=dataframe['Average direction (°deg)'].str.extract(r'(\d+)')
dataframe['Rainfall for month (in)']=dataframe['Rainfall for month (in)'].str.extract(r'(\d+.\d+)')
dataframe['Rainfall for year (in)']=dataframe['Rainfall for year (in)'].str.extract(r'(\d+.\d+)')
dataframe['Maximum rain per minute']=dataframe['Maximum rain per minute'].str.extract(r'(\d+.\d+)')
dataframe['Maximum temperature (°F)']=dataframe['Maximum temperature (°F)'].str.extract(r'(\d+.\d+)')
dataframe['Minimum temperature (°F)']=dataframe['Minimum temperature (°F)'].str.extract(r'(\d+.\d+)')
#dataframe['Maximum humidity (%)']=dataframe['Maximum humidity (%)'].str.extract(r'(\d+\s\%)|(\d+\%)')
#dataframe['Minimum humidity (%)']=dataframe['Minimum humidity (%)'].str.extract(r'(\d+\s\%)|(\d+\%)')
dataframe['Minimum humidity (%)']=[x[:4] for x in dataframe['Minimum humidity (%)']]#slicing based on lenght of each char in a column
dataframe['Maximum humidity (%)']=[x[:4] for x in dataframe['Maximum humidity (%)']]

#removing blank space and removing the % symbol
dataframe['Minimum humidity (%)']=[x.replace(r' ','') if x.endswith(" ") else x for x in dataframe['Minimum humidity (%)']]
dataframe['Minimum humidity (%)']=[x.replace(r'%', '') if x.endswith("%") else x for x in dataframe['Minimum humidity (%)']]

#removing blank space and removing the % symbol
dataframe['Maximum humidity (%)']=[x.replace(r' ','') if x.endswith(" ") else x for x in dataframe['Maximum humidity (%)']]
dataframe['Maximum humidity (%)']=[x.replace(r'%', '') if x.endswith("%") else x for x in dataframe['Maximum humidity (%)']]


dataframe['Maximum pressure']=[x[:-28] for x in dataframe['Maximum pressure']]
dataframe['Minimum pressure']=[x[:-28] for x in dataframe['Minimum pressure']]
dataframe['Maximum windspeed (mph)']=[x[:-28] for x in dataframe['Maximum windspeed (mph)']]
dataframe['Maximum gust speed (mph)']=[x[:-45] for x in dataframe['Maximum gust speed (mph)']]
dataframe['Maximum heat index (°F)']=[x[:-26] for x in dataframe['Maximum heat index (°F)']]

#removing the blank spaces
dataframe['Maximum gust speed (mph)']=[x.replace(r' ','') for x in dataframe['Maximum gust speed (mph)']]



#changing the data types of dataframe from string to numeric values

dataframe = dataframe.apply(pd.to_numeric)

dataframe = dataframe[:3280]#removing unwanted rows


        
#saving as pickle file##
import pickle
with open("dataframe.pk", "wb") as file:
    pickle.dump(dataframe,file)

j  = pd.read_pickle("dataframe.pk")


dataframe.dtypes

type(date)



