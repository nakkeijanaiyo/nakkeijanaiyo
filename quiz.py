#timeモジュール
import time

#ゲームの説明
print("これから連想ゲームを行い、合計ポイントで競います。正解したら1問につき2点もらえます。")
time.sleep(2.7)
print("答えをどうぞ！と言われたら答えを入力してください")
time.sleep(2)
print("連想ゲームとはヒントをもとに答えを導くゲームです。ヒントは4つ出します。")
time.sleep(3)
print("では初めます")


#合計点数を競うので最初のscoreを0にする
score = 0

#カウントダウン
time.sleep(2)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("START")
time.sleep(1.5)


#問題文　読みやすいように間隔を開ける                                      
print("・持ち運びが出来てサイズは小さい")
time.sleep(2.2)
print("・なくなったら生活できない人がいる")
time.sleep(2.5)
print("・耳にかけて使用する")
time.sleep(2.2)
print("・プラスチックとガラスで出来ている")
time.sleep(1)
print("答えをどうぞ！")


#答えansをinputから受け取る
ans = input()

#答え合わせ
if ans == "めがね":
    print("正解！次！")
    score+=2    #正解してたら2Pあげる
    time.sleep(1)
elif ans == "眼鏡":
    print("正解！次！")
    score +=2
    time.sleep(1)
elif ans == "メガネ":
    print("正解！次！")
    score+=2
    time.sleep(1)
else:
    print("不正解...次！")
    time.sleep(1)


#問題文2
print("・夏と冬")
time.sleep(2.2)
print("・4年に一度")
time.sleep(2.2)
print("・世界的")
time.sleep(2.2)
print("・スポーツ")
time.sleep(0.8)
print("答えをどうぞ！")


#答えansをinputから受け取る
ans = input()

#答えあわせ2
if ans == "オリンピック":
    print("正解！次！")
    score+=2
    time.sleep(1)
elif ans == "五輪":
    print("正解！次！")
    score+=2
    time.sleep(1)
elif ans == "おりんぴっく":
    print("正解！次！")
    score+=2
    time.sleep(1)
else:
    print("不正解...次！")
    time.sleep(1)


#問題文3
print("・葛飾北斎も描いたもの")
time.sleep(2.2)
print("・銭湯の背景画にもなっている")
time.sleep(2.2)
print("・登った人もいる")
time.sleep(2.2)
print("・日本一")
time.sleep(0.8)
print("答えをどうぞ！")


#答えansをinputから受け取る
ans = input()

#答えあわせ3
if ans == "富士山":
    print("正解！次！")
    score+=2
    time.sleep(1)
elif ans == "ふじさん":
    print("正解！次！")
    score+=2
    time.sleep(1)
else:
    print("不正解...次！")
    time.sleep(1)


#問題文4
print("・料理にはかかせないもの")
time.sleep(2.2)
print("・木とプラスチック")
time.sleep(2.2)
print("・食べられない")
time.sleep(2.2)
print("・食材を切るのにかかせないもの")
time.sleep(0.8)
print("答えをどうぞ！")


#答えansをinputから受け取る
ans = input()

#答えあわせ4
if ans == "まな板":
    print("正解！次！")
    score+=2
    time.sleep(1)
elif ans == "まないた":
    print("正解！次！")
    score+=2
    time.sleep(1)
else:
    print("不正解...次！")
    time.sleep(1)


#問題文5
print("・強烈な匂い")
time.sleep(2.2)
print("・好きな人は好き")
time.sleep(2.2)
print("・スーパーで手に入る")
time.sleep(2.2)
print("・ネバネバしている")
time.sleep(0.8)
print("・答えをどうぞ！")


#答えansをinputから受け取る
ans = input()

#答えあわせ5
if ans == "納豆":
    print("正解！これで終わりだよ！")
    score+=2
    time.sleep(2.5)

elif ans == "なっとう":
    print("正解！これで終わりだよ！")
    score+=2
    time.sleep(2.5)

else:
    print("不正解...これで終わりだよ！")
    time.sleep(2.5)


#合計点の表示
if score >= 6:
    print("あなたの合計点数は～？")
    time.sleep(2.5)
    print(str(score) + "点です！！")
    print("ええ調子やの！")
else:
    print("あなたの合計点数は～？")
    time.sleep(2.5)
    print(str(score) + "点です...")
    print('"次も頑張ろな...')