
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



import tkinter as tk
from tkinter.constants import X, Y
from typing import TYPE_CHECKING, DefaultDict, Text

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('Python-tkinter : タイトルです')




#pack()


buttonA = tk.Button(
  baseGround, text="ボタンA").pack()

buttonB = tk.Button(
  baseGround, text="ボタンB").pack(side= tk.LEFT)

buttonC = tk.Button(
  baseGround, text="ボタンC").pack(side= tk.RIGHT)

baseGround.mainloop()



#grid()メソッドを使用して画面にボタンを配置すると、行(row)と列(column)
#を指定して部品を配置することができます


#grid()

buttonA = tk.Button(
    baseGround, text = 'ボタンA').grid(row= 0, column=1)
 
buttonB = tk.Button(
    baseGround, text = 'ボタンB').grid(row= 0, column=2)
 
buttonC = tk.Button(
    baseGround, text = 'ボタンC').grid(row= 0, column=3)
 
baseGround.mainloop()


#place()

buttonA = tk.Button(
  baseGround, text= "ボタンA").place(x=50, y=100)

buttonB = tk.Button(
  baseGround, text= "ボタンB").place(x=100, y=150)

buttonC = tk.Button(
  baseGround, text= "ボタンC").place(x=150, y=200)

baseGround.mainloop()


#Label()のパラメータにtextを指定することで、ラベルの名前を設定することができます。
#また、foregroundを指定するとラベルの色を設定できます。
#backgroundを指定すると、ラベルの背景色を設定することができます。

#Label

label1 = tk.Label(text="ここにラベルを表示" , foreground= "orange" , background="black")
label1.pack()

baseGround.mainloop()


#tkinterを使って画面に1行のテキストボックスを配置する場合はEntry()を使用します
#また、パラメータにwidthを指定することで、テキストボックスの大きさを設定することができます。


#ラベル

label = tk.Label(text= "テキストボックス")
label.place(x=30, y=70)

#テキストボックス
txtBox = tk.Entry(width=20)
txtBox.place(x=30, y=90)

baseGround.mainloop()


#複数行のテキストボックスの作成と配置
textbox = tk.Text(width= 30, height= 15)    #テキストボックスの大きさ
textbox.pack()

baseGround.mainloop()



#画面にボタンを配置(色付き)
buttonA = tk.Button(
  baseGround, text="ボタンA",foreground="red").pack()

buttonB = tk.Button(
    baseGround, text="ボタンB", foreground="blue").pack()

baseGround.mainloop()


#ラジオボタンの作成
# ラジオボタンに表示する文字列
item= ['A', 'B', 'C', 'D']

# Intvarオブジェクトを作成して変数に代入
val = tk.IntVar()

# ラジオボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # 親要素を指定
    tk.Radiobutton(baseGround,
                   # valueの値を1にする
                   value = i,
                   # variableにIntVarオブジェクトを指定
                   variable =val,
                   # textにリストitemのi番目の要素を指定
                   text = item[i]
                   # 左寄せで配置する
                   ).pack(anchor=tk.W)

# ラジオボタンの状態を通知する関数
def choice():
    # Intvarオブジェクトの値を取得
    ch = val.get()
    #リストitemのインデックスをchに指定して要素を出力
    print(item [ch] + 'を選択しました。')
    
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = 'OK',
                # クリック時にchoice()関数を呼ぶ
                command = choice
                ).pack(side = tk.LEFT)

baseGround.mainloop()




#画面にチェックボタンを配置する
#チェックボタンに表示する文字列を用意
item = ["手帳", "口座手帳" , "キャッシュカード", "住民票"]

check = {}

#itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
  # BooleanVarオブジェクトを作成しリストのcheck要素に追加
  check[i] = tk.BooleanVar()
  #チェックボタンの作成と配置
  tk.Checkbutton(baseGround,
                 variable=check[i], text=item[i]).pack(anchor=tk.W)
            
  
#チェックボタンの状態を通知する関数
def select():
  #辞書check要素の数だけ繰り返す
  for i in check:
    if check[i].get() == True:
      print(item[i] + "チェックしました")
  
#ボタンの作成と配置
button = tk.Button(baseGround, text="必需品",
                   #クリックしたときにselect()を呼ぶ
                   command=select).pack(anchor=tk.W)
                  

baseGround.mainloop()




#スピンボックスの配置
spinbox = tk.Spinbox(baseGround, value = ("ボックス1", "ボックス2", "ボックス3", "ボックス4"))
spinbox.pack()

baseGround.mainloop()




#画面にメニューを配置する
def callback():
  print("プログラムを閉じる")

menubar = tk.Menu(baseGround)

baseGround.config(menu=menubar)

file = tk.Menu(menubar)
menubar.add_cascade(label="ファイル",menu=file)

file.add_cascade(label="閉じる", command=callback)

edit = tk.Menu(menubar)
menubar.add_cascade(label="エディット",menu=edit)


baseGround.mainloop()





#値をラベルに表示する
def btn_click():

    # 入力した値を取得
    text1 = input_text.get()
    # 入力した値をラベルに出力
    label2['text'] = text1


# テキストボックス
input_text = tk.Entry()
input_text.pack()

# ボタン
btn = tk.Button(baseGround, text='入力値を出力', command=btn_click)
btn.pack()

# ラベル
label1 = tk.Label(text = '入力値:')
label1.pack()
label2 = tk.Label()
label2.pack()

#表示
baseGround.mainloop()





import tkinter as tk

#前の画面から別の画面に遷移(せんい)する方法
def btn_click():
  #最初のGUIの画面に戻る
  def return_view():
    baseGround_new_csv.destroy()
  baseGround_new_csv = tk.Tk()

    #GUIの画面のサイズ
  baseGround_new_csv.geometry("300x200")
  #GUIの画面タイトル
  baseGround_new_csv.title("次の画面")



  #ボタン
  btn_return = tk.Button(baseGround_new_csv, text="前のGUIの画面に戻る")
  btn_return.pack()
  baseGround_new_csv.mainloop()

baseGround = tk.Tk()
#GUIの画面サイズ
baseGround.geometry("300x200")
#GUIの画面タイトル
baseGround.title("最初の画面")

#ボタン
btn = tk.Button(baseGround,text="次の画面に移動", command=btn_click)
btn.place(x=120, y=140)

#表示
baseGround.mainloop()







import tkinter as tk
import random
 
 
def btn_click():
 
    num = random.randint(0, 2)
 
    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()
 
    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('300x200')
    #GUIの画面タイトル
    baseGround_new_csv.title('結果')
    if i == num:
        lbl_filename = tk.Label(baseGround_new_csv, text='あいこです。')
    elif i == 0 and num == 1 or i == 1 and num == 2 or i == 2 and num == 0:
        lbl_filename = tk.Label(baseGround_new_csv, text='あなたの勝ちです。')
    else:
        lbl_filename = tk.Label(baseGround_new_csv, text='あなたの負けです。')
        
    lbl_filename.pack()
 
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()
 
baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('300x200')
#GUIの画面タイトル
baseGround.title('最初の画面')
label1 = tk.Label(baseGround, text="ジャンケンをします。")
label1.pack()
label2 = tk.Label(baseGround, text="グーチョキパーのどれかを選択してください。")
label2.pack()
# ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click)
btn.place(x=120, y=140)
 
# ラジオボタンに表示する文字列
item= ['グー', 'チョキ', 'パー']
 
# Intvarオブジェクトを作成して変数に代入
val = tk.IntVar()
 
# ラジオボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # 親要素を指定
    tk.Radiobutton(baseGround,
                   # valueの値
                   value = i,
                   # variableにIntVarオブジェクトを指定
                   variable =val,
                   # textにリストitemのi番目の要素を指定
                   text = item[i]
                   # 左寄せで配置する
                   ).pack()
 
#表示
baseGround.mainloop()






   
#BMI計算アプリ
import tkinter as tk


def btn_click():
    

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()

    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('500x300')

    
    #GUIの画面タイトル
    baseGround_new_csv.title('結果')

    height = text1.get()
    #stringからfloatに
    height_f = float(height)
    
    weight = text2.get()
    #stringからfloatに
    weight_f = float(weight)

    
    height_m = height_f / 100
    result = weight_f / (height_m * height_m)
    result_str = str(round(result, 2))

    #BMI計算
    if result < 18.5:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で低体重(やせ型)です')
    elif result >= 18.5 and result < 25:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で普通体重です')
    elif result >= 25 and result < 30:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(1度)です')
    elif result >= 30 and result < 35:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(2度)です')
    elif result >= 35 and result < 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(3度)です')
    elif result >= 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(4度)です')
    else:
        lbl_result = tk.Label(baseGround_new_csv, text='エラーです。')
          
    lbl_result.pack()
    
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()

baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('500x300')
#GUIの画面タイトル
baseGround.title('BMI計算')
label1 = tk.Label(baseGround, text="BMIの計算")
label1.pack()
label2 = tk.Label(baseGround, text="身長(cm)")
label2.pack()
text1 = tk.Entry(width=30)
text1.pack()
label3 = tk.Label(baseGround, text="体重(kg)")
label3.pack()
text2 = tk.Entry(width=30)
text2.pack()
# ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click)
btn.pack()

#表示
baseGround.mainloop()

import tkinter as tk
 
 
def btn_click():
    
 
    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()
 
    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('500x300')
 
    
    #GUIの画面タイトル
    baseGround_new_csv.title('結果')
 
    height = text1.get()
    #stringからfloatに
    height_f = float(height)
    
    weight = text2.get()
    #stringからfloatに
    weight_f = float(weight)
 
    
    height_m = height_f / 100
    result = weight_f / (height_m * height_m)
    result_str = str(round(result, 2))
 
    #BMI計算
    if result < 18.5:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で低体重(やせ型)です')
    elif result >= 18.5 and result < 25:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で普通体重です')
    elif result >= 25 and result < 30:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(1度)です')
    elif result >= 30 and result < 35:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(2度)です')
    elif result >= 35 and result < 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(3度)です')
    elif result >= 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str +'で肥満(4度)です')
    else:
        lbl_result = tk.Label(baseGround_new_csv, text='エラーです。')
          
    lbl_result.pack()
    
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()
 
baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('500x300')
#GUIの画面タイトル
baseGround.title('BMI計算')
label1 = tk.Label(baseGround, text="BMIの計算")
label1.pack()
label2 = tk.Label(baseGround, text="身長(cm)")
label2.pack()
text1 = tk.Entry(width=30)
text1.pack()
label3 = tk.Label(baseGround, text="体重(kg)")
label3.pack()
text2 = tk.Entry(width=30)
text2.pack()
# ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click)
btn.pack()
 
#表示
baseGround.mainloop()