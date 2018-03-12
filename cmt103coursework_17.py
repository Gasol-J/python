##CMT103 COURSEWORK 2017/18 ###
###############################
##You need to implet the following methods:
##
##Task 1
##readnumbers()  [2 marks]
##isPrime()    [5 marks]
##
##Task 2
##readsequences()  [2 marks] 
##longest_common_string() [6 marks]
##
##Task 3
##get_words() [4 marks]
##sort_tuples() [4 marks]
##get_top_10() [7 marks]
################################


###################################################
#Task 1: Check if a Given Number is a Prim Number:#
###################################################
def readnumbers(file_name): 
    
    f= open(file_name,'r')
    num = f.read().split(',')
    for i in range(len(num)):
        num[i]=int(num[i].strip(' '))


    # print('Numbers:', num,'\n')
    return num

def isPrime(nums):
        
    if(nums>1):
        for i in range(2,nums):
            if (nums % i)==0:
                return 0
                
        else:
            return 1
    
    
    
  
# readnumbers('readnumber.txt')

############################################ 
#Task 2: Find the longest common substring #
#       between two strings:               #
############################################
def readsequences(file_name): 
   
    f = open(file_name,'r')
    lines = f.readlines()
    str1= lines[0].strip("\n\r")
    str2 = lines[1]
    list1 = (str1,str2)
    tup = tuple(list1)
    return tup

    
def longest_common_string(st1, st2): 
    m=0
    n=len(st1)
    st3=[]
    b=0
    while(m<n):
        i=n-m
        while(i>=0):
            st3.append(st1[m:m+i])
            i-=1
        m+=1
 
    for x in st3:
        a=0
        if x in st2:
            a=len(x)
            c=st3.index(x)
        if a > b:
            b=a
            d=c
 
    if b>0:
        commonst= st3[d]
        return commonst
     

    

######################################
#Task 3: Get Top 10 ly-Words:        #
######################################
def get_words(file_name): 
    '''
    Input: the text file of a fiction
    Output: a list of all words that have occured in the file.
    '''
    import string
    import re
    word_count = 0
    lyword_count = 0
    lywordlist=[]
    b='ly'
    c='--'
    r='[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    f = open('sense_and_sensitivity.txt','r')
    word0 = f.read().split()
    word = str(word0)
    word1 = re.sub(r,'',word)
    word2 = word1.lower()
    wordlist = word2.split()
    
    words = wordlist
    return words

def get_dic(words): 
    '''
    Input: a list of words
    Return: a dic of ly-words and its number of occurrences
    '''
    lywordlist=[]
    b='ly'
    for item in words:
        if item[-2:]==b:
            lywordlist.append(item)

    dic ={}
    for i in lywordlist:
        if lywordlist.count(i)>=1:
            dic[i]=lywordlist.count(i)

    return dic
    

def get_top_10(dic): 
    '''
    Input: a dic of ly-words and its number of occurrences
    Return: a sorted list of top 10 two-element tuples.
    '''
    list1=[]
    i = 0
    while i<10:
        lymax1 = max(dic,key=dic.get)
        list1.append((lymax1,dic[lymax1]))
        del dic[lymax1]
        i+=1
    return list1
    



####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################


import sys
if __name__ == '__main__':
    #Take care of the console inputs
    if len(sys.argv)<=1:
        sys.argv = ['', "numbers.txt", "sequences.txt", "sense_and_sensitivity.txt"]
        
   
    stars = '*'*40
    print(stars)
    print("Testing Task 1 --- Is It a Prime?")
    print(stars)

    #Task 1-a
    try:
        nums = readnumbers(sys.argv[1])
        if not nums:
            print("readnumbers() returns None.")
        else:
            print("Numbers: ", nums)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    #Task 1-b
    try:
        if not nums: #Task 1-a has not been implemented
            print("isPrime() skipped....")
        else:    
            for num in nums:
                result = isPrime(num)
                if result==None:
                    print("isPrime() returns None.")
                    break
                print("{} : {}".format(num, "Prime" if result else "Not Prime"))
                    
    except Exception as e:
        print("Error (isPrime()):", e)

    #testing task 2
    print("\n\n"+stars)
    print("Testing Task 2 --- Longest Common Substring")
    print(stars)

    #Task 2-a
    try:
        tup = readsequences(sys.argv[2])
        if not tup:
            print("readsequences() returns None.")
        else:
            st1, st2 = tup
            print("The first string: {}".format(st1)) 
            print("The second string: {}".format(st2)) 
    except Exception as e:
        print("Error (readsequences()):", e)

    #Task 2-b
    try:
        if not tup: #Task 2-a has not been implemented
            print("longest_common_string() skipped...")
        else:
            commonst= longest_common_string(st1, st2)
            if not commonst:
                print("longest_common_string()  returns None.")
            else:
                print("The longest common substring is {} of size {}.".format(commonst,len(commonst)))    
    except Exception as e:
        print("Error (longest_common_string()):", e)

    print("\n\n"+stars)
    print("Testing Task 3 --- Top LY Words")
    print(stars)

    #Task 3-a
    try:
        words = get_words(sys.argv[3])
        if not words:
            print("get_words()  returns None.")
        else:
            print("+ {} has a total of {} words.".format(sys.argv[3], len(words)))
    except Exception as e:
        print("Error (get_words()):", e)

    #Task 3-b
    try:
        if not words: #Task 3-a has not been implemented
            print("get_dic() skipped....")
        else:
            dic = get_dic(words)
            if not dic:
                print("get_dic()  returns None.")
            else:
                print("+ There are {} ly-words in the file.\n+ '{}' and '{}' have {}, {} occurrences respectively.\n".format(len(dic), 'only', 'hardly', dic['only'], dic['hardly']))
    except Exception as e:
        print("Error (get_dic()):", e)

    #Task 3-c
    try:
        if not words or not dic: #Task 3-a has not been implemented
            print("get_top_10() skipped....")
        else:
            results = get_top_10(dic)
            if not results:
                print("get_top_10() returns None.")
            else:
                print("+ Top 10 ly-Words in {}:".format(sys.argv[3]))
                for word, n in results:
                    print(" "*5+"{:<20} {:<}".format(word, n)) 
    except Exception as e:
        print("Error (get_top_10()):", e)


