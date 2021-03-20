# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:34:38 2021

@author: nikhi
"""


#Taking Input from the file ip.txt

f=open('ip.txt')
input_string=f.readlines()

#Taking input - No of Employees
employee_count= int(input("Enter No of Employees: "))
least=10**10

splitted_data=[]
for each in input_string:
    splitted_data.append(each.split(": "))
for i in range(len(splitted_data)):
    x=splitted_data[i]
    x[1]=int(x[1][:])

#Empty Dictionary to store Goodie Name and its price as Key-Value Pair
d={}
for item in splitted_data:
    d[item[1]]=item[0]

#Sorting the prices
arr_keys=sorted(list(d.keys()))


#Main Logic
result_i=0
l=len(arr_keys)
for value in range(0,l-employee_count):
    if arr_keys[-1+value+employee_count]-arr_keys[value]<least:
        result_i=value
        least=arr_keys[-1+value+employee_count]-arr_keys[value]

#Result
for each in arr_keys[result_i:(employee_count+result_i)]:
    print('{}: {}'.format(d[each],each))

f.close()