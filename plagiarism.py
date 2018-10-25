from bs4 import BeautifulSoup
import requests
import os
filename= input("enter the file name : ")
path=os.path.abspath(filename)
file_name=open(path,"r")
line=file_name.readline()
search=requests.get("http://www.google.com/search?btnG=1&q="+line)
x=search.text
bs=BeautifulSoup(x,"html.parser")
result=bs.select(".r a")
for i in range(min(4,len(result))) :
	print(result[i].get('href'))
result2=bs.select("h3")
for i in range(min(4,len(result2))) :
	print(result2[i].get_text())

