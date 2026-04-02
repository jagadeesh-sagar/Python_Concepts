'''
Group anagrams together -
 ["eat", "tea", "tan", "ate", "nat", "bat"] → 
 [["eat","tea","ate"], ["tan","nat"], ["bat"]]
'''

def anaragam(list1:list[str])->list[list[str]]:

    dict1={}

    for word in list1:
        key=''.join(sorted(word))

        if key in dict1:
            dict1.get(key).append(word)
        else:
            dict1[key]=[word]
    # for value in dict1.values():
    #     anaragams.append(value)

    return list(dict1.values())

print(anaragam(list1=["eat", "tea", "tan", "ate", "nat", "bat"]))