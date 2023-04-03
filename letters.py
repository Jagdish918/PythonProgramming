def most_frequent(string):
 
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1


    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

   
    for letter, count in sorted_freq:
        print(f"{letter} = {count:02}")

s=input("Enter a String :")
most_frequent(s)
