alphabet_str = "אבגדהוזחטיכלמנסעפצקרשת"
i = 1
while i < 10:
	alphabet_str = alphabet_str[:i * 10] + " " * 9 + alphabet_str[i * 10:]
	i += 1
i = 1
while i*100 < len(alphabet_str):
	alphabet_str = alphabet_str[:i * 100] + " " * 99 + alphabet_str[i * 100:]
	i += 1


def letter_value(let):
	if let == "ן": let = "נ"
	if let == "ם": let = "מ"
	if let == "ף": let = "פ"
	if let == "ך": let = "כ"
	if let == "ץ": let = "צ"
	return alphabet_str.find(let)+1


def word_value(wor):
	sum1 = 0
	for letter in wor:
		sum1 += letter_value(letter)
	return sum1


def same_value(w1, w2):
	return word_value(w1) == word_value(w2)


def all_same(word):
	words = ""
	wlist = open("heb_words.txt", "rt").read().splitlines()
	for place in wlist:
		current = place.split(',')[0]
		if same_value(current, word):
			words += current + '\n'
	return words

	
print(all_same(input("איזו מילה תרצה לבדוק? \n")))
