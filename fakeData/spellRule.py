# -*- coding: utf-8 -*-
# @Author: t-yubai
# @Date:   2016-07-22 10:27:10
# @Last Modified by:   t-yubai
# @Last Modified time: 2016-07-22 13:59:01

import re
import random
import string

class spellRule(object):
	"""This class is used to add some wrong spell rules"""

	fmap ={
		'ly' : lyIssue,
		'doubleToSingle' : doubleToSingleIssue,
		'missing' : missingCharIssue,
		'surplus' : surplusIssue
		'random' : randomIssue
	}

	def lyIssue(seg):
		res = []
		if(seg[-2:] != 'ly'):
			return res
		else:
			newSeg = seg[:-2] + 'ies'
			res.append(newSeg)
			return res

	def doubleToSingleIssue(seg):
		res = []
		Len = len(seg)
		pos = []
		for i in xrange(0,Len):
			if(i < len - 1 and seg[i+1] == seg[i]):
				pos.append(i)
		for p in pos:
			newSeg = seg[:p] + seg[p + 1:]
			res.append(newSeg)
		return res


	def missingCharIssue(seg):
		Len = len(seg)
		res = []
		for i in range(0, Len):
			p = random.randint(0, Len - 1)
			newSeg = seg[:p] + seg[p+1:]
			res.append(newSeg)
		return res

	def surplusIssue(seg):
		Len = len(seg)
		res = []

		for i in range(0, Len):
			p = random.randint(0, Len - 1)
			newSeg = seg[:p] + seg[p] + seg[p+1:]
			res.append(newSeg)
		return res

	def randomIssue(seg):
		Len = len(seg)
		res = []

		for i in range(0, Len):
			p = random.randint(0, Len - 1)
			c = random.choice(string.ascii_lowercase)
			newSeg = seg[:p] + c + seg[p+1:]
			res.append(newSeg)
		return res

	def addRule(fun, name):
		fmap[name] = fun

	def __init__(self, arg):
		super(spellRule, self).__init__()
		self.arg = arg
		