def division(filename):
	try:
		with open(filename, 'r') as f:
			for line in f:
				line=line.split()
				if len(line) <2:
					print('Error: Too few numbers given')
					continue
				try:
					print(int(line[0])/int(line[1]))
				except ZeroDivisionError:
					print(f'Error: division by 0')
				except ValueError:
					print(f'Error: line contains non digits')

	except IOError:
		print(f'Cannot open this file {filename}')
	
division('check_file.txt')