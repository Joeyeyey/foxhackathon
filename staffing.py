
class staff():
    def __init__(self, host,server,expeditor):
        self.host = host
        self.server = server
        self.expeditor = expeditor


def calculate_staffing(total_revenue, num_hours_shift, host_cost, server_cost, expeditor_cost):
    '''
    :param total_revenue: the total revenue that is expected over the course of the shift
    :param num_hours_shift: the number of hours that the shift is (float)
    :param host_cost: the amount of money per 30 minutes that will be used for the host
    :param server_cost: the amount of money per 30 minute used for a server
    :param expeditor_cost:  the amount of money per 30 min for expiditor

    :return: object with number of people required for each position
    '''

    from math import ceil

    # calculate the revenue per 30 minute shift

    number_30_min_intervals = num_hours_shift * 2
    avg_rev_in_30_min = total_revenue / number_30_min_intervals

    print('30 avg revenue %s' % avg_rev_in_30_min)
    num_hosts = ceil(avg_rev_in_30_min / host_cost)
    num_server = ceil(avg_rev_in_30_min / server_cost)
    num_expeditor = ceil(avg_rev_in_30_min / expeditor_cost)

    print('number of hosts is %s' % num_hosts)

    staff_obj = staff(num_hosts, num_server, num_expeditor)

    return staff_obj


if __name__ == '__main__':
    rev = 10000
    hrs = 9 - 4
    h = 500
    s = 200
    e = 300
    data = calculate_staffing(rev, hrs, h,s,e)
    print(data.__dict__)
