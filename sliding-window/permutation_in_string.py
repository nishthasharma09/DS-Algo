def checkInclusion(s1: str, s2: str): # fixed window question
    length = len(s1)
    result = False
    for i in range(0, len(s2) - length+1):
        print(f"{make_dict(s2[i:i+length])} == {make_dict(s1)}")
        if make_dict(s2[i:i+length]) == make_dict(s1):
            result = True
    print(result)

def make_dict(string):
    str_dict = {}
    for s in string:
        if s in str_dict:
            str_dict[s] = str_dict[s] +1
        else:
            str_dict[s] = 1
    return str_dict

checkInclusion("ab", "eidbaoo")