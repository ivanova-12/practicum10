def vowels_and_consonants(sentence: str) -> None:
    """Outputs the number of vowels and consonants in a sentence
    Args: sentence in russian language
    Returns: None
    """

    all_vowels = 'ауоеияюёэы'
    spec_symbols = '.,...!?""«»-—;:()[] '
    vowels_in_snt = 0
    consonants_in_snt = 0
    all_sentence = len(sentence)

    for elem in sentence.lower():
        if elem in all_vowels:
            vowels_in_snt += 1
            all_sentence -= 1
        elif elem in spec_symbols or elem in '1234567890':
            all_sentence -= 1
    consonants_in_snt = all_sentence

    print(f'{vowels_in_snt} гласных и {consonants_in_snt} согласных букв')
    
