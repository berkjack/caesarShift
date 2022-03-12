

def user_text():
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	text_crypt = input("Enter the text you want to encrypt, please:\n")
	shift_rate = int(input("Enter the 'shift rate', please:\n"))
	alphabet_size = len(alphabet)

	temp_text = []
	words_list = text_crypt.split()
	for i in range(len(words_list)):
		for j in range(len(words_list[i])):
			element_index = alphabet.index(words_list[i][j])
	
			if element_index + shift_rate <= alphabet_size-1:
				if element_index + shift_rate < (-1*alphabet_size):
					index = (-1*(element_index) + shift_rate) % alphabet_size
					temp_text.append(alphabet[-1*index])
					
				else:
					temp_text.append(alphabet[element_index + shift_rate])
				
			elif element_index + shift_rate > alphabet_size-1:
				index = (element_index + shift_rate) % alphabet_size
				temp_text.append(alphabet[index])
		
		if i != (len(words_list) - 1):	
			temp_text.append(" ")
		
	crypted_text = "".join(temp_text)
	print(crypted_text)


user_text(alphabet)

