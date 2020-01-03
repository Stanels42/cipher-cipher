# cipher-cipher
###### Sorry it said cipher-cipher in the lab instructions

## About
The goal of the lab was to create a ceaser cipher in python that could take in a string and encript it. The second half was about creating a bot that would be able to take in an encripted sentence and return what it thought was the ornigonal sentence based on checking if the words are english.

## Precess
Encription: Time: I used a list that contains the alphabet. The function then finds the position of each charactor and replaces it with the cahractor X steps down the list<br>
Decription Bot: It guesses. Sort of. The approach I used was to to have the program check each key one step at a time. The bot then tests the result for english words. If more then 50% are real words it claims the input is translated. 50% was chosen because most longer sentences will work regardless but for shorter sentences might need threshold and a little help.