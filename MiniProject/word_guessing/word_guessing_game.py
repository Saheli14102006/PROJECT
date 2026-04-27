from word_dictionary import words
import random
random_word= random.choice(list(words.keys()))
# print(random_word)
randomword=['_']*len(random_word)
# print(randomword)
attempts=10
while attempts > 0:
  print('\nCurrent word:'+' '.join(randomword))
  print('Hint: ' + random.choice(words[random_word]))
  guess = input('Guess a letter:').lower()
  if guess in random_word:
    for i in range(len(random_word)):
      if random_word[i]==guess:
        randomword[i]=guess
    print('Great guess!')
  else:
    attempts-=1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in randomword:
    print('\nCongratulations!! You guessed the word: ' + random_word)
    break
if attempts==0 and '_' in randomword:
  print("\nYou've run out of attempts! The word was: " + random_word)
  
        
      