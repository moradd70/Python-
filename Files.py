# how to open a file
fo = open('test.txt', 'w')

# get some info
print('Name: ', fo.name)
print('Is closed', fo.closed)
print('opening mode', fo.mode)
fo.write('I love Python')
fo.write(' by MR')
fo.close()

# open to append 
fo = open('test.txt', 'a')
fo.write(' , and I also like PHP')
fo.close()

# read from file
file = 'test.txt'
fo = open(file, 'r+')
text = fo.read()
print(text)
fo.close()

# create file
fo = open('test2.txt', 'w+')
fo.write('This is my new text file')
fo.close()
