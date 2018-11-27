from collections import deque


class CountCash:

    def sorting_people(self, f_people_count):
        f_people_queue = deque([])
        for iterating_element in range(f_people_count):
            f_choice = int(input("Enter your choice : "))
            if f_choice == 1:
                f_people_queue.append(1)
            elif f_choice == 2:
                f_people_queue.append(2)
            else:
                print("Invalid Choice")
        return f_people_queue

    def bank_operations(self,  g_people_queue,people_count):
        f_people_queue = deque(g_people_queue)


        g_total_cash = 10000000
        print(f_people_queue)

        for iterating_element in range(people_count):
            if f_people_queue[iterating_element] == 1:
                # if g_total_cash > 100000:
                    try:
                        print("1 -- ", f_people_queue)
                        f_people_queue.popleft()
                        print("2--", f_people_queue)
                        f_amount = int(input("Enter your amount : "))
                        g_total_cash = g_total_cash + f_amount
                        print("Remaining = ", g_total_cash)
                    except IndexError:
                        print("Pass")
                        pass

            elif f_people_queue[iterating_element] == 2:
                try:
                    f_people_queue.popleft()
                    f_amount = int(input("Enter your amount : "))
                    g_total_cash = g_total_cash - f_amount
                    print("Remaining = ", g_total_cash)

                except IndexError:
                    # try:
                    #     while g_total_cash > 0:
                    #         f_amount = int(input("Enter your amount : "))
                    #         g_total_cash = g_total_cash - f_amount
                    #         print("Remaining = ", g_total_cash)
                    #
                    # except IndexError:
                        print("Closed!!!")
        return

    g_people_queue = deque([])


    print("Options : "
          "1--Withdraw"
          "2--Deposit")


g_people_count = int(input("Enter number of people available :"))
cc = CountCash()
g_people_queue = cc.sorting_people(g_people_count)
cc.bank_operations(g_people_queue,g_people_count)








