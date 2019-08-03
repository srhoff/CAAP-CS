
openfile = open("eng_dict.txt", 'r')
#Open and read the file
if openfile.mode == 'r':
    words = openfile.read().splitlines()
anagram_proto = {}
anagrams = {}
#sets length of words = 8
#sorts letters in word by alphabetical order
for word in words:
    if len(word) >= 8:
        letters = word.lower()
        letters = ''.join(sorted(letters))
        if not (letters in anagram_proto):
            anagram_proto[letters] = [word]
        else:
            anagram_proto[letters].append(word)
    ####res = [[i for i in anagram_proto[word]] for i in anagram_proto.keys()]
##need assistance on doing good
for [word] in anagram_proto.values():
    if len([word]) > 1:
        anagrams[letters] = [word]
print(anagrams)


        #print(letters)##testing
#print(anagram_proto)##testing



##Sort the File Alphabetically
#print(''.join(sorted(words)))
            ##Iterate through the list of words
                ##DURING EACH ITERATION
                #check wordlength
                #sort the letters in current word
                ##key in sorted letters
                #check if key exists in dictionary already
                    ##if the key exists:
                        #add the words
                    ##if the key does not exist yet:
                        #add a key to the dictionary
### Go through dictionary and check for sizes = 1
##If length bad
    #continue
##else (length good)
    #program logic
#abceesu : ["because", ""]

##Key : Thang
##size of this anagram = 2 (length of list)
##length of anagram = number of characters in word
##Remember, In order of importance
    ##Only Length 8+
    ##Anagram size is better
    ##IF SAME SIZE
    ##sort by Length
# this_dict = {}
# for key,value in this_dict
#
# this_dict['a_key'] = 'a_value'
#
# print(this_dict)
# print(this_dict['a_key'])
#
# if this_dict["asdfasf"]:
#     #do things\
# else:
#     #do other things
# if 'a_key' in this_dict
#
# if "a_key" not in this_dict
