# problem 1
# import this

#problem 2
#a = 895
#b = 954

#x = a*a + b*b

#print(x)

# problem 3

#x = "w8bqdednrBpnD6dMAZ3WACiHsGTU9huUzH4c6aUv9OeH02LWtiXx5ynoh2JTxPOsteopilusdB9gD8UJflJxaBZzQQxereocMZDh6oQ6pnq7bDeXeim6ZzsfbwlvmSeYiiJXhEh0lFtemminskiilvb7c9sZ0uVNEo9cHZEyb91JFxAUwXoVYbVZX0I30Zj."
#y =  f'{x[62:71+1]} {x[138:147+1]}'
#print (y)

# problem 4

# x = 4970
# y = 9734
# count = 0

# for i in range(x, y+1):
#     if i % 2 != 0:
#         count += i
# print(count)

# same process
# r = sum([i for i in range(x,y+1) if i%2 != 0])
# print(r)

# problem 5


# x = open('input.txt','r')
# x = x.readlines()
# outputfile = []
# for pos,lines in enumerate(x):
#     if pos % 2 != 0:
#         outputfile.append(lines)
# print(outputfile)
#
#
#
# # write files
#
# f =  open("out.txt", "w")
# f.write(''.join([line for line in outputfile]))


## problem 6

#string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# dict = {}
#
# for word in string.split(' '):
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
#
# for key,value in dict.items():
#     print(key,value)

## 2nd method
# from collections import Counter
#
# dict = Counter(string.split(' '))
#
# for key,value in dict.items():
#     print(key,value)





