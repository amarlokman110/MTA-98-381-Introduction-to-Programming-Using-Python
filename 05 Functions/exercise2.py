word = 'python'
reversed_word = word[::-1]
print (reversed_word)

reversed_word = ''
for c in word: #for..in loop
    reversed_word = c + reversed_word
    print(c, reversed_word)

reversed_word = ''
for i in range(len(word)):  #for..in..range loop
    reversed_word = word[i] + reversed_word
    print(i, word[i], reversed_word)

reversed_word = ''
for i in range(len(word)-1, -1, -1):  #for..in..range loop
    reversed_word += word[i] 
    print(i, word[i], reversed_word)
