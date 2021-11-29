from profanity_check import predict_prob

#First e need to open twitter sentence file in read mode

file = open("twitter-sentences.txt","r")

#And then reading each sentence in twitter file
for eachSentence in file.readlines():
	print(eachSentence)

	#degree of profanity of each sentence
	profanity = predict_prob(eachSentence)
	print(profanity)
