class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        s_list =sorted([ch for ch in s])
        t_list = sorted([ch for ch in t])

        s_len = len(s_list)
        if s_len != len(t_list):
            print("not the same length")
            return False

        for i in range(s_len):
            if s_list[i] != t_list[i]:
                print(s_list[i] , t_list[i])
                return False
        return True
        