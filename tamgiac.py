# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:51:36 2024

@author: BAO KHANH
"""

a=float(input("Độ dài cạnh a:"))
b=float(input("Độ dài cạnh b:"))
c=float(input("Độ dài cạnh c:"))
if a==b==c:
    print("Đây là tam giác đều")
elif a==b or a==c or b==c:
    print("Đây là tam giác cân")
elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
    print("Đây là tam giác vuông")
else:
    print("Đây là tam giác thường")