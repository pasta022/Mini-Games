# open story template file
with open("story.txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# check forbeginning and end of word to be replaced
for idx,char in enumerate(story):
    if char == target_start:
        start_of_word = idx
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: idx + 1]
        words.add(word)
        start_of_word = -1

answers = {}

# get replacement for each word
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# put replacememt in story3
for word in words:
   story = story.replace(word, answers[word])

print("\n",story)