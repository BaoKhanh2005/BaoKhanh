# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:33:22 2024

@author: BAO KHANH
"""

GPA=float(input("Nhập điểm trung bình:"))

if GPA<3.5:
    print("Học lực Kém")
elif 3.5<=GPA<5.0:
    print("Học lực Yếu")
elif 5.0<=GPA<7.0:
    print("Học lực trung bình")
elif 7.0<=GPA<8.0:
    print("Học lực Khá")
elif 8.0<=GPA<9.0:
    print("Học lực Giỏi")
elif 9.0<=GPA<10.0:
    print("Học lực Xuất Sắc")
else:
    print("Không xác định")
    