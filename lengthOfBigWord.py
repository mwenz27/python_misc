def lengthOfBigWord(sent):
    
    #1 use a split function to get a list of words
    words = sent.split(" ")
    #2 use a loop to compare word sizes
    largest_word = words[0]
    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
        
    #3 return largest word
    return print(largest_word)

sentence = "We'll start with an overview of how machine learning models work and how they are used. This may feel basic if you've done statistical modeling or machine learning before. Don't worry, we will progress to building powerful models soon."

lengthOfBigWord(sentence)