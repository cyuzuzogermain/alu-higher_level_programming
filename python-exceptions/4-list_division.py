#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            if not all(isinstance(n, (int, float)) for n in (a, b)):
                print("wrong type")
                result = 0
            else:
                result = a / b
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)

    return result_list
