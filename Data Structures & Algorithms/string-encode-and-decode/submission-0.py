class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        encoded = ''
        for i in strs:
            encoded+=i
            encoded+='.'
        encoded = str(n)+'.'+encoded
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        print(s)
        list_of_strs = s.split('.')
        print(list_of_strs)
        decoded = list_of_strs[1:-1]
        return decoded
