def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금 함수
    print("입금이 완료되었습니다. 잔액은, {}원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance,money): # 출금
    if balance >= money : # 출금 가능
        print("--출금이 완료되었습니다.--")
        print("잔액은 {}원입니다.".format(balance-money))
        return balance-money
    else :
        print("--출금이 완료되지 않았습니다.--")
        print("잔액은 {}원입니다.".format(balance))

def withdraw_night(balance,money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission # 튜플 형식


balance = 0 # 잔액
balance = deposit(balance,1000)
# print(balance)
# balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance,500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.". format(commission,balance))