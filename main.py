from solution import *

try:
    N = int(input("Enter N: "))
    K = int(input("Enter K: "))
    s = read_file(path)

    check_variables(N, K)
    print(frequency_list(s))
    print("Amount of words: ", words_counts(s))
    print("Average amount of words in sentence: ", average(words_counts(s)))
    print("Median amount of words in sentence: ", median(words_counts(s)))
    dct = Ngramms(s, K)
    print(f"Top-{N} {K}-gramms: ")
    print([dct[i] for i in range(min(N, len(dct)))])

except EOFError as exception:
    print(exception)

except ValueError as ex:
    print(ex)
    
