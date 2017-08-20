def share_price(arr):
    #initialize as difference between first two days
    max_profit = arr[1][1] - arr[0][1]
    day_range = [arr[0][1],arr[1][1]]
    days = [0,1]
    cur_profit = max_profit
    cur_range = day_range
    cur_days = [0,1]
    idx = 1
    for day_el in arr[2:]:
        idx += 1
        #if we should just extend the range
        if (day_el[0] - cur_range[0]) > max_profit & (cur_range[1] - cur_range[0]) > 0:
            day_range = [cur_range[0],day_el[0]]
            days = [cur_days[0],idx]
        #if we should replace the range
        elif day_el[0]-cur_range[1] > max_profit:
            day_range = [cur_range[0],day_el[0]]

            days = [cur_days[0],idx]
        elif (day_el[0]-cur_range[1]) > 0 & (cur_range[1]-cur_range[0]) > 0:
            cur_range[1] = day_el[0]
            cur_days[1] = idx
        elif (day_el[0]-cur_range[1]) > 0:
            cur_range = [cur_range[1],day_el[0]]
            cur_days = [cur_days[1],idx]
        else:
            cur_range = [day_el[0],day_el[0]]
            cur_days = [idx,idx]
    return days

print(share_price([[0,1,2],[-1,2,3],[-3,0,1],[2,5,7],[-10,-5,10],[5,10,15]]))
