import serial
import time
# 打开串口
ser = serial.Serial("COM3", 115200)
def main():
    while True:
        # 获得接收缓冲区字符
        ser.write('reset'.encode('utf-8'))
        # ser.close()
        # ser.open()
        count = ser.inWaiting()
        print(count)
        if count != 0:
            # 读取内容并回显
            recv = ser.readlines()
            print(recv)
            ser.write(recv)
        # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()