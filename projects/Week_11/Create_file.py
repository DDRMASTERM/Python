# Files can be opened with the following
#	'r' = read only
#	'w' = write
#	'a' = append
#	'r+' = read/write
# A file opened in write mode will overwrite any 
# existing contents in the file. 


file_name = 'hello_world.txt'
with open(file_name) as f:
	contents = f.read()
	print(contents)

file_name = 'bye_world.txt'
with open(file_name) as f:
	for line in f:
		print(line.strip())

file_name = 'bye_world.txt'
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
            print(line.strip())

file_name = 'write_hello.txt'
with open(file_name, 'w') as f:
     f.write('Hello world!')

with open(file_name, 'a') as f:
     f.write('Hello polly!')

with open(file_name) as f:
	for line in f:
		print(line.strip())
