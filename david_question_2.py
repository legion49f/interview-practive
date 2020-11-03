# Do not code until you solve

# MAX_VALUE = 1000

# [0, 1 ,5, 8, 10]
# [0,1,2,3,4,5,6,7,8,9,10] => 2-4, 6-7, 9

# [
# [0, 1, 3, 8, 15] => 2 , 4-7, 9-14 , 16-1000

# 1 - 0 = 1   i=1
# 3 - 1 = 2   i=2
# 8 - 3 = 5   i=3
# 15 - 8 = 7  i=4

def output_rge(lst:int, next:int):
    if lst == next:
        print(f'{lst}')
    else:
        print( f'{lst}-{next-1}')


def missing_nums(ints_list:list, max_value:int): 
    map = dict(ints_list) # O(n)
    lst = int() 
    next = int()
    for idx in range(0, max_value): # o(m) 
        if idx not in map:
            if idx > lst:
                lst = idx   # lst =4
        if idx in map:
            next = idx
            output_rge(lst, next)

#  O(m + n) where M is max_value and n = len(list)
