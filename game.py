#タイムモジュール
import time
from typing import SupportsComplex


#クイズの合計点数
score = 0

#ルール説明
print("これから連想ゲームを行います")
time.sleep(1.8)
print("連想ゲームとは、ヒントに基づいて答えを導くゲームです。")
time.sleep(3)
print("合計点数が満点の人は賞品があります")
time.sleep(3)
print("ヒントは4個だされます。「答えをどうぞ」と言われたら答えを入力してください")
time.sleep(4)
print("では始めます")
time.sleep(1.3)

#カウントダウン
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
time.sleep(1)

#1問目
print("第1問！")
time.sleep(0.8)
print("・持ち運びが出来てサイズが小さい")
time.sleep(2)
print("・なくなったら生活できない人がいる")
time.sleep(2)
print("・耳にかけて使用する")
time.sleep(1.8)
print("・プラスチックとガラスで出来ている")
time.sleep(2)
print("・答えをどうぞ！")

#答えansをinput関数で入力する
ans = input()

#答え合わせ
if ans == "眼鏡":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "めがね":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "メガネ":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
else:
    print("不正解...")
    time.sleep(1)
    print("次！")
    time.sleep(1)

#2問目
print("第2問！")
time.sleep(1)
print("・夏と冬")
time.sleep(1.4)
print("・4年に1度")
time.sleep(1.4)
print("・世界的")
time.sleep(1.4)
print("・スポーツ")
time.sleep(1.2)
print("・答えをどうぞ！")

#ansをinput関数で入力する
ans = input()

#答え合わせ
if ans == "オリンピック":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "おりんぴっく":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "五輪":
    score +=2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
else:
    print("不正解...")
    time.sleep(1)
    print("次！")
    time.sleep(1)

#3問目
print("第3問！")
time.sleep(1)
print("・強烈な匂い")
time.sleep(1.5)
print("・好きな人は好き")
time.sleep(1.5)
print("・スーパーで手に入る")
time.sleep(2)
print("・ネバネバしている")
time.sleep(2)
print("答えをどうぞ！")

#ansをinput関数で入力
ans = input()

#答え合わせ
if ans == "納豆":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "なっとう":
    score +=2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
else:
    print("不正解...")
    time.sleep(1)
    print("次！")
    time.sleep(1)

#4問目
print("第4問！")
time.sleep(1)
print("・料理には欠かせないもの")
time.sleep(2)
print("・木とプラスチック")
time.sleep(2)
print("・食べられない")
time.sleep(1.5)
print("・食材を切るのに欠かせないもの")
time.sleep(2.5)
print("答えをどうぞ！")

#ansをinput関数で入力する
ans = input()

if ans == "まな板":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
elif ans == "まな板":
    score += 2
    print("正解！")
    time.sleep(1)
    print("次！")
    time.sleep(1)
else:
    print("不正解...")
    time.sleep(1)
    print("次！")

#4問目
print("第5問！")
time.sleep(1)
print("・オムライスとナポリタン")
time.sleep(1.5)
print("・明治時代にアメリカから伝わった")
time.sleep(1.8)
print("・トマト")
time.sleep(1)
print("・調味料")
time.sleep(1.5)
print("答えをどうぞ！")

#ansをinput関数で入力する
ans = input()

#答え合わせ
if ans == "ケチャップ":
    score += 2
    print("正解！")
    time.sleep(1)
    print("これでおしまいです")
    time.sleep(2)
elif ans == "けちゃっぷ":
    score += 2
    print("正解！")
    time.sleep(1)
    print("これでおしまいです")
    time.sleep(2)
else:
    print("不正解...")
    time.sleep(1)
    print("これでおしまいです")
    time.sleep(2)

#結果発表
print("あなたの合計点数は～")
time.sleep(2)
if score <= 5:
    print(str(score) + "点です...")
elif score >= 5 and score <= 9:
    print(str(score) + "点です！")
else:
    print(str(score) + "点で～～～す！！！")
    time.sleep(0.5)
    print("満点おめでとう！！")

#商品受取る時に電話する番号
phone_num = 123456789

#満点の人の賞品
if score == 10:
    print("あなたは合計点数が満点なので好きなジュースを3本それぞれの種類の間に\"半角の\",(コンマ)を入れて入力してください")
    time.sleep(3)
    print("例：A,B,C")
    #好きなジュースを追加
    like_juice = input()

print("あなたはこのジュースが毎月ほしいですか？")
print("毎月欲しいなら「はい」を欲しくないなら「いいえ」を入力してください")
ans = input()

#答えが「はい」でも「いいえ」でもなかった場合の動作
while ans != "はい" and ans != "いいえ":
    print("それは答えとして認められません")
    ans = input()


#答えが「はい」だった場合の動作
if ans == "はい":
    print("わかりました。では、お電話で利用者番号を伝えてください")
    time.sleep(1.5)
    print("電話番号は")
    time.sleep(1)
    print(phone_num)
    time.sleep(0.2)
    print("です！ではお待ちしております！")

#答えが「いいえ」だった場合の動作
elif ans == "いいえ":
    print("わかりました")
    time.sleep(1)
    print("ご協力ありがとうございました")
