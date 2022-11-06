def frequencies():
    '''
    Prints the frequency of each letter in a sentence.
    '''
    freq = dict()
    sentence = input('Enter a Sentence: ')
    for i in sentence:
        if not i.isalpha():
            continue
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    print('Frequencies: ')
    for letter in freq:
        print(f'{letter} => {freq[letter]}')

frequencies()
