
# 변수 만들기

my_money = 10000 # 내 돈

gum_price = 700 # 개껌 가격

taku_food = 0 # 타쿠 개껌 개수







# 타쿠 간식을 살 수 있는 한 모두 산다





# i 인자를 0으로 생성하는 대신

위에 생성한 변수 사용해

가진 돈 > 간식 가격

이라면

돈 마이너스 / 간식 획득





# 내 용돈이 개껌 가격보다 클 때



1. 돈을 낸다

2. 간식을 하나 획득한다의

반복







while my_money > taku_food :

print ( '보유 개껌 : { } 개, 남은 돈 : { }원'.format(taku_food, my_money))



# 타쿠 간식 하나 획득 식 = 내 돈 - 개껌 가격 / 그리고 타쿠 간식 1개 증가

my_money = my_money - gum_price

taku_food = taku_food + 1

