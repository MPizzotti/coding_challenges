# https://edabit.com/challenge/QWAqDyd9RXqyrNyo3

def abbreviate(phrase, min_length=4):
    """
    Aim of this function is returning a string that is the abbreviation of the phrase passed as input,
    taking in consideration only the words that are longer than the min_length passed.

    :param phrase: phrase passed as input.
    :param min_length: minimum_length for a word to be considered during abbreviation.
    :return: abbreviated string.
    :rtype: str
    """
    return "".join([word[0].upper() for word in phrase.split(" ") if len(word) >= min_length])


if __name__ == '__main__':
    min_length_is_not_valid = True
    # get the phrase to abbreviate.
    str_to_abbreviate = input("insert phrase: ")

    # until the value is not good.
    while min_length_is_not_valid:
        # get the minimum length for abbreviating .
        min_length_to_consider = input("insert minimum word length (default is 4, press enter to skip): ")

        # if the value is not "", we have to use the specified number from input.
        if min_length_to_consider != "":
            # validating the input passed.
            try:
                # the value passed must be an integer.
                min_length_to_consider = int(min_length_to_consider)
            # if the value is not correct, ask again for the number.
            except ValueError:
                print("value not correct!")
                continue

            # the validation has taken place, so we set the flag to false for exiting the loop.
            min_length_is_not_valid = False
            # abbreviate the phrase using the defined number passed as input.
            abbreviated_str = abbreviate(str_to_abbreviate, min_length_to_consider)

        # if the value is "", we have to use the default number from the function.
        else:
            # the validation has taken place, so we set the flag to false for exiting the loop.
            min_length_is_not_valid = False
            # abbreviate the phrase using the default number.
            abbreviated_str = abbreviate(str_to_abbreviate)

    # print the result
    print(f"the abbreviated phrase is '{abbreviated_str}'")
