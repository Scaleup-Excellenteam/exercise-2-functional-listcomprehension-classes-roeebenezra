import string


def count_words(text):
    """
    Counts the length of each word in a given text and returns a dictionary of the lengths and their frequencies.
    :param text: The text to count the word lengths from.
    :return: A dictionary of the lengths of each word and their frequencies.
    """
    # Define the valid characters as all letters (lowercase and uppercase), apostrophes, and hyphens
    valid_characters = string.ascii_lowercase + string.ascii_uppercase + "'-"
    # Clean text from non-valid characters using the valid_characters set
    words = ("".join(c for c in word if c in valid_characters) for word in text.split())
    # Use a dictionary comprehension to count the lengths of the words
    word_lengths = {len(word): 0 for word in words}
    for word in text.split():
        # Strip word from non-valid characters
        word = "".join(c for c in word if c in valid_characters)
        if len(word) in word_lengths:
            word_lengths[len(word)] += 1
    return word_lengths


if __name__ == '__main__':
    text_for_count = "This is a sample sample text, text with words of " \
           "different lengths! Let's see if our function counts them correctly."
    word_len = count_words(text_for_count)
    print(word_len)
