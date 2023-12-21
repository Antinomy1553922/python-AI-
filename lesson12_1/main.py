import pyinputplus as pyip
from tools import getStudents,save_to_csv


if __name__ == "__main__":
    s_nums:int = pyip.inputInt("請輸入學生的數量(1~50人)：",min=1,max=50)
    students:list[str] = getStudents(s_nums)
    fileName = pyip.inputFilename("請輸入檔案名稱(不需要副檔名稱)：")
    save_to_csv(students,fileName)
