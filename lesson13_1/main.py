import pyinputplus as pyip
from tools import getStudents,save_to_csv



if __name__ == "__main__":
    s_nums:int = pyip.inputInt("請輸入學生的數量(1~50人)：",min=1,max=50)
    students:list[str] = getStudents(s_nums)
    fileName = pyip.inputFilename("請輸入檔案名稱(不需要副檔名稱)：")
    format = pyip.inputChoice(['1','2'],"請選擇要輸出哪一種檔案格式：\n按1 輸出.xlsx\n按2 輸出.csv\n請輸入：")
    if format == '1':
        print("輸出xlsx")
    else:
        save_to_csv(students,fileName)
