from datetime import datetime


def logger(func):
    def create_loggsfile(*args, **kwargs):
        date_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('loggsfile.txt', 'a', encoding='utf-8') as f:
            f.write(f'date:{date_time}; name:{func_name}; arguments:{args}, '
                    f'{kwargs}; result:{result}.\n')
        return result
    return create_loggsfile


def path_logger(path):
    def path_loggsfile(func):
        def create_loggsfile(*args, **kwargs):
            date_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            func_name = func.__name__
            result = func(*args, **kwargs)
            file = str(path) +'\loggsfile.txt'
            with open(file, 'a', encoding='utf-8') as f:
                f.write(f'date:{date_time}; name:{func_name}; arguments:{args},'
                        f' {kwargs}; result:{result}.\n')
            return result
        return create_loggsfile
    return path_loggsfile


@path_logger((r'C:\Users\m\Desktop\Projects'))
def range_1(stop):
    my_list = []
    for i in range(stop):
        my_list.append(i)
    return my_list


@logger
def range_2(start, stop, step):
    my_list = []
    for i in range(start, stop, step):
        my_list.append(i)
    return my_list


print(range_1(5))
print(range_2(1, 8, 2))