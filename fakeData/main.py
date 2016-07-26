from generateData import  genFakeWordPair

generator = genFakeWordPair()
generator.readFile('data.txt')
generator.genAndWrite()