def get_words(text):
        #print(text)
        words = text.split()
        #print(words)
        count = len(words)
        return count

def count_chars(text):
	words = text.lower()
	existing = 1
	char_count = {}
	for char in words:
		if char in char_count:
			existing = char_count[char]
			existing += 1
			char_count[char] = existing
		else:
			char_count[char] = 1
	return char_count 


def sort_on(dict):
	return dict["count"]
def sort_chars(char_dict):
    #convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count":count})
        #sort list by count
    char_list.sort(reverse=True,key=sort_on)
    return char_list 
