
#関数
import time

def greeting():
    print("こんにちは")
    time.sleep(1)
    print("今日はいい天気ですね")
    time.sleep(1)
    print("さて今日は何をしましょう")

greeting()





#カタカナでもできる
def プリント():
    print("print")

プリント() 

















#while文
date = 10
while date == 30:
    date+=1

if date == 10:
    greeting()

elif date == 12:
    greeting()

elif date == 15:
    greeting()

number = 5

while (number < 10):  #10未満という条件を満たしているときは処理を行う
    number += 1
    print(number)
else:                 #10未満という条件を満たしてないときの処理
    number += 1
    print("まだ" + str(number) + "だよ～？")





















#while文
ans = input()
while ans != "はい" and "いいえ":  #これでは実行しない。if文と同じでandを書いたらその後を省略しがちだけど、その後のも条件式を書く。
                                  #例えば while ans != "はい" and ans != "いいえ"のように 
    print("処理A")



while ans != "はい" and ans != "いいえ": #これが正解。andの後も条件式を書く
    print("処理A")



















#+,-,+,/以外の演算子
print(2**3)        #掛け算のマーク*(アスタリスク)が二つでべき乗になる。今回は2の3乗なので2*2*2で8になる
print(13%5)        #剰余(A%B,AをBで割ったあまりを表す。例えば 13 & 5 = 3) 13/5は2あまり3なのであまりの3が出る
print(7//3)        #切り捨ての割り算(割り算の結果の小数点以下を切り捨てる。例えば 7 // 3 = 2) 7/3は2.33333・・・
                   #小数点以下を切り捨てて2が答えになる
#文字列の演算
print("hello" * 3)  #文字列の後に*が来たらその文字列を繰り返す
print("hello" + "world" * 3)  #これの実行結果はhelloworldworldworldなので*xの直前の文字列を繰り返す
aiueo = "hello" + " " + "world" + " "
print(aiueo * 3)   #既に連結させたものだとok.　*xの前の文字列が繰り返される→この場合*3の前はaiueo→aiueoには"hello world "が入っている
                   #なので"hello world "が3回繰り返される
                   #" "はスペース




















#ループ文
for i in range(5):  #iというのは繰り返し回数を格納する変数のこと。カウンタ変数という

    if i == 3:
        break  #もしiが3になったら処理を止める
        
    print(i)


for i in range(5):
    if i == 3:
        continue  #もしiが3になったら処理をスキップする
        
    print(i)



for i in range(3):
    for j in range(3):    #外側のiが0周目の時にjが1周して、次はiが2週目に入って、もう1回jが1周して、iが3週目に入ってjが1周して終わり
    
        print(i,j,sep="&")    #printの第一引数、第二引数をそれぞれi,jにして、sep引数をハイフンにすることで、iハイフンjと表示できる(ハイフン以外でもできる)ようするに

arr = [2,4,6,8,10]
sum = 0
for i in arr:  #さっきも言った通りiは繰り返し回数を格納する変数のこと。ここではarrというのを格納している。

    sum+=i    #ここではsum = sum + iで、iにはarrが格納されてるので2,4,6,8,10が順序出されて足し算される 

print(sum)   #まずはじめにarrは2なのでiに2を格納する。そしてsum + sum + iなのでsumに2がたされる。sumは最初に0と定義してるので答えは2になる。
               #次はarrが4なのでiに4を格納する。そして先程の計算でsumが2になったのでsum + iで2+4は6になる。それを続けると30になる


















#import A as B     ←importで持ってきたものは省略できる
import time as t

print("a")
t.sleep(1)
print("b")
