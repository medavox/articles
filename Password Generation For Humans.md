Secure, Human-Compatible Password Generation
=============================================


You will need:

one or more 6-sided dice
One or more big, obscure dictionary


take the largest dictionary for the most obscure topic you can find.
Uncommon languages are a good source, as a domain-specific technical dictionaries, eg a medical or science dictionary

    in this example I'll be using Y Geiriadur Mawr ( The Big Welsh Dictionary), Ninth Edition



Roll one more dice than the number of digits in your dictionary's page count.

    my dictionary has 367 pages (3 digits), so I will roll 4 dice.
    

Roll the dice (or the same die multiple times) and subtract 1 one from each result.
These make up a number in base-6
    
    My dice show 6655, so the number is 5544


convert the number to decimal
(use an online converter; search for "base 6 to decimal converter")

    using https://www.unitconverters.net/numbers/base-6-to-decimal.htm ,
    I find that 5544 base 6 is 1288 in decimal

modulo this number with the number of pages in the dictionary, and add one
    
    (1288 % 367) + 1 = 188


Open your dictionary to this page.


Use a technique to choose a random word from the two pages open in front of you.
I like to close my eyes and drop my finger somewhere, but this is not optimally random.

    My finger landed on the word 'dirym', which is a Welsh adjective meaning 'weak'.
    Bear in mind that for my dictionary, I could have randomly ended up in the English-to-Welsh half,
    and therefore blind-picked an English word. This is fine.

To generate a long, strong password, do this process at least 3 times, 
with a different dictionary each time. The goal is to make up a phrase that is *at least* 10 characters long.

Whether to put spaces between the words, or even capitalisation is up to you (and the password policy).


Make up a story in your head about the words if you can, to help you remember.


Changing your password
=====================

When the time comes to change your password:


Drop a word from the existing phrase. I recommend you choose which one randomly.

Perform the word-choosing procedure above to add a new word to the existing phrase,
at a random position within it.



Tips
====

if you find uncommon or foreign words hard to remember, limit yourself to just English words.

Just be aware that if you reveal you do this to anyone,
it will reduce the randomness (and therefore the strength) of the password.

If this is still difficult to remember, try limiting the word to particular types.
eg 4 nouns, or 2 nouns, an adjective and a verb. Make it a sentence, and feel free to add connecting words between them!


Try to avoid common English words, as these are often in lists of common words that brute-force password crackers try.