books = ['InfiniteJest', 'TheStranger', 'Dune', 'FreeWill']
vowels = list('aeiou')
output = []

def maind():
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

def main():
    the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

    # Your code goes below here

    del the_list[0]
    del the_list[3]
    del the_list[3]

    the_list.insert(0, the_list.pop(2))
    liss = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    the_list.extend(liss)

    print(the_list)

main()