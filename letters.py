def most_frequent(string):
    # create a dictionary to store the frequency of each letter
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    # sort the dictionary by frequency, in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # print the letters and their frequencies in descending order
    for letter, count in sorted_freq:
        print(f"{letter} = {count:02}")

s=input("Enter a String :")
most_frequent(s)
