
def decoder(message, offset):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	encrypted_message = ""
	punctuation = ".,?'! "
	for letter in message:
		if not letter in punctuation:
			letter_value = alphabet.find(letter)
			encrypted_message += alphabet[(letter_value + offset) % 26]
		else:
			encrypted_message += letter
	return encrypted_message
    	
def encoder(message, offset):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	translated_message = ""
	punctuation = ".,?'! "
	for letter in message:
		if not letter in punctuation:
			letter_value = alphabet.find(letter)
			translated_message += alphabet[(letter_value - offset) % 26]
		else:
			translated_message += letter
	return translated_message
  

message = "my Python genius was on the other side of fear, glad I found it!!!"    	
 

message_2 = "po pojxed wudyki mqi ed jxu ejxuh iytu ev vuqh, wbqt p vekdt yj!!!"

print(encoder(message, 10)) 
print(decoder(message_2, 10))

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# The easiest way to break this code is to simply brute force though all of the possible shifts.
# We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can 
# look through all of the outputs and look for the one that in english, and we've decoded our message!
for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + decoder(coded_message, i) + "\n")



def vigenere_decoder(coded_message, keyword):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword_repeated = ""
    punctuation = ".,?'! "
    while len(keyword_repeated) < len(coded_message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(coded_message)]
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"
keyword = "friends"

print(vigenere_decoder(message, keyword))

def vigenere_coder(message, keyword):
    keyword_repeated = ''
    while len(keyword_repeated) < len(message):    
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(message)]
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v,keyword))
	
