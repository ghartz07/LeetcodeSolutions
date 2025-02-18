class Solution:
    # this solution works for when either only one of them are a subset of the other
    def isAnagram(self, s: str, t: str) -> bool:
        # two maps
        output1 = True
        output2 = True

        count_dict1 = {}
        count_dict2 = {}

        for letter in s:
            count_dict1[letter] = count_dict1.get(letter, 0) + 1   #get(keyname, a value to return if key doesn't exist)

        for letter in t:
            count_dict2[letter] = count_dict2.get(letter, 0) + 1   #get(keyname, a value to return if key doesn't exist)

        for (key1, val1) in count_dict1.items(): # Check if s is a subset of t
            if not (key1 in count_dict2 and val1 <= count_dict2[key1]):
                output1 = False
                
        for (key2, val2) in count_dict2.items(): # Check if t is a subset of s
            if not (key2 in count_dict1 and val2 <= count_dict1[key2]):
                output2 = False    

        if output1 == True and output2 == True:
            return True

        return False