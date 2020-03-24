def is_vowel(symbol):
	return symbol == 'a' or symbol == 'e' or symbol == 'i' or symbol == 'o' or symbol == 'u' or symbol == 'y' or symbol == 'A' or symbol == 'E' or symbol == 'I' or symbol == 'O' or symbol == 'U' or symbol == 'Y'

def is_consonants(symbol):
	return not is_vowel(symbol) and ((symbol >= 'A' and symbol <= 'Z') or (symbol >= 'a' and symbol <= 'z'))

def count_consonants(str):
	return len([x for x in str if is_consonants(x)])