from collections import deque


class CountCash:

    def sorting_people(g_people_count):
        f_deposit_queue = []
        f_withdraw_queue = deque([])
        for iterating_element in range(g_people_count):
            f_choice = int(input("Enter your choice : "))
            if f_choice == 1:
                f_deposit_queue.append(iterating_element)
            elif f_choice == 2:
                f_withdraw_queue.append(iterating_element)
            else:
                print("Invalid Choice")
        return f_deposit_queue, f_withdraw_queue

    def bank_operations(f_deposit_queue, f_withdraw_queue,g_people_count):
        # global g_people_count
        g_total_cash = 1000000
        for iterating_element in range(g_people_count):
            if g_total_cash > 300000:
                f_deposit_queue.popleft()
                try:
                    f_amount = int(input("Enter your amount : "))
                    g_total_cash = g_total_cash + f_amount
                except:
                    pass
            else:
                f_withdraw_queue.popleft()
                try:
                    f_amount = int(input("Enter your amount : "))
                    g_total_cash = g_total_cash - f_amount
                except:
                    try:
                        while g_total_cash > 0:
                            f_amount = int(input("Enter your amount : "))
                            g_total_cash = g_total_cash - f_amount
                    except:
                        print("Closed!!!")
        return

    g_deposit_queue = []
    g_withdraw_queue = deque([])

    print("Options : "
          "1--Withdraw"
          "2--Deposit")
g_people_count = int(input("Enter number of people available :"))
cc = CountCash
g_deposit_queue,g_withdraw_queue = cc.sorting_people(g_people_count)
# print(g_deposit_queue)
# print(g_withdraw_queue)
cc.bank_operations(g_deposit_queue, g_withdraw_queue,g_people_count)








