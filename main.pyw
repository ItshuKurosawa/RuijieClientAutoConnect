from ping3 import ping
from time import sleep
from os import startfile

def main():
    second = check()
    if second == None:
        for times in range(6):
            sleep(10)
            second = check()
            if second != None:
                print(second)
                break
        if times == 5:
            print('已断线')
            relink()

def check():
    second = ping('www.hust.edu.cn')
    print(second)
    return second

def relink():
    startfile(r'C:\Program Files\Ruijie Networks\Ruijie Supplicant\noUAC.RuijieSupplicant.lnk')
    print('已重连')

if __name__ == '__main__':
    main()
