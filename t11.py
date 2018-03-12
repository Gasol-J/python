# def readnumbers(file_name): 
    
#     f= open(file_name,'r')
#     num = f.read().split(',')
#     for i in range(len(num)):
#         num[i]=num[i].strip(' ')

#     print('Numbers:', num)

#     def isPrime(nums):
        
#      	if(nums>1):
#     	 	for i in range(2,nums):
#     		 	if (nums % i)==0:
#     			 	print(nums,':Not Prime')
#     			 	break
#     	 	else:
#     	 	 	print(nums,':Prime')
#     for i in range(len(num)):
#     	isPrime(int(num[i]))
	

  
# readnumbers('readnumber.txt')


# def readsequences(file_name): 
#     '''
#     Input: a file name
#     Return: a tuple of two strings
#     '''
#     f = open(file_name,'r')
#     lines = f.readlines()
#     str1= lines[0].strip("\n\r")
#     str2 = lines[1]

#     print("The first string:",str1)
#     print("The second string:",str2)
    



# # st1="BBEBDEAEBADAAEDCDDBCBACBBCBDDBABBDEECDBAECACEECC"
# # st2="CCBADACDCCADDBDABDEDCDDBCBACBBCBDDBABBDEECCACCBDCEBABBBEDC"
#     def longest_common_string(st1, st2): 
#         m=0
#         n=len(st1)
#         st3=[]
#         b=0
#         while(m<n):
#             i=n-m
#             while(i>=0):
#                 st3.append(st1[m:m+i])
#                 i-=1
#             m+=1
 
#         for x in st3:
#             a=0
#             if x in st2:
#                 a=len(x)
#                 c=st3.index(x)
#             if a > b:
#                 b=a
#                 d=c
 
#         if b>0:
#             print("The longest common substring is ",st3[d],"of size",len(st3[d]))
#     longest_common_string(str1,str2)
# readsequences('sequences.txt')

import string
import re
word_count = 0
lyword_count = 0
lywordlist=[]
b='ly'
c='--'
r='[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
f = open('sense_and_sensitivity.txt','r')
words = f.read().split()
word = str(words)
words = re.sub(r,'',word)
words = words.lower()
wordlist = words.split()
# for a in wordlist:
# 	if a[-2:]==c:
# 		a=a[:-2]



for item in wordlist:
	if item[-2:]==b:
		lywordlist.append(item)

lywordlist1=[]
for i in lywordlist:
	if i in lywordlist1:
		continue
	lywordlist1.append(i)
print(len(lywordlist1))

print(len(lywordlist))

a ={}
for i in lywordlist:
	if lywordlist.count(i)>=1:
		a[i]=lywordlist.count(i)
print(a)
for i in range(len(lywordlist)-1,-1,-1):
	if lywordlist[i] in lywordlist[:i]:
		lywordlist.pop(i)

list1=[]
i = 0
while i <10: 
	lymax1 = max(a, key=a.get)
	# print(lymax1, ":",a[lymax1])
	list1.append((lymax1,a[lymax1]))
	del a[lymax1]
	i+=1
	print(list1)





# print(len(a))
# print(len(lywordlist))
# print("this is numbers of ly-words:",len(lywordlist))

# print("this is the numbers of all words:",word_count)


