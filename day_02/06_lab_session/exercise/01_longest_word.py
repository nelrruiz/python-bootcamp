def get_longest_word(text):
    """TODO: Add decoding process"""
    word_list=list(text.split())
    print(word_list)  
    
    longest_word = None

    if not text:
        return ""
    else:
        for word in word_list:
            if longest_word is None or len(word)> len(longest_word):
                longest_word = word
    print(longest_word)          

# "The quick brown fox jumps" -> "quick"
print(get_longest_word("The quick brown fox jumps"))

# "I love programming in Python!" -> "programming"
print(get_longest_word("I love programming in Python!"))

# "" -> ""
print(get_longest_word(""))
