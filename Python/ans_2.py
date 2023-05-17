inp = input().replace(' ','')
frequency = {}
for letter in inp:
    frequency[letter]=0 if letter not in frequency else frequency[letter]
    frequency[letter]+=1
values_set = set(frequency.values())   
print('Yes') if len(values_set)==1 else print('No')
    