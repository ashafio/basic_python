numofWords=0
numofLetters=0
numofDigits=0

text=input("Enter anything: ")
for x in text:
     x=x.lower()
     if x >= 'a' and x<= 'z':
          numofLetters = numofLetters+1

     elif x >= '0' and x<= '9':
          numofDigits = numofDigits+1

     elif x == ' ':
          numofWords = numofWords+1

print("number of Letters: ", numofLetters)
print("number of Digits: " ,numofDigits)
print("number of Words: ",numofWords+1)