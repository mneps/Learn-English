
# Learning English

## Overview
This program uses the Markov chaining technique to "teach" the computer the syntactic form of English.  By analyzing a text file of significant length, the program builds a frequency table and can thus learn the likelihood of one letter following another.  By referencing this table, the program can then "learn" common morphemes, words, and phrases and is capable of producing a string of characters that--while not meaningful English--holds recognizable properties of the language.  For this program, English is considered to be comprised of only letters and spaces.

## Versions
There are two versions of the program (named v1 and v2).
### v1
Version one is a non-learning model of the program.  No text file is given, so a random, bogus version of English will be created.  This interpretation of the language is randomly generated and will thus change each time the program is run.  Based on its understanding of English, the program will then produce a 150-character string, representing what it believes English might look like.  Because the frequency table is completely made up, the string will not resemble English in any meaningful fashion.<br/>
If one is in the learn_english directory and wishes to run the non-learning version of the program, simply do the following:
```
cd v1
python not_learning.py
```

### v2
Version two is the interesting one.  The program takes in two command-line arguments, a text file and a "link" length, that it will use to learn English.  The text file should be large enough to give the program a basis upon which to learn English.  (All non-letters and non-spaces will be stripped from the text file and all letters will be converted to lower case.)  I have provided a 44,500-word text file called meditations.txt, which contains the Meditations of Emperor Marcus Aurelius Antoninus.  The "link" length (called such because it's a link in the Markov chain) is an integer that represents the length of characters by which to learn English.  (The link length should generally not be greater than 7 or so.  The program becomes quite slow if the link length is too big.)  If the link length is 1, for example, the progam will create a frequency table by moving letter by letter through the file (in the word "hello," for example, "e" would follow "h", "l" would follow "e", and so forth).  If the length is 2, the frequency table will be created by moving two letters at a time (so in "hello," "el" would follow "he", "ll" would follow "el," and so on).  This means that the greater the link length, the more accurately the computer will learn.  Like the non-learning version, the learning version will create and print a 150-character string based on what it believes English looks like.  Since the program now has real English to look to as a model, we expect the output to more closely resemble real English.<br/>
If one is in the learn_english directory and wishes to run the learning version of the program (with meditations.txt as the text file and a link length of 3), simply do the following:
```
cd v2
python learning.py meditations.txt 3
```

## Does it Work?
If the program works, we would expect the 150-character string produced by the non-learning version to be gibberish, while the string produced by the learning version to resemble English more and more as the link length increases.  I ran the program six times--the non-learning program once and the learning program with link lengths of one through five--and have printed the strings produced below.<br/>
### Not Learning:
alpjuptpfcuxxrnjf crofhfsilgecrzyhfrurvtvtqnhkcusqslwrcnbyrfivfst rgejfxxpm wvxcrossnnipmgkdxdkmnfbujszjfcvpuiniokang ybuxvctpmthexlleseubyzxvejisrhkoq
### Learning with a link length of 1:
u sseithfousst allllf wom probe ntofthound the appr lyt d m wit f at ith tids meanu bupo ancirce ha gacibys se rng d atore gsty cunk walavisen thichico
### Learning with a link length of 2:
kcome its hat it it of to mationthey derimper gin andagive such his of cand gainds your youre con ons plue thence caut all of is  ceive me butere such f
### Learning with a link length of 3:
n and fore othe memberg  all you lity ordantall thus revery you with them approduces anslatterest neithose to the a part  bothe wher not mated samen and
### Learning with a link length of 4:
o what is good and good for the gent you may be bodies of variety cast of be and work of you do evil thing  he which heroesus luxury arch of while yet whi
### Learning with a link length of 5:
now for yourself in justice with that i retain you should so reason what the end substances change the highest which profitable necessity can attain found
As is expected, each iteration of the program gets more and more accurate, thus proving the functionality of the program.

