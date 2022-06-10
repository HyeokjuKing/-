
drink_list2 = {'물': 20, '레몬워터': 20, '옥수수 수염차': 20, '콘트라베이스 커피': 20, '트레비': 20,
                              '밀키스': 20, '펩시': 20, '핫식스': 20, '칠성사이다': 20, '코코 망고맛': 20, '립톤 아이스티': 20,
                              '트로피카나 스파클링 사과맛': 20, '트로피카나 스파클링 포도맛': 20, '가나': 20,
                              '레쓰비': 20, '카타타 라떼': 20, '레쓰비 커피타임': 20, '게토레이': 20, '코코 포도맛': 20,
                              '식혜': 20}                        # 음료 종류 및 재고
change_list = {'1000원': 50, '500원': 100, '100원': 100} # 동전 종류 및 재고



#위의 변수 및 딕셔너리는 변환가능한 것

class main():
    def __init__(self):
       self.drink_list = {'물' :'600원', '레몬워터': '1500원', '옥수수 수염차': '1300원', '콘트라베이스 커피': '2000원', '트레비': '1000원',
                             '밀키스': '800원', '펩시': '800원', '핫식스': '1000원', '칠성사이다': '1000원', '코코 망고맛': '1000원',
                             '립톤 아이스티': '1000원',
                             '트로피카나 스파클링 사과맛': '1000원', '트로피카나 스파클링 포도맛': '1000원', '가나': '600원',
                             '레쓰비': '600원', '카타타 라떼': '1000원', '레쓰비 커피타임': '1000원', '게토레이': '800원', '코코 포도맛': '800원',
                             '식혜': '800원'}                       # 음료 종류 및 가격


       self.count_1000 = 0   # 거스름돈 변수
       self.count_500 = 0
       self.count_100 = 0

       self.change_data = 0  # 거스름돈을 재사용할 때 사용하는 변수

    def manager(self):                 #관리자 모드
          while 1:
            tool = str(input("어떤 기능을 이용하시겠습니까?\n"))
            if tool == "음료재고확인":
                for key, value in drink_list2.items():
                    print(key, value, '개', end=' ')
                print('\n')
                return self.manager()

            elif tool == "음료재고보충":
                drink_add_name = str(input("음료의 이름은?"))
                drink_add_count = int(input("음료 개수는?"))
                drink_list2[drink_add_name] += drink_add_count      #음료재고보충
                for key, value in drink_list2.items():
                    print(key, value, '개', end=' ')
                print('\n')
                return self.manager()

            elif tool == "잔돈재고확인":
                for key, value in change_list.items():
                    print(key, value, '개', end=' ')
                print('\n')
                return self.manager()

            elif tool == "잔돈재고보충":
                money_add_name = str(input("잔돈의 종류는?"))
                money_add_count = int(input("잔돈 개수는?"))
                change_list[money_add_name] += money_add_count     #잔돈재고보충
                for key, value in change_list.items():
                    print(key, value, '개', end=' ')
                print('\n')
                return self.manager()

            else:
                return start()       #다시 처음으로


    def consumer(self):         # 소비자 모드
          while 1:
            print(self.drink_list)
            money = int(input("돈을 투입하세요: "))
            money += self.change_data
            drink_select = str(input("음료를 선택하세요: "))
            drink_cost = int(self.drink_list[drink_select].strip('원'))
            drink_count = drink_list2[drink_select]

            if drink_count == 0:               #재고가 없을 때
                print("재고가 없습니다.")
                return self.consumer()         #다시 돈 투입하는 곳으로

            elif drink_cost > money:           #사용자가 넣은 금액보다 음료의 금액이 클 때
                print("금액이 부족합니다.")
                return self.consumer()         #다시 돈 투입하는 곳으로

            else:                              #음료을 정상적으로 구매할 수 있을 때
                self.change_data = money - drink_cost
                self.change(self.change_data)
                ask_reuse = str(input("거스름돈을 반환하시겠습니까?\n"))  # 거스름돈을 재사용할것인지 질문
                if (ask_reuse == "네"):  # 거스름돈 반환
                    drink_list2[drink_select] -= 1
                    change_list['1000원'] -= self.count_1000  # 잔돈재고 제거하기
                    change_list['500원'] -= self.count_500
                    change_list['100원'] -= self.count_100
                    break       #구매완료

                elif (ask_reuse == "아니오"):  # 거스름돈 재사용
                    drink_list2[drink_select] -= 1
                    continue    #다시 돈 투입하는 곳으로


    def change(self, data):       # 거스름돈 계산 함수

        self.change_data = data        #거스름돈을 변수에 잠시 저장
        self.count_1000 = int(data / 1000)         #거스름돈 계산
        data = data % 1000
        self.count_500 = int(data / 500)
        data = data % 500
        self.count_100 = int(data / 100)

        if(change_list['1000원'] < self.count_1000):     # 만약 1000원짜리 잔돈이 부족한 경우
            self.count_500 += self.count_1000 * 2         # 500원짜리 잔돈으로 대체

        if(change_list['500원'] < self.count_500):       # 만약 500원짜리 잔돈이 부족한 경우
            self.count_100 += self.count_500 * 5          # 100원짜리 잔돈으로 대체

        if(change_list['100원'] < self.count_100):       # 만약 100원짜리 잔돈이 부족한 경우
            print('자판기의 잔돈이 부족합니다. 다음에 다시 이용해 주세요.')
            exit()          #프로그램 종료하기

        else:
            print("음료를 구입했습니다.\n")
            print("거스름돈은 %d원 %d장" % (1000, self.count_1000),
                  "%d원 %d개" % (500, self.count_500), "%d원 %d개\n" % (100, self.count_100))
            print("총", self.change_data, "원 입니다")     #거스름돈 저장했던 변수 출력


def start():      #시작
    while 1:
        A = main()
        key = str(input("아무키나 눌러 시작하십시오.\n"))
        if key == "관리자":
            A.manager()         #관리자 모드로
            continue
        elif key == "종료" :
            exit()              #프로그램 종료
        else :
            A.consumer()        #소비자 모드로
            continue


start()         #프로그램 시작
