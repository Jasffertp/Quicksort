#Author: Jasffer T. Padigdig
#Date: September 26, 2020
#Assignment: Quicksort
#Description: It's an quick sort algorithm that arranges a given word into alphabetical order
#References: I based my work on the pseudocode of the "Introduction to Algorithms - 3rd edition" Book
#and i based seperating a string into an array to this: https://www.codegrepper.com/code-examples/delphi/how+to+split+a+word+into+letters+in+python
#and combining an array into a string to this: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q + 1, r)

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
            
    a[i + 1], a[r] = a[r], a[i + 1]
    
    return i+1
    
word = input('what word do you want sorted? ')
print(f'your word is: {word}')
s = word
word = list(word)
length = len(word) - 1

quicksort(word, 0, length)

word = ''.join(word)
print(f'{s} in a sorted manner is: {word}')