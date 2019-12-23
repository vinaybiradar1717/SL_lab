# 6b. Python Classes: Write a python class to reverse a sentence (initialized via constructor) 
# word by word. Example:  “I am here” should be reversed as “here am I”. 
# Create instances of this class for each of the three strings input by the user
# and display the reversed string for each, in descending order of number of vowels in the string.

class sentenceReverser:
    vowels = ['a','e','i','o','u']
    sentence = ""
    reverse = ""
    vc = 0

    def __init__(self,sentence):
        self.sentence = sentence
        self.reverseSentence()

    def reverseSentence(self):
        self.reverse = " ".join(reversed(self.sentence.split()))

    def getVC(self):
        self.vc = sum(s in self.vowels for s in self.sentence.lower())
        return self.vc

    def getReverse(self):
        return self.reverse

items = []

for i in range(3):
    reverser = sentenceReverser(input("Enter a sentence: "))
    items.append(reverser)
    print(reverser.reverse)

for i in sorted(items, key=lambda item: item.getVC(),reverse=True):
    print(i.getReverse()," >>>>> ",i.getVC())