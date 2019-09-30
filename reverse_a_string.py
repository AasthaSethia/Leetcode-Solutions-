class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list_word = s.split(' ')
        result = []
        for i in list_word:
            result.insert(0,i)
        final = str(' '.join(result))
        final = " ".join(final.split())
        return final
