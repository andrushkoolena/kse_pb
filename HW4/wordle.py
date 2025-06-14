# import random

# words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
# x = random.random()
# y = x * len(words)
# z = int(y)
# secret_word = words[z]

# tries = 6
# wl = len(secret_word)
# # w = secret_word

# print("Welcome to Wordle!")
# print("Guess the",wl,"-letter word. You have", tries, "tries.")

# while tries!=0:
#     guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
    
#     if len(guess)!=wl:
#         print("Wrong length. Expected", wl)
#         continue

#     if guess==w:
#         print("You win!!!")
#         break

#     result=[]; i=0
#     while i<wl:
#         ch = guess[i]
#         if ch==w[i]:
#             result.append('correct')
#         elif ch in w:
#             result.append('present')
#         else:
#             result.append('absent')
#         i+=1

#     display=[]
#     j=0
#     while j<wl:
#         s = guess[j]
#         res = result[j]
#         if res=='correct':
#             display.append("["+s.upper()+"]")
#         elif res=='present':
#             display.append("("+s+")")
#         else:
#             display.append(" "+s+" ")
#         j+=1

#     junk = ''.join([c for c in display if c])
#     print("Result:", ' '.join(display))
#     tries = tries - 1
# else:
#     final = secret_word
#     print("You lose! The word was:", final)

from main import random_word, guess_the_word, show_the_result
secret_word=random_word()
tries=6
word_length=len(secret_word)
print("Welcome to Wordle!")
print(f"Guess the {word_length}-letter word. You have {tries} tries.")
while tries>0:
    try:
        guess=input(f"Attempt {7-tries}/6 - Eneter guess:")
        if len(guess)!=word_length:
            print(f"Wrong length. Expected {word_length} characters.")
            continue
        result=guess_the_word(guess, secret_word)
        if guess==secret_word:
            print("You win!!!")
            break
        display=show_the_result(guess,result)
        print("Result:", display)
        tries-=1
    except Exception as e:
        print(f"Error occured: {e}")
        continue
else:
    print(f"You lose! The word was: {secret_word}")

