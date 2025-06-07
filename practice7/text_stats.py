words=[]
def average_word_length(text):
    text3=text.split(" ")
    for word in text3:
       words.append(word)
    return len(word)/len(text3)
print(average_word_length("ttt ttt"))



