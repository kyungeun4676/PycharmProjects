import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0
    max_heap = []

    while stock < k:
        for data_index in range(current_day_index, len(dates)):
            print(data_index, dates[data_index], stock, supplies[data_index])
            if dates[data_index] <= stock:
                heapq.heappush(max_heap, -supplies[data_index])
            else:
                current_day_index = data_index
                break

        answer += 1
        stock += -heapq.heappop(max_heap)
        print("stock is", stock)
        return answer
    # 풀어보세요!
    return


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))