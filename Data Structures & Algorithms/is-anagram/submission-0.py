class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] in hashmap1:
                hashmap1[s[i]] += 1
            else:
                hashmap1[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hashmap2:
                hashmap2[t[i]] += 1
            else:
                hashmap2[t[i]] = 1
        
        if hashmap1 == hashmap2:
            return True
        
        return False