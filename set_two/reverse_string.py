def reverse_words(text):
    reversed = []
    text_splited = text.split(' ')
    for w in text_splited:
        reversed.append(w[::-1])
    reversed = ' '.join(reversed)

    return reversed

print(reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god')
