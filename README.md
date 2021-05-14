import random
chosen_word=random.choice(['rakam','kamna','karamvir','chetna','geeta','jaipal'])
print(chosen_word)
x=len(chosen_word)
display=[]
for i in range(x):
    display+='_'
print(display)
end_of_game=False
while not end_of_game:
    guess=input("guess any letter to save hangman:-").lower()
    for position in range(x):
        if guess==chosen_word[position]:
            display[position]=guess
    print(display)
    while '_' not in display:
        end_of_game=True
        print("u win")
        break
