import random
#print("ランダム数字を出力:",random.randint(1,20))
arr = [1,2,3,4,5]
a = random.choices(arr)
#print(a)
janken = ["ぐー","ちゅき","パー"]
#print(janken[2])
#print(random.randint(0,3))
#print(random.uniform(0,3))
print(random.uniform(janken)[0])