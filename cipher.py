import re
import random
import nltk
from nltk.corpus import words
nltk.download('words')
english = words.words()

def encript(string, key):
	"""Takes in a string and a key and will apply the ceaser cipher to the string based on the key. Then returning the result"""

	alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_str = ''

	for char in string.lower():
		if char in alp:
			new_str += alp[(alp.index(char) + key) % len(alp)]
		else:
			new_str += char

	return new_str


def decript(string, key):
	"""Works the encript function backwards"""
	return encript(string, -key)


def decript_bot(string):

	def check_correct(string):
		"""A helper function that takes in a string and returns a number for how many of those words are in the english language"""
		count = 0.0
		words = re.findall(r"[a-zA-Z]+", string)
		for word in words:
			if word in english:
				count += 1.0
		return count / len(words)
	
	while check_correct(string) < .5:
		string = decript(string, 1)
	return string

if __name__ == "__main__":
# 	string = """Hyperbolic Tangent and Derivative
# It has a structure very similar to Sigmoid function. However, this time the function is defined as (-1, + 1). The advantage over the sigmoid function is that its derivative is more steep, which means it can get more value. This means that it will be more efficient because it has a wider range for faster learning and grading."""
	string = "z yfgv kyrk ze kyzj pvri kf tfdv, pfl drbv dzjkrbvj. svtrljv zw pfl riv drbzex dzjkrbvj, kyve pfl riv drbzex evn kyzexj, kipzex evn kyzexj, cvriezex, czmzex, gljyzex pflijvcw, tyrexzex pflijvcw, tyrexzex pfli nficu. pfl'iv ufzex kyzexj pfl'mv evmvi ufev svwfiv, reu dfiv zdgfikrekcp, pfl'iv ufzex jfdvkyzex."
	key = random.randint(0, 27)
	print(f"Key: {key}")
	print(f"Current Input:\n{string}")
	string = encript(string, key)

	print(f"Encripted String: \n{string}")
	print(f"Decripted By Bot: \n{decript_bot(string)}")


