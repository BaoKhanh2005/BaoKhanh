# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:03:05 2024

@author: BAO KHANH
"""
import random
choices=["kéo","búa","bao"]
player= input("Nhập kết quả người chơi:")
if player not in ["kéo","búa","bao"]:
    print("sai kết quả , nhập lại")
system=random.choice(choices)
print("kết quả của máy")
if player==system:
    print("Bạn Hòa")
elif (player == "búa" and system=="kéo") or\
    (player == "kéo" and system=="bao") or\
     (player=="bao"and system =="búa"):
    print("bạn thắng")
else:
    print("bạn thua")
