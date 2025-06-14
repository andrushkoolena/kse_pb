import random
def random_word():
    words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
    x=random.random()
    y=x*len(words)
    number_of_word=int(y)
    return words[number_of_word]

def guess_the_word(guess, secret_word):
    result=[]
    for i in range(len(secret_word)):
        if guess[i]==secret_word[i]:
            result.append("correct")
        elif guess[i] in secret_word:
            result.append("present")
        else:
            result.append("absent")
    return result

def show_the_result(guess, result):
    display=[]
    for i in range(len(guess)):
        if result[i]=="correct":
            display.append("["+guess[i].upper()+"]")
        elif result[i]=="present":
            display.append("("+guess[i]+")")
        else:
            display.append(" "+guess[i]+" ")
    result_row=""
    for i in display:
        result_row+=i
    return result_row




