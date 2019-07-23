s = "janfebmaraprmay"

for i in range(0, len(s), 3):
    print(f'{s[i]}{s[i+1]}{s[i+2]}')
    print(s[i:i+3])