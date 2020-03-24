def is_vowel(symbol):
	return symbol == 'a' or symbol == 'e' or symbol == 'i' or symbol == 'o' or symbol == 'u' or symbol == 'y'

def count_vowels(str):
	return len([x for x in str if is_vowel(x)])