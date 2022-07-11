class Solution:
    '''
    For each str, convert it to a frequency list freq where freq[0] = # of 'a's in str, freq[1] = # of 'b's in str, and so on. 
    Use a hash table to associate each frequency list to the group of strings that convert to that list (anagrams). 
    Time complexity: O(n(k+26)) = O(nk), Space complexity: O(n(k+26)) = O(nk) where n = # of strings and k = max length of a string. 
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq2Strs = {}
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch)-ord('a')] += 1
        
            freq = tuple(freq) # dictionary keys must be immutable
            if freq not in freq2Strs:
                freq2Strs[freq] = [s]
            else:
                freq2Strs[freq].append(s)
        return list(freq2Strs.values())