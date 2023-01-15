"""Encipher or decipher text using The Route Cypher."""


def main():
    """Call encipher or decipher with args."""
    # plain_text = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
    plain_text = "one two three four five six seven eight nine ten eleven \
        twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
    cols, rows = 4, 5
    key = '-1 2 -3 4'
    enciphered = encipher(plain_text, cols, rows, key)
    print(enciphered)
    # cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
    # cols, rows = 4, 5
    # key = '-1 2 -3 4'
    deciphered = decipher(enciphered, cols, rows, key)
    print(deciphered)


def encipher(text, cols, rows, key) -> str:
    """Encipher a given text.

    Args:
        text (str): Text to encode
        cols (int): Number of columns
        rows (int): Number of rows
        key (list[int]): List of signed ints to choose col path

    Returns:
        str: String result
    """
    cipher_list = list(text.split())
    keys = list(map(int, key.split()))
    cipher_block = [None] * cols
    for i in range(cols):
        key_i = abs(keys[i])-1
        if keys[i] > 0:  # Positive key
            cipher_block[key_i] = cipher_list[key_i:: cols]

        else:  # Negative key
            cipher_block[key_i] = list(
                reversed(cipher_list[key_i:: cols]))

    enciphered = " ".join([" ".join(row) for row in cipher_block])
    return enciphered


def decipher(text, cols, rows, key) -> str:
    """Decipher a given text.

    Args:
        text (str): Text to decode
        cols (int): Number of columns
        rows (int): Number of rows
        key (list[int]): List of signed ints to choose col path

    Returns:
        str: String result
    """
    cipher_list = list(text.split())
    keys = list(map(int, key.split()))
    cipher_block = [None] * cols
    for i in range(cols):
        key_i = abs(keys[i])-1
        if keys[i] > 0:
            cipher_block[key_i] = cipher_list[key_i * rows:key_i*rows+rows]

        else:
            cipher_block[key_i] = list(
                reversed(cipher_list[key_i * rows:key_i*rows+rows]))

    deciphered = " ".join([row[i] for i in range(cols+1)
                          for row in cipher_block])
    return deciphered


if __name__ == "__main__":
    main()
