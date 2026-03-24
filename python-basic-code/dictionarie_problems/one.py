import string
text='These are the bread-and-butter problems for Python intern interviews. Most interviewers pick 2-4 of these depending on the interview length. Would you like me to provide solutions for specific problems you want to practice?'

class dict_pblms:

    # Count word frequency in a sentence
    def count_words(self,text:str)->dict:
        trns=str.maketrans(string.punctuation,' '*len(string.punctuation))
        clean_text=text.translate(trns)

        words=clean_text.split()

        d={}
        for word in words:
            word=word.lower()
            d[word]=d.get(word,0)+1
        
        return d
    
    # Find the key with maximum value in a dictionary
    def popular_word(self,text:str)->None:
        d=self.count_words(text)
        popular_word=''
        maximum_value=0

        for key,value in d.items():
            if(value>maximum_value):

                maximum_value=value
                popular_word=key
        return popular_word
    
    # Merge two dictionaries
    def dict_merge(self,text1,text2):
        dict1=self.count_words(text1)
        dict2=self.count_words(text2)
        dict3={}
        for key,value in dict2.items():
            if (dict1.get(key)):
                dict1[key]=dict1.get(key,0)+1
            else:
                dict1[key]=value
        print(dict1)


    #Invert a dictionary (swap keys and values)
    def invert_dict(self,text):
        dict1=self.count_words(text)
        dict2={}
        for key,value in dict1.items():
            # dict2[value] = dict2.get(value, []) + [key]
            if (dict2.get(value)):
                d=dict2.get(value)
                d.append(key)
            else:   
              dict2.update({value:[key]})
        print(dict2)


dp=dict_pblms()
text2='Would you like me to provide actual code solutions for any of these the, or focus on a specific area where youd like more practice problems?'
# dp.dict_merge(text,text2)
dp.invert_dict(text)
