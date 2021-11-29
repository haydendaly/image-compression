"""
https://www.section.io/engineering-education/run-length-encoding-algorithm-in-python/#implementation
"""


def compress(message: str) -> str:
    # TODO: Change algorithm so that input is of type bytes and it returns bytes
    # The problem lies in the fact that this algorithm relies on the input
    # (the message) to be a string. This has many problems:
    # 1. We don't want to store the whole image in memory. It is inefficient. It
    # is better to go byte by byte using a generator. However, this is not a big
    # issue as long as our data fits in memory.
    # 2. IMPORTANT. We have to handle how to "store" the count and the characters
    # when the characters are bytes instead of 1-length `str` objects.
    #
    # If we solve (2), and apply the same solution for de-compress, we have a
    # working RLE algorithm for bytes. The ugly (and inefficient) but working
    # solution is just taking the input as bytes and interpret it as strings and
    # then just compress that instead. Since the algorithm is lossless, the
    # result will not be lost. However, since Python will "stringify" the bytes
    # with their own syntax, we would be compressing an image according to the
    # redundancy added by the Python byte parser instead of the redundancy of
    # the image itself, which is the algorithm would be slow AND not very
    # correct.
    encoded_string = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            # if the character at the current index is the same as the character at the next index. If the characters are the same, the count is incremented to 1
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        # the count and the character is concatenated to the encoded string
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string


def decompress(our_message: str) -> str:
    # TODO: Change algorithm so that input is of type bytes and it returns bytes
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while i <= len(our_message) - 1:
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message + run_word
            j = j + 1
        i = i + 2
    return decoded_message
