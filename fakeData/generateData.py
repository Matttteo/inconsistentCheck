# -*- coding: utf-8 -*-
# @Author: t-yubai
# @Date:   2016-07-21 13:26:31
# @Last Modified by:   t-yubai
# @Last Modified time: 2016-07-22 13:59:00


class genFakeWordPair:
	#Three kind of fake data
	caseIssue = {}
	missingIssue = {}
	spellIssue = {}


	definitons = []



	def readFile(filename):
		with open(filename, 'rt') as f:
			for name in f:
				definitons.append(name[:-2])

	def readWord(word):
		definitons.append(word)


	def isLowCase(Char):
		return Char.islower()

	def genWordSeg(word):

		wordLen = len(word)
		wordSeg = []
		lo = 0
		for i in range(0, wordLen):
			if  isLowCase(word[i]) is False:
				if i + 1 < wordLen and isLowCase(word[i+1]) is False:
					abbreviation = ""
					while i < wordLen and isLowCase(word[i]) is False:
						abbreviation += word[i]
						i += 1
					wordSeg.append(abbreviation)
					lo = i
					continue
				else:
					if( i == 0 ): continue
					seg = word[lo:i]
					wordSeg.append(seg)
					lo = i
			else:
				i += 1
		wordSeg.append(word[lo:])
		return wordSeg


				
	def genCaseIssue():
        caseIssue = {}
        for word in definitons:
        	wordSeg = genWordSeg(word)
        	if len(wordSeg) == 1:
        		continue
        	else:
		        word0 = wordSeg[0]
		
		        if len(word0) == 0:
		        	return
		        if isLowCase(word0[0]):
		        	word0 = word0[0].upper() + word0[1:]
		        tmpword = []
		        caseIssue[word] = []
		    	__genCaseIssue(wordSeg, tmpword, word, 0)


    def __genCaseIssue(wordSeg, tmpword, word, idx):
        if len(tmpword) == len(wordseg):
        	data = ""
        	for part in tmpword:
        		data += part
        	caseIssue[word].append(data)
        	return
        for i in range(idx,len(wordseg)):
        	tmpword.append(wordseg[i])
        	__genCaseIssue(wordseg, tmpword, i + 1)
        	tmpword.pop()
        	wordseg[i] = wordseg[i][0].lower() + wordseg[i][1:]
        	tmpword.append(wordseg[i])
        	__genCaseIssue(wordseg, tmpword, i + 1)
        	tmpword.pop()

    def genMissingIssue():
    	missingIssue = {}
    	for word in definitons:
    		wordSeg = genWordSeg(word)
    		missingIssue[name] = []
    		for i in range(0, len(wordSeg)):
    			name = ""
    			for j in range(0, len(wordSeg)):
    				if(j == i):
    					continue
    				else:
    					name = name + wordseg[j]
    			missingIssue[word].append(name)

    def __genSpellIssue(wrongSpellDic, tmpword, word, idx):
    	if idx == len(wrongSpellDic):
    		data = ""
    		for part in tmpword:
    			data += part
    		spellIssue[word].append(data)
    		return
    	for i in range(0, len(wrongSpellDic[idx])):
    		tmpword.append[wrongSpellDic[idx][i]]
    		__genSpellIssue(wrongSpellDic, tmpword, word, idx + 1)
    		tmpword.pop()


    def genSpellIssue():
    	spellIssue = {}
    	for word in definitons:
    		wordSeg = genWordSeg(word)

    		wrongSpellDic = []
    		for i in range(0, len(wordSeg)):
    			wrongSpellDic.append(genWrongSpell(wordSeg[i]))
    		tmpword = []
    		spellIssue[word] = []
    		__genSpellIssue(wrongSpellDic, tmpword, word, 0)

    def genWrongSpell(seg):
    	wrongSpellList = []
    	for funName in spellIssueRule.fmap:
    		wrongSpellList.extend(spellIssueRule.fmap[funName](seg))
    	return wrongSpellList


    def writeToFile()）：
    '''TODO
    '''
    
	def __init__(self):
		self.caseIssue = {}
		self.missingIssue = {}
		self.spellIssue = {}
		self.definitons = []

		self.spellIssueRule = spellRule()