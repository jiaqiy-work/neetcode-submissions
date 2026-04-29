class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for s in strs:
            key = tuple(sorted(s))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        for value in hashmap.values():
            res.append(value)
        return res