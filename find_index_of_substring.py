def find_index(source:str, target:str):
    ret_idx = 0
    count = 0
    for idx in range(len(source)):
        if source[idx] == target[0]:
            if len(target) == 1:
                return idx
            ret_idx = idx
            temp = idx + 1
            for char in target[1:]:
                if char == source[temp]:
                    temp+=1
                    count+=1
                else:
                    ret_idx = 0
                    break
                if count == len(target[1:]):
                    return ret_idx
    if ret_idx == 0:
        return -1