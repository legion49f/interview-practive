
def in_range_helper(lesser:int, greater:int, x:int):
	if x >= lesser or x <= greater:
		return True
	return False

def find_index(mylist, myint:int):
    min, max, idx = 0, len(mylist) - 1, len(mylist) // 2
    while( in_range_helper(mylist[min], mylist[max], myint) ):
        idx = (min + max) // 2
        if min == idx or max == idx:
                break
        if myint == mylist[idx]:
            return idx
        elif myint > mylist[idx]:
            min = idx
        elif myint < mylist[idx]:
            max = idx
            
def freq_count(mylist, myint:int) -> int:
    count = 0
    idx = find_index(mylist, myint)
    if idx is None:
        # print('idx is None:')
        return count
    # print('idx is":', idx)
    left_idx = right_idx = idx
    while (left_idx >= 0 and mylist[right_idx] == myint): 
        count += 1
        left_idx-=1
    while (right_idx < len(mylist)-1 and mylist[right_idx] == myint): 
        count += 1
        right_idx+=1
    return count

if __name__ == "__main__":
    #        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 
    list1 = [1,1,1,6,6,6,6,6,7,7,7,7,7,9,9,9,9] # myint= 7
    list2 = [1,1,1,1,1,1,1,1,1,1,1,1,1] # myint = 1
    list3 = [1,1,1,1,1,1,1,1,4,5,6,7,8] # myint = 1
    list4 = [-1,-1,-1,-1,-1,-1,-1,-1,-4,-5,-6,-7,-8] # myint = 1
    list5 = [1,1,1,6,6,6,6,6,7,7,7,7,7,9,9,9,9] # myint= 7
    list6 = [1,5,5,6,6,6,6,6,7,7,7,7,7,9,9,9,9] # myint= 7
    list7 = [1,1,1,6,6,6,6,6,7,7,7,7,7,9,9,9,12] # myint= 7
    print('list1:', freq_count(list1, 5))
    print('list2:',freq_count(list2, 1))
    print('list3:',freq_count(list3, 4))
    print('list4:',freq_count(list4, -1))