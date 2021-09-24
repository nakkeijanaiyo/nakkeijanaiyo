'''

import tkinter

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('ボタンのサンプル') # 画面タイトルの設定

# ボタンの作成
btn = tkinter.Button(tki, text='ボタン') # ボタンの設定(text=ボタンに表示するテキスト)
btn.place(x=300, y=0) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()

import tkinter
from tkinter import messagebox

# click時のイベント
def btn_click():
  messagebox.showinfo("メッセージ", "ボタンがクリックされました")


# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('ボタンのサンプル') # 画面タイトルの設定

# ボタンの作成
btn = tkinter.Button(tki, text='ボタン', command = btn_click)
btn.place(x=700, y=400) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()
'''

import tkinter as tk
from tkinter.constants import X

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('Python-tkinter : タイトルです')





#pack()
'''
buttonA = tk.Button(
  baseGround, text="ボタンA").pack()

buttonB = tk.Button(
  baseGround, text="ボタンB").pack(side= tk.LEFT)

buttonC = tk.Button(
  baseGround, text="ボタンC").pack(side= tk.RIGHT)

baseGround.mainloop()
'''


#grid()メソッドを使用して画面にボタンを配置すると、行(row)と列(column)
#を指定して部品を配置することができます


#grid()
'''
buttonA = tk.Button(
    baseGround, text = 'ボタンA').grid(row= 0, column=1)
 
buttonB = tk.Button(
    baseGround, text = 'ボタンB').grid(row= 0, column=2)
 
buttonC = tk.Button(
    baseGround, text = 'ボタンC').grid(row= 0, column=3)
 
baseGround.mainloop()
'''

#place()
'''
buttonA = tk.Button(
  baseGround, text= "ボタンA").place(x=50, y=100)

buttonB = tk.Button(
  baseGround, text= "ボタンB").place(x=100, y=150)

buttonC = tk.Button(
  baseGround, text= "ボタンC").place(x=150, y=200)

baseGround.mainloop()
'''

#Label()のパラメータにtextを指定することで、ラベルの名前を設定することができます。
#また、foregroundを指定するとラベルの色を設定できます。
#backgroundを指定すると、ラベルの背景色を設定することができます。

#Label
'''
label1 = tk.Label(text="ここにラベルを表示" , foreground= "orange" , background="black")
label1.pack()

baseGround.mainloop()
'''

#tkinterを使って画面に1行のテキストボックスを配置する場合はEntry()を使用します
#また、パラメータにwidthを指定することで、テキストボックスの大きさを設定することができます。


#ラベル
'''
label = tk.Label(text= "テキストボックス")
label.place(x=30, y=70)

#テキストボックス
txtBox = tk.Entry(width=20)
txtBox.place(x=30, y=90)

baseGround.mainloop()
'''




























































































