def calculate_staffing(total_revenue, num_hours_shift, dict_of_staff_and_costs):
    '''
    :param total_revenue: the total revenue that is expected over the course of the shift
    :param num_hours_shift: the number of hours that the shift is (float)
    :param dict_of_staff_and_costs: dictionary of all the positions and the money per position that is required

    :return: object with number of people required for each position
    '''

    from math import ceil

    # calculate the revenue per 30 minute shift

    number_30_min_intervals = num_hours_shift * 2
    avg_rev_in_30_min = total_revenue / number_30_min_intervals

    staff_count = {}

    # print('30 avg revenue %s' % avg_rev_in_30_min)
    for key in dict_of_staff_and_costs.keys():
        cost = dict_of_staff_and_costs[key]

        staff_count[key] = ceil(avg_rev_in_30_min/cost)

    return staff_count


if __name__ == '__main__':
    rev = 10000
    hrs = 9 - 4
    data = calculate_staffing(rev, hrs, {'expeditor': 300, 'host': 500, 'server': 200})
    print(data)
