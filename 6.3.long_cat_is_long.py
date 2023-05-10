def count_words(text):
    """
    Counts the length of each word in a given text and returns a dictionary of the lengths and their frequencies.
    :param text: The text to count the word lengths from.
    :return: A dictionary of the lengths of each word and their frequencies.
    """
    # Clean text from non-alphabetic characters using a generator expression
    words = (word.strip().strip('.,!?') for word in text.split())
    # Use a dictionary comprehension to count the lengths of the words
    word_lengths = {word: 0 for word in words}
    for word in text.split():
        # Strip word from non-alphabetic characters
        word = word.strip().strip('.,!?')
        if word in word_lengths:
            word_lengths[word] += 1
    return word_lengths


if __name__ == '__main__':
    text = "This is a sample sample text, text with words of different lengths! Let's see if our function counts them correctly."
    word_lengts = count_words(text)
    print(word_lengts)
