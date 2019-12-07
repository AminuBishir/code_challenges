import math
'''
Lilah has a string, , of lowercase English letters that she repeated 
infinitely many times.

Given an integer, , find and print the number of letter a's in the first  
letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the 
first  characters of her infinite string. There are  occurrences of a in 
the substring.
'''
#Solution

def repeatedString(s, n):
	#make sure 'a' exist in the string and that the string is not made up of 'a' alone
	if len(s)>1 and s.count('a') >0:

		#get the counts of 'a' from the given string
		char_count = s.count('a')

		#get how many times can the whole string be repeated (neglecting part of it
		#that may appear at the end)
		repetition = math.floor(n/len(s))

		#get the length of the remaining part of the string that reappear at the end
		rem_chars_count = n % len(s)

		#get the remaining substring 
		targets_rem = s[:rem_chars_count]

		#the frequency of 'a' is its numbers of appearance in the repeated string 
		#plus its count in the remaining substring
		char_frequency = char_count*repetition + targets_rem.count('a')

		return char_frequency
	#just return n when the string contains only a, i.e 'a' appears n times
	elif len(s) == 1 and s.count('a') >0:
		return n
	#return 0 if the string doesn't contain 'a'
	else:
		return 0
print("a appears "+str(repeatedString("amina",100))+" times when the string 'amina' is repeated 100 times") 