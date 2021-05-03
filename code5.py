'''
# question 1
file=open('demo.txt','w')
file.close()
'''

# question 2
file =open('demo.txt','r')
content =file.read()
print('content before appending:\n',content)
file.close()

# question 3
file=open('demo.txt','a')
file.write("\nthis is pyhton course")
file.close()

file=open('demo.txt','r')
content =file.read()
print('content after appending:\n',content)
file.close()
