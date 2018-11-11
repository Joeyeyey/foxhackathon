import json
from shift_length import calc

class shift_data():
    def __init__(self, revenue, shift_start, shift_end, host,server,expeditor):
        self.host_expected = host
        self.server_expected = server
        self.expeditor_expected = expeditor

        self.revenue = revenue

        self.shift_time = calc(shift_start, shift_end)



def parser(input_json):
    '''
    :param input_json: a json file that is to be parsed
    :return: an object containing all the information about the shift
    '''
    base_staff = input_json['staffTypes']

    host = base_staff['host']['revenue']
    server = base_staff['server']['revenue']
    expeditor = base_staff['expeditor']['revenue']

    revenue = input_json['revenueGoal']
    shift_start = input_json['shiftStart']
    shift_end = input_json['shiftEnd']

    obj = shift_data(revenue, shift_start, shift_end, host,server,expeditor)

    return obj




if __name__ == '__main__':
    with open('original_default.json', 'r') as f:
        data = json.load(f)
        import pprint
        pprint.pprint(data)
    obj = parser(data)

    import pprint

    pprint.pprint(obj.__dict__)
