import pyinputplus as pyip
import random

min = 1
max = 100
count = 0
random_number = random.randint(min,max) #包含max
print("================猜數字遊戲================")
while(True):
    keyin = pyip.inputInt(f"猜數字範圍{min}~{max}：")
    count += 1
    print(keyin)
    if keyin == random_number:
        print(f"今天的你歐氣滿滿，答案是:{random_number}！")
        print(f"你嘗試了{count}次")
        break
    elif keyin > random_number:
        print("再縮小一點！")
        max = keyin -1
    elif keyin < random_number:
        print("再放大一點！")
        min = keyin +1
    print(f"你嘗試了{count}次")
    print("======================")
        
        

print("遊戲結束")