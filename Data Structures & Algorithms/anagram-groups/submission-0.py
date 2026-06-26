class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        index = 0
        result = []
        for string in strs:
            found = False
            count_dict = {}
            for char in string:
                count_dict[char] = count_dict.get(char, 0) + 1
            for key, value in str_dict.items():  
                if value == count_dict: 
                    result[key].append(string)
                    found = True
                    break
            if not found:        
                str_dict[index] = count_dict
                result.append([string])
                index += 1
        return result    
                

        