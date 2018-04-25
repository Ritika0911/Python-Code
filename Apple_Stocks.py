def get_max_profit_1(s_p_y):
    max_profit = 0

    for outer_time in xrange(len(s_p_y)):
        for inner_time in xrange(len(s_p_y)):
            earlier_time = min(outer_time,inner_time)
            later_time = max(outer_time,inner_time)
            
            earlier_price = s_p_y[earlier_time]
            later_price = s_p_y[later_time]

            potential_profit = later_price - earlier_price

            max_profit = max(max_profit, potential_profit)

    return max_profit

def get_max_profit_2(s_p_y):
    max_profit = 0

    for earlier_time, earlier_price in enumerate(s_p_y):
        for later_time in xrange(earlier_time+1, len(s_p_y)):
            later_price = s_p_y[later_time]

            potential_profit = later_price - earlier_price
            max_profit = max(max_profit, potential_profit)

    return max_profit

def get_max_profit_3(s_p_y):
    min_price = s_p_y[0]
    max_profit = 0

    for current_price in s_p_y:
        min_price = min(min_price, current_price)
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)

    return max_profit

def get_max_profit_4(s_p_y):
    if len(s_p_y)<2:
        raise ValueError('etting a profit requires atleast 2 prices')

    min_price = s_p_y[0]
    max_profit = s_p_y[1] - s_p_y[0]
    for current_time in xrange(1,len(s_p_y)):
        current_price = s_p_y[current_time]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit

if __name__ == '__main__':
    s_p_y = [10, 7, 5, 8, 11, 9]
    print get_max_profit_1(s_p_y)
    print get_max_profit_2(s_p_y)
    print get_max_profit_3(s_p_y)
    print get_max_profit_4(s_p_y)
    
    
