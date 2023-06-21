while True:

    sent = input("Enter the sentence:")

    if sent == "":
        break

    words = sent.split()
    print("No of words entered:", len(words))

    count = 0

    for word in words:

        if 'a' in word.lower():
            count += 1
        print("No of words that contain the vowel ‘a’:", count)
