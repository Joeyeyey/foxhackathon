
def calc(start_string,  end_string):
    '''
    :param start_string: string in 24 hour clock format of the start of the shift
    :param end_string: string in 24 hour clock format of the end of the shift
    :return: float of the number of hours total (this will
    '''
    from datetime import datetime

    start_string= datetime.strptime(start_string, '%H:%M')
    end_string = datetime.strptime(end_string, '%H:%M')
    delta = end_string - start_string
    hour = delta.seconds / (60**2)
    return hour
