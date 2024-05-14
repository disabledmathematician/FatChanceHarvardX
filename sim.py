import random
import string
import matplotlib.pyplot as plt

# Charles Truscott while studying Fat Chance - Probability and Statistics with Harvard University
# By the subtraction rule, this simulation inspired by 6.002x should converge to 26^4 - 26
# The probability of four of the same letters in a 26 non case sensitive enumeration of all possibilities, 26/26^4 or
def RunSim():
""" ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Conditional Probability: 5.689576695493855e-05, millionths of a chance: 56.89576695493855
Simulation Probability: 1.6959315150029762e-05, millionths of a chance: 16.959315150029763 
Number of total possible characters minus the latter case in point: 0.9999431042330451, and 0.9999830403972267
"""
	random.seed(1)
	outcomes = []
	letters = []
	for letter in string.ascii_uppercase:
		letters.append(letter)
	print(letters)
	for trial in range(26 ** 4):
		s = ""
		for n in range(4):
			s += random.choice(letters)
			outcomes.append(s)
		s = ""
	same_caught = 0
	total = 0
#	all_outcomes = 26 ** 4
	for outcome in outcomes:
		if outcome == "AAAA":
			same_caught += 1
		elif outcome == "BBBB":
			same_caught += 1
		elif outcome == "CCCC":
			same_caught += 1
		elif outcome == "DDDD":
			same_caught += 1
		elif outcome == "EEEE":
			same_caught += 1
		elif outcome == "FFFF":
			same_caught += 1
		elif outcome == "GGGG":
			same_caught += 1
		elif outcome == "HHHH":
			same_caught += 1
		elif outcome == "IIII":
			same_caught += 1
		elif outcome == "JJJJ":
			same_caught += 1
		elif outcome == "KKKK":
			same_caught += 1
		elif outcome == "LLLL":
			same_caught += 1
		elif outcome == "MMMM":
			same_caught += 1
		elif outcome == "NNNN":
			same_caught += 1
		elif outcome == "OOOO":
			same_caught += 1
		elif outcome == "PPPP":
			same_caught += 1
		elif outcome == "QQQQ":
			same_caught += 1
		elif outcome == "RRRR":
			same_caught += 1
		elif outcome == "SSSS":
			same_caught += 1
		elif outcome == "TTTT":
			same_caught += 1
		elif outcome == "UUUU":
			same_caught += 1
		elif outcome == "VVVV":
			same_caught += 1
		elif outcome == "WWWW":
			same_caught += 1
		elif outcome == "XXXX":
			same_caught += 1
		elif outcome == "YYYY":
			same_caught += 1
		elif outcome == "ZZZZ":
			same_caught += 1
		else: 
			total += 1
	print("Conditional Probability: {}, millionths of a chance: {}".format(26 / 26 ** 4, 26 / 26 ** 4 * 1000000))
	print("Simulation Probability: {}, millionths of a chance: {} ".format(same_caught / len(outcomes), same_caught / len(outcomes) * 1000000))
	print("Number of total possible characters minus the latter case in point: {}, and {}".format((26 ** 4 - 26) / 26 ** 4, (total - same_caught) / total))
#	plt.hist(outcomes)
#	plt.show()
# Charles Truscott Watters
# Very Proud of enrolling in Harvard Centre for Continuing Education courses, great revision of 6.002x optimisation models, graphs trees walks, divide and conquer, probability and statistics. Thank you John Guttag, Ana Bell and Eric Grimson
RunSim()