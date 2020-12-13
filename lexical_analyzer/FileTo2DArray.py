
def fileTo2DArray(file_path):
	file = open(file_path, 'r')

	array = []

	file_lines = file.readlines()

	for line in file_lines:
		array.append(line.split('  '))

	return array
