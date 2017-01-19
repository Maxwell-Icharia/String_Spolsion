def string_spolsion(string):
	if len(string) > 1:
		counter = len(string) - (len(string) - 2)
		for x in string:
			counter = counter + 1
			return x * counter
		