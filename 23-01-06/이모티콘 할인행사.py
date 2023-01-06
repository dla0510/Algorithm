import itertools


def solution(users, emoticons):
    l_u = len(users)
    l_e = len(emoticons)
    possible_sale_p = []
    for user in users:
        if not user[0] in possible_sale_p:
            possible_sale_p.append(user[0])

    possible_sale_p.sort()

    result = list(itertools.product([10,20,30,40], repeat=l_e))
    # print(result)

    max_join = 0
    max_total_amount = 0

    for sale_percentage in result:
        join = 0
        total_amount = 0

        for i in range(l_u):
            [target_percentage, target_amount] = users[i]
            amount = 0
            for j in range(l_e):
                if sale_percentage[j] >= target_percentage:
                    # if sale_percentage == (40,40,20,40):
                    #     print(f'현재 할인율과 구매하려는 할인율 {sale_percentage[j]}, {target_percentage}')
                    #     print(f'구매 가격 {emoticons[j] * sale_percentage[j]/100}')
                    amount += emoticons[j] * (100-sale_percentage[j])/100

            # if sale_percentage == (40,40,20,40):
            #     print('현재 이모티콘 구매 비용과 목표 비용 ', amount, target_amount)
            if amount >= target_amount:
                join += 1
            else:
                total_amount += amount

            # print(max_join, max_total_amount)
            # print(sale_percentage)
            # print(join, total_amount)
            # print('--------------------------------')

        if join>max_join or (join>=max_join and total_amount>max_total_amount):
            max_join = join
            max_total_amount = total_amount

    return [max_join, max_total_amount]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users1 = [[40, 10000], [25, 10000]]
    emoticons1 = [7000, 9000]


    users2 = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons2 = [1300, 1500, 1600, 4900]

    print(solution(users1, emoticons1))
    print(solution(users2, emoticons2))