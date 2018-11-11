import json
from shift_length import calc

class parsed_data():
    def __init__(self, revenue, hours, worker_dictionary):
        self.revenue = revenue
        self.hours = hours
        self.worker_dictionary = worker_dictionary



def parser(input_json):
    '''
    :param input_json: a json file that is to be parsed
    :return: an object containing all the information about the shift
    '''
    base_staff = input_json['staffTypes']
    worker_dictionary = {}
    for worker_type in base_staff:
        rev = base_staff[worker_type]['revenue']
        worker_dictionary[worker_type] = rev

    revenue = input_json['revenueGoal']
    shift_start = input_json['shiftStart']
    shift_end = input_json['shiftEnd']

    hours = calc(shift_start, shift_end)

    obj = parsed_data(revenue, hours, worker_dictionary)

    return obj





if __name__ == '__main__':
    with open('original_default.json', 'r') as f:
        data = json.load(f)
        import pprint
        pprint.pprint(data)
    obj = parser(data)

    import pprint

    pprint.pprint(obj.__dict__)
