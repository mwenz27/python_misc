try:
    f = open("text.txt", 'r')
except as r:
    print("file doesn't exist", r)