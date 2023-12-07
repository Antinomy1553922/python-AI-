import math
import pyinputplus as pyip

#一個參數，有傳出值
def cricle_area(redius):          #function的redius
    area = redius ** 2 * math.pi
    return area                   #function的area



radius = pyip.inputFloat("請輸入半徑：")     #整個文件的radius
print(radius)
area = cricle_area(radius)                  #整個文件的area
print(f"輸入半徑為「{radius}」，得出園面積為「{area:.5f}」")

#這裡的radius：引數值
#引數值：真正的值
#傳回上方參數，應用在程式區塊，得出園面積
