---
title: pyWin32的简单使用
date: 2018-06-12 17:19:44
tags:
---

```python
import win32gui
import win32con
import win32api

# 從頂層窗口向下搜索主窗口，無法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口類名 窗口標題名
handle = win32gui.FindWindow("Notepad", None)


# 獲取窗口位置
left, top, right, bottom = win32gui.GetWindowRect(handle)
#獲取某個句柄的類名和標題
title = win32gui.GetWindowText(handle)
clsname = win32gui.GetClassName(handle)

# 打印句柄
# 十進制
print(handle)
# 十六進制
print("%x" %(handle) )


# 搜索子窗口
# 枚舉子窗口
hwndChildList = []
win32gui.EnumChildWindows(handle, lambda hwnd, param: param.append(hwnd),  hwndChildList)

# FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None) 父窗口句柄 若不為0，則按照z-index的順序從hwndChildAfter向後開始搜索子窗體，否則從第一個子窗體開始搜索。 子窗口類名 子窗口標題
subHandle = win32gui.FindWindowEx(handle, 0, "EDIT", None)

# 獲得窗口的菜單句柄
menuHandle = win32gui.GetMenu(subHandle)
# 獲得子菜單或下拉菜單句柄
# 參數：菜單句柄 子菜單索引號
subMenuHandle = win32gui.GetSubMenu(menuHandle, 0)
# 獲得菜單項中的的標誌符，注意，分隔符是被編入索引的
# 參數：子菜單句柄 項目索引號
menuItemHandle = win32gui.GetMenuItemID(subMenuHandle, 0)
# 發送消息，加入消息隊列，無返回
# 參數：句柄 消息類型 WParam IParam
win32gui.postMessage(subHandle, win32con.WM_COMMAND, menuItemHandle, 0)


# wParam的定義是32位整型，high word就是他的31至16位，low word是它的15至0位。
# 當參數超過兩個，wParam和lParam不夠用時，可以將wParam就給拆成兩個int16來使用。
# 這種時候在python裏記得用把HIWORD的常數向左移16位，再加LOWORD，即wParam = HIWORD<<16+LOWORD。

# 下選框內容更改
# 參數：下選框句柄； 消息內容； 參數下選框的哪一個item，以0起始的待選選項的索引；如果該值為-1，將從組合框列表中刪除當前選項，並使當前選項為空； 參數
# CB_Handle為下選框句柄，PCB_handle下選框父窗口句柄
if win32api.SendMessage(CB_handle, win32con.CB_SETCURSEL, 1, 0) == 1:
# 下選框的父窗口命令
# 參數：父窗口句柄； 命令； 參數：WParam：高位表示類型，低位表示內容；參數IParam，下選框句柄
# CBN_SELENDOK當用户選擇了有效的列表項時發送，提示父窗體處理用户的選擇。 LOWORD為組合框的ID. HIWORD為CBN_SELENDOK的值。
            win32api.SendMessage(PCB_handle, win32con.WM_COMMAND, 0x90000, CB_handle)
# CBN_SELCHANGE當用户更改了列表項的選擇時發送，不論用户是通過鼠標選擇或是通過方向鍵選擇都會發送此通知。LOWORD為組合框的ID. HIWORD為CBN_SELCHANGE的值。
            win32api.SendMessage(PCB_handle, win32con.WM_COMMAND, 0x10000, CB_handle)


# 設置文本框內容，等窗口處理完畢後返回true。中文需編碼成gbk
# 參數：句柄；消息類型；參數WParam，無需使用； 參數IParam，要設置的內容，字符串
win32api.SendMessage(handle, win32con.WM_SETTEXT, 0, os.path.abspath(fgFilePath).encode('gbk'))


# 控件點擊確定,處理消息後返回0
# 參數:窗口句柄; 消息類型; 參數WParam HIWORD為0（未使用），LOWORD為控件的ID; 參數IParam  0（未使用）,確定控件的句柄
win32api.SendMessage(Mhandle, win32con.WM_COMMAND, 1, confirmBTN_handle)


# 獲取窗口文本不含截尾空字符的長度
# 參數：窗口句柄； 消息類型； 參數WParam； 參數IParam
bufSize = win32api.SendMessage(subHandle, win32con.WM_GETTEXTLENGTH, 0, 0) +1
# 利用api生成Buffer
strBuf = win32gui.PyMakeBuffer(bufSize)
print(strBuf)
# 發送消息獲取文本內容
# 參數：窗口句柄； 消息類型；文本大小； 存儲位置
length = win32gui.SendMessage(subHandle, win32con.WM_GETTEXT, bufSize, strBuf)
# 反向內容，轉為字符串
# text = str(strBuf[:-1])

address, length = win32gui.PyGetBufferAddressAndLen(strBuf)
text = win32gui.PyGetString(address, length)
# print('text: ', text)

# 鼠標單擊事件
#鼠標定位到(30,50)
win32api.SetCursorPos([30,150])
#執行左單鍵擊，若需要雙擊則延時幾毫秒再點擊一次即可
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#右鍵單擊
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

def click1(x,y):                #第一種
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def click2(x,y):               #第二種
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2,0,0,0,0)
    ctypes.windll.user32.mouse_event(4,0,0,0,0)

def click_it(pos):          #第三種
    handle= win32gui.WindowFromPoint(pos)
    client_pos =win32gui.ScreenToClient(handle,pos)
    tmp=win32api.MAKELONG(client_pos[0],client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)

# 發送回車
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


# 關閉窗口
win32gui.PostMessage(win32lib.findWindow(classname, titlename), win32con.WM_CLOSE, 0, 0)


# 檢查窗口是否最小化，如果是最大化
if(win32gui.IsIconic(hwnd)):
#     win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.ShowWindow(hwnd, 8)
    sleep(0.5)

# SW_HIDE：隱藏窗口並激活其他窗口。nCmdShow=0。
# SW_MAXIMIZE：最大化指定的窗口。nCmdShow=3。
# SW_MINIMIZE：最小化指定的窗口並且激活在Z序中的下一個頂層窗口。nCmdShow=6。
# SW_RESTORE：激活並顯示窗口。如果窗口最小化或最大化，則系統將窗口恢復到原來的尺寸和位置。在恢復最小化窗口時，應用進程應該指定這個標誌。nCmdShow=9。
# SW_SHOW：在窗口原來的位置以原來的尺寸激活和顯示窗口。nCmdShow=5。
# SW_SHOWDEFAULT：依據在STARTUPINFO結構中指定的SW_FLAG標誌設定顯示狀態，STARTUPINFO 結構是由啟動應用進程的進程傳遞給CreateProcess函數的。nCmdShow=10。
# SW_SHOWMAXIMIZED：激活窗口並將其最大化。nCmdShow=3。
# SW_SHOWMINIMIZED：激活窗口並將其最小化。nCmdShow=2。
# SW_SHOWMINNOACTIVE：窗口最小化，激活窗口仍然維持激活狀態。nCmdShow=7。
# SW_SHOWNA：以窗口原來的狀態顯示窗口。激活窗口仍然維持激活狀態。nCmdShow=8。
# SW_SHOWNOACTIVATE：以窗口最近一次的大小和狀態顯示窗口。激活窗口仍然維持激活狀態。nCmdShow=4。
# SW_SHOWNORMAL：激活並顯示一個窗口。如果窗口被最小化或最大化，系統將其恢復到原來的尺寸和大小。應用進程在第一次顯示窗口的時候應該指定此標誌。nCmdShow=1。


# win32雖然也可控制鍵盤，但不如使用PyUserInput的方便。需要注意在windows和mac下接口參數可能有所不同。
from pymouse import PyMouse
from pykeyboard import PyKeyboard
m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
# 鼠標點擊
m.click(x_dim/2, y_dim/2, 1)
# 鍵盤輸入
k.type_string('Hello, World!')

# 按住一個鍵
k.press_key('H')
# 鬆開一個鍵
k.release_key('H')
# 按住並鬆開，tap一個鍵
k.tap_key('e')
# tap支持重複的間歇點擊鍵
k.tap_key('l',n=2,interval=5)
# 發送判斷文本
k.type_string('123456')

#創建組合鍵
k.press_key(k.alt_key)
k.tap_key(k.tab_key)
k.release_key(k.alt_key)
# 特殊功能鍵
k.tap_key(k.function_keys[5]) # Tap F5
k.tap_key(k.numpad_keys['Home']) # Tap 'Home' on the numpad
k.tap_key(k.numpad_keys[5], n=3) # Tap 5 on the numpad, thrice

# Mac系統
k.press_keys(['Command','shift','3'])
# Windows系統
k.press_keys([k.windows_l_key,'d'])

其中的PyMouseEvent和PyKeyboardEvent還可用於監聽鼠標和鍵盤事件的輸入
```
