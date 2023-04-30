def spin_words(sentence):
    words = sentence.split(' ')
    word_sentence = [word[::-1] if len(word) >= 5 else word for word in words]
            
    return ' '.join(word_sentence)