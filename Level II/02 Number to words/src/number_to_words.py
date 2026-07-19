from src.constats import UNDER_20, TENS, ABOVE_100


def num_to_words(num: int) -> str:
    """
    Convert a number to its word representation.
    Note: This function only works for number less than 10^15 and greater than 0.

    :param num: The number to convert.
    :return: The word representation of the number. 

    >>> number_to_word(0)
    'zero'
    >>> number_to_word(10)
    'ten'
    >>>num_to_words(3468)
    'three Thousand four Hundred sixty eight'
    """
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return TENS[num // 10]

        return TENS[num // 10] + " " + UNDER_20[remainder]

    # 112 -> 1 Hundred 12
    # 212 -> 2 Hundred 12
    # 3212 -> 3 Thousand 212

    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_words(num // pivot)
    p2 = ABOVE_100[pivot]

    if num % pivot == 0:
        return f"{p1} {p2}"

    return f"{p1} {p2} {num_to_words(num % pivot)}"


if __name__ == "__main__":
    print(num_to_words(315412))
