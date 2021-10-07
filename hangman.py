##TOY PROJECT: HANGMAN GAME
##Note: correctWord is case sensitive: will make either upper case or lower case

correctWord='Khabibulin'
blankWord=['_','_','_','_','_','_','_','_','_','_']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

win=0
wrong=0

while win==0: 
    
    print('')
    print(alphabet)
    
    #ask the user to guess a letter
    guess=input('Guess a letter!')
    
    #if user enters '!', stop the game
    if guess=='!':
        break
    
    print('You guessed: ', guess)
    
    j=0 #correctWord is string array; blankWord is an array; index j corresponds to correctWord character g 
    count=0 #count the number of occurrences of a letter
    
    #loop through the correct word
    for g in correctWord:
        
        #if the guessed letter is in the correct word
        if g==guess:
            if g in alphabet:
                alphabet.remove(g)
            
            blankWord[j]=g
            count+=1
        j+=1
    
    print('' * 2)
        
    if count>0:
        print('There is/are', count, guess)
    print(str(blankWord))
    
    #if the guessed letter is not in the correct word
    if guess not in correctWord:
        print('There is no', guess)
        nope+=1
        
        if guess in alphabet:
            alphabet.remove(guess)
            
    print('Wrong guesses: ' ,wrong)
    
    print('')
            
    if count>0:

        #ask the user if they want to solve the puzzle
        solve = input('Would you like to solve? yes: 1; no: 0; stop game: !') 
       
        #if user types '0', they don't want to solve; continue playing
        if solve=='0':
            continue
            
        #if user types '1', they want to solve'''   
        if solve=='1':
            answer=input('Enter your answer')
            if answer==correctWord:
                print('Yay! You won!')
                win=1
                break
        
        #if user types '!', stop the game
        if solve=='!':
            break
            
    #head, body, arm, arm, leg, leg
    #therefore, 6 wrong guesses
    #end game after 6 wrong guesses
    if wrong==6:
        print('Sorry, you lost.')
        print(correctWord)
        break
            

##NOTES AND FIGURING STUFF OUT

#make array same length as correctWord
"""blankWord = ['*'] * len(correctWord)
print(a)"""

#if guessWord == correctWord:

#head, body, arm, arm, leg, leg
#6 guesses

#if y: do
#if n: continue

'''
if ??? == correctWord
print "yay! you won!
break
'''

#if letter is in word
#loop through alphabet array
#pop out of array

#NOTE: correctWord is case sensitive
#make either uppercase or lowercase

#trying to figure something out
'''z = 'popcorn'
zz = 'p'

for y in z:
    if y == zz and y in alphabet:
        alphabet.remove(y)
        
print (alphabet)''' 
    
#find index of p
#pop has to be an index
#or...
#hmmm...

#Don't forget to make guess be 1 character long and be a letter
#Modification: guess can't be anything except a letter (upper/lower) or '!'

#while solve !='0' and solve !='1' and solve !='!':
#that sounds wrong; brain is currently broken
#tried grouping the whole thing but 'else' didn't seem to work

#would you like to solve? (yes:1 no:0 end the game: !)

#make array of random words; low long do I want?
#popcorn, parachute, sandwich, ostrich, dragonfly, hornet, chicken, hummingbird, rainbow, baseball, chocolate, mushroom, satellite, glasses, castle, puppet, avocado, giraffe, cricket, balloon, oatmeal, butterfly, peppermint, kangaroo, 

##FOUND OUT
#Remember: pop() removes by index e.g. array.pop(2)       
#remove() just removes
#remove() only gets rid of first occurence, but array is just the alphabet so it's fine
        
    