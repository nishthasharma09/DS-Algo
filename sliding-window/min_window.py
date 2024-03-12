def minWindow(s, t):
    left, right = 0 , 0
    dict_t = make_dict(t)
    min_window = ""
    while right <= len(s):
        temp = s[left:right]
        if len(s[left:right]) >= len(t):
            dict_s = make_dict(s[left:right], dict_t)
            if compare_dictionaries(dict_s, dict_t):
                while compare_dictionaries(make_dict(s[left+1:right]), dict_t):
                    left += 1
                if min_window == '':
                    min_window = s[left:right]
                else:
                    if len(min_window) > len(s[left:right]):
                        min_window = s[left:right]
                left += 1
        right += 1
    print(min_window)

def compare_dictionaries(dict1, dict2):
    if len(dict1) < len(dict2):
        return False
    
    for key in dict2:
        if key not in dict1 or dict1[key] < dict2[key]:
            return False
    
    return True


def make_dict(string, dict_t={}):
    str_dict = {}
    for s in string:
        if s in str_dict:
            str_dict[s] = str_dict[s] +1
        else:
            str_dict[s] = 1
    return str_dict

minWindow("a", 'aa')