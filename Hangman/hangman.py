import random
import os

word_file = open("wordlist.txt", "r")
data = word_file.read()
data_list = data.replace('\n', ' ').split(" ")
word_file.close()



not_found = True
target_list = []
guessed_letters = []
target_word_list = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
health_count = 7


play = int(input("Choose game mode(1 for computer, 2 for player vs player): "))
if play == 1:
    target_word = random.choice(data_list)
    print("Choosing word")
    print("...")
    print("...")
    print("...")
    print("Word selected")
elif play == 2:
    target_word = str(input("Enter a target word: "))
    os.system('cls' if os.name == 'nt' else 'clear')
for n in target_word:
    target_list.append('_')
    target_word_list.append(n)

print(*target_list)


while not_found and health_count > 0:
    print('----------------------------------------')
    print("Health: ", health_count, "lives remaining")
    print(*target_list)
    guess = str(input("Enter a letter to guess: "))
    if guess not in guessed_letters and guess in alphabet and guess in target_word:
        guessed_letters.append(guess)
        index = [i for i in range(len(target_word)) if target_word.find(guess, i) == i]
        for x in index:
            target_list[x] = guess
    elif guess in guessed_letters and guess in target_word:
        print("Sorry that letter has already been guessed")
    elif guess not in target_word:
        print("Sorry that letter is not in the word")
        health_count = health_count - 1
    if '_' not in target_list and target_list == target_word_list:
        print(target_word_list)
        print("Congrates you guessed the word!!!")
        not_found = False
    if health_count == 0:
        print("Sorry you failed to guess in the alloted attempts")
        print("The target word was ", target_word)
        