import random
import functools

QUESTION = '\033[95m'
NORMAL = '\033[0m'
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]


def task1():
    print(QUESTION)
    print("1. Define the id of next variables:\nint_a = 55\nstr_b = 'cursor'\nset_c = {1, 2, 3}\n"
          "lst_d = [1, 2, 3]\ndict_e = {'a': 1, 'b': 2, 'c': 3}")
    print(NORMAL)
    print('int_a id is: ', id(int_a))
    print('str_b id is: ', id(str_b))
    print('set_c id is: ', id(set_c))
    print('lst_d id is: ', id(lst_d))
    print('dict_e id is: ', id(dict_e))


def task2():
    print(QUESTION)
    print("2. Append 4 and 5 to the lst_d and define the id one more time.")
    print(NORMAL)
    print('lst_d was  ', lst_d)
    lst_d.extend([4, 5])
    print('Now lst_d is ', lst_d)
    print('lst_d id is: ', id(lst_d))


def task3():
    print(QUESTION)
    print("3. Define the type of each object from step 1.")
    print(NORMAL)
    print('Type of int_a: ', type(int_a))
    print('Type of str_b: ', type(str_b))
    print('Type of set_c: ', type(set_c))
    print('Type of lst_d: ', type(lst_d))
    print('Type of dict_e: ', type(dict_e))


def task4():
    print(QUESTION)
    print("4*. Check the type of the objects by using isinstance.")
    print(NORMAL)
    check = [int_a, str_b, set_c, lst_d, dict_e]
    types = [int, str, set, list, dict]
    for i in check:
        for j in types:
            if isinstance(i, j):
                print('Type of ', i, ' is ', j)


def task5():
    print(QUESTION)
    print("5. With .format and curly braces {}")
    print(NORMAL)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print('String became\n"Anna has {} apples and {} peaches."'.format(a, b))


def task6():
    print(QUESTION)
    print("6. By passing index numbers into the curly braces.")
    print(NORMAL)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print('String became\n"Anna has {1} apples and {0} peaches."'.format(2, 1))


def task7():
    print(QUESTION)
    print("7. By using keyword arguments into the curly braces.")
    print(NORMAL)
    a = random.randint(1, 100)
    p = random.randint(1, 100)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print('String became\n"Anna has {apples} apples and {peaches} peaches."'.format(apples=a, peaches=p))


def task8():
    print(QUESTION)
    print("8*. With indicators of field size (5 chars for the first and 3 for the second)")
    print(NORMAL)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print('String became\n"Anna has {0:5} apples and {1:3} peaches."'.format(5, 3))


def task9():
    print(QUESTION)
    print("9. With f-strings and variables")
    print(NORMAL)
    apples = random.randint(1, 100)
    peaches = random.randint(1, 100)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print(f'String became\n"Anna has {apples} apples and {peaches} peaches."')


def task10():
    print(QUESTION)
    print("10. With % operator")
    print(NORMAL)
    apples = random.randint(1, 100)
    peaches = random.randint(1, 100)
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print('String became\n"Anna has %d apples and %d peaches."' % (apples, peaches))


def task11():
    print(QUESTION)
    print("11*. With variable substitutions by name (hint: by using dict)")
    print(NORMAL)
    fruity_dict = {'apples': 3, 'peaches': 2}
    print('String was\n"Anna has ___ apples and ___ peaches."')
    print('String became\n"Anna has {apples} apples and {peaches} peaches."'.format(**fruity_dict))


def task12():
    print(QUESTION)
    print("12. Convert (1) to list comprehension")
    print(NORMAL)
    lst2 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
    print(lst2)


def task13():
    print(QUESTION)
    print("13. Convert (2) to regular for with if-else")
    print(NORMAL)
    list_comprehension = []
    for num in range(10):
        if num % 2 == 0:
            list_comprehension.append(num // 2)
        else:
            list_comprehension.append(num * 10)
    print(list_comprehension)


def task14():
    print(QUESTION)
    print("14. Convert (3) to dict comprehension.")
    print(NORMAL)
    d = {num: num**2 for num in range(1, 11) if num % 2 == 1}
    print(d)


def task15():
    print(QUESTION)
    print("15*. Convert (4) to dict comprehension.")
    print(NORMAL)
    d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
    print(d)


def task16():
    print(QUESTION)
    print("16. Convert (5) to regular for with if.")
    print(NORMAL)
    dict_comprehension = {}
    for x in range(10):
        if x ** 3 % 4 == 0:
            dict_comprehension[x] = x ** 3
    print(dict_comprehension)


def task17():
    print(QUESTION)
    print("17*. Convert (6) to regular for with if-else.")
    print(NORMAL)
    dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
    print(dict_comprehension)
    dict_comprehension = {}
    for x in range(10):
        if x ** 3 % 4 == 0:
            dict_comprehension[x] = x ** 3
        else:
            dict_comprehension[x] = x
    print(dict_comprehension)


def task18():
    print(QUESTION)
    print("18. Convert (7) to lambda function")
    print(NORMAL)
    foo = lambda x, y: x if x < y else y
    print("For x = 1 and y = 3 foo will be", foo(1, 3))


def task19():
    print(QUESTION)
    print("19*. Convert (8) to regular function")
    print(NORMAL)

    def foo(x, y, z):
        if y < x and x > 2:
            return z
        else:
            return y
    print("For x = 1, y = 3 and z = 5 foo will be", foo(1, 3, 5))


def task20():
    print(QUESTION)
    print("20. Sort lst_to_sort from min to max")
    print(NORMAL)
    print("Original array (lst_to_sort) is:\n"
          "[5, 18, 1, 24, 33, 15, 13, 55]\n"
          "Sorted array is:")
    print(sorted(lst_to_sort))


def task21():
    print(QUESTION)
    print("21. Sort lst_to_sort from max to min")
    print(NORMAL)
    print("Original array (lst_to_sort) is:\n"
          "[5, 18, 1, 24, 33, 15, 13, 55]\n"
          "Sorted array is:")
    print(sorted(lst_to_sort, reverse=True))


def task22():
    print(QUESTION)
    print("22. Use map and lambda to update the lst_to_sort by multiply each element by 2")
    print(NORMAL)
    print("Original array (lst_to_sort) is:\n"
          "[5, 18, 1, 24, 33, 15, 13, 55]\n"
          "Processed array is:")
    lst_to_print = list(map(lambda x: x * 2, lst_to_sort))
    print(lst_to_print)


def task23():
    print(QUESTION)
    print("23*. Raise each list number to the corresponding number on another list:")
    print("list_A = [2, 3, 4]\n"
          "list_B = [5, 6, 7]")
    print(NORMAL)
    lst_to_print = [list_A[i] + list_B[i] for i in range(len(list_A))]
    print("Sum =", lst_to_print)


def task24():
    print(QUESTION)
    print("24. Use reduce and lambda to compute the numbers of a lst_to_sort.")
    print(NORMAL)
    print("lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]\n"
          "Sum =", functools.reduce(lambda x, y: x + y, lst_to_sort))


def task25():
    print(QUESTION)
    print("25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.")
    print(NORMAL)
    lst_to_print = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
    print("lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]\n"
          "Filtered =", lst_to_print)


def task26():
    print(QUESTION)
    print("26. Considering the range of values: b = range(-10, 10),"
          "use the function filter to return only negative numbers.")
    print(NORMAL)
    lst_to_print = list(filter(lambda x: (x < 0), range(-10, 10)))
    print("Negatives =", lst_to_print)


def task27():
    print(QUESTION)
    print("27*. Using the filter function, find the values that are common to the two lists:\n"
          "list_1 = [1, 2, 3, 5, 7, 9]\n"
          "list_2 = [2, 3, 5, 6, 7, 8]")
    print(NORMAL)
    lst_to_print = list(filter(lambda x: (x in list_1), list_2))
    print("In common =", lst_to_print)


if __name__ == '__main__':
    while True:
        print('Enter a number of task you want to execute\n'
              'Print "exit" to exit')
        choice = input()
        if choice != 'exit':
            func = 'task' + choice + '()'
            try:
                eval(func)
            except NameError:
                print('That`s not a proper task!')
            print('-' * 20)
        else:
            exit()
