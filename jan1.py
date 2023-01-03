class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split()
        k, v, p = Counter(pattern), Counter(ls), Counter(zip(pattern, ls))
        return len(k) == len(v) == len(p) and len(pattern) == len(ls)