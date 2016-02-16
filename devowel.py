books = ['InfiniteJest', 'TheStranger', 'Dune', 'FreeWill']
vowels = list('aeiou')
output = []

def main():
	for book in books:
		book_list = list(book.lower())

		for vowel in vowels:
			while True:
				try:
					book_list.remove(vowel)
				except:
					break
		output.append(''.join(book_list).capitalize())

	print(output)

main()