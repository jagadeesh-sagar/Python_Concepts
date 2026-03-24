import collections
class stringPatterns:

    # Find the first non-repeating character in a string
    def noDuplicate(self,text:str)->None:
        chars=[]
        for char in text:
            chars.append(char)
        for char in text:
          if(chars.count(char)==1):
              return char
          #faster
    def noDuplicates(self, text: str) -> str | None:
        if not text:
            return None

        # Step 1: Count character frequencies
        char_counts = collections.Counter(text)
        print(char_counts)

        # Step 2: Iterate through the string to find the first character with a count of 1
        for char in text:
            if char_counts[char] == 1:
                return char

        # Step 3: If no non-repeating character is found
        return None

    
sp=stringPatterns()
c=sp.noDuplicates(text='aagguuj')
print(c)

# common=collections.Counter('jaggu').most_common(2)
