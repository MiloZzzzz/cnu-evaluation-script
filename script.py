import keyboard
import time
from pynput.keyboard import Controller, Key
import threading

SLEEPTIME = 0.05

keyboard_controller = Controller()
print("=== 自动按键脚本（增强版）===")
print("按数字1键开始执行预设按键序列")
print("按ESC键随时终止程序或当前序列")
print("\n=============================")
print("使用教程如下")
print("1.使用前先复制一个‘无’字")
print("2.进入评教界面，选择一个老师，点进去，随后不要点任何位置")
print("3.按数字1键，启动脚本，将会自动完成所有评教，默认100分，评价为无")
print("如果没有反应请先esc结束，然后点击空白处，保证可以用tab键切换不同的选项。随后按1")

# 定义全局事件用于控制线程
stop_event = threading.Event()

def run_sequence():
    global stop_event
    stop_event.clear()  # 重置停止标志
    print("开始执行按键序列...")
    
    try:
        # 阶段1：循环10次Tab和上箭头
        for _ in range(17):
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press_and_release('tab')
            print("按下Tab键")
            time.sleep(SLEEPTIME)
            
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press_and_release('up')
            print("按下上箭头键")
            time.sleep(SLEEPTIME)
        
        # 阶段2：输入一次Tab＋三次上箭头
        if stop_event.is_set():
            raise InterruptedError("用户终止")
        keyboard.press_and_release('tab')
        print("按下Tab键")
        time.sleep(SLEEPTIME)
        
        for _ in range(3):
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press_and_release('up')
            print("按下上箭头键")
            time.sleep(SLEEPTIME)

        if stop_event.is_set():
            raise InterruptedError("用户终止")
        keyboard.press_and_release('tab')
        print("按下Tab键")
        time.sleep(SLEEPTIME)
        
        if stop_event.is_set():
            raise InterruptedError("用户终止")
        keyboard.press_and_release('up')
        print("按下上箭头键")
        time.sleep(SLEEPTIME)

        if stop_event.is_set():
            raise InterruptedError("用户终止")
        keyboard.press_and_release('tab')
        print("按下Tab键")
        time.sleep(SLEEPTIME)
        
        # 阶段3：输入两次Ctrl+V
        for _ in range(2):
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press('ctrl')
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release('ctrl')
            print("按下Ctrl+V")
            time.sleep(SLEEPTIME)
            
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press_and_release('tab')
            print("按下Tab键")
            time.sleep(SLEEPTIME)

        if stop_event.is_set():
            raise InterruptedError("用户终止")
        keyboard.press_and_release('space')
        print("按下空格键")

        for i in range(3):
            if stop_event.is_set():
                raise InterruptedError("用户终止")
            keyboard.press_and_release('space')
            print("按下空格键")
            time.sleep(SLEEPTIME)
            
        if not stop_event.is_set():
            print("序列执行完毕！")
            
    except InterruptedError as e:
        print(e)
        print("序列已终止")
    finally:
        stop_event.clear()  # 重置停止标志

# ESC键回调函数
def on_esc_press(e):
    if e.name == 'esc':
        print("检测到ESC键，正在终止当前操作...")
        stop_event.set()  # 设置停止标志
        # 这里可以添加额外的清理代码
    return False  # 停止事件传播

# 设置ESC键监听器
keyboard.on_press_key('esc', on_esc_press)

# 主循环
try:
    print("程序运行中，等待按键...")
    sequence_thread = None
    
    while True:
        if keyboard.is_pressed('1') and (sequence_thread is None or not sequence_thread.is_alive()):
            time.sleep(0.2)  # 防抖
            sequence_thread = threading.Thread(target=run_sequence)
            sequence_thread.start()
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("程序已退出")
finally:
    stop_event.set()  # 确保线程停止
    keyboard.unhook_all()  # 清理键盘监听器
    print("程序已安全退出")