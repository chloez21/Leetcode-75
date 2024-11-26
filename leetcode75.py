from typing import List

# Contains Duplicate
def hasDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Valid Anagram(**An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.)**
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
                    
        return True
    

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1 #ord() 是 "ordinal" 的缩写，意思是 "序数" 或 "顺序号"
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True



# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return 


# Group Anagrams
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = {} # key: tuple, value: list
    for s in strs: #"eat"
        count = [0] * 26 #[0,0,0,...0]
        for c in s:
            count[ord(c) - ord('a')] += 1 #[1, 0, 0, 0, ..., 0] 
        if tuple(count) not in ans:
            ans[tuple(count)] = [] 
        ans[tuple(count)].append(s) # ans={(1, 0, ..., 1): ["eat"]}
    return ans.values()


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())
