import os, sys, string
import nltk
from nltk import *


def load_file(file):
	reviews, ratings = [], []
	# print("hello")
	with open(file,'r', encoding='utf-8') as f:
		flag = False
		# using for lopp
		for line in f:
			curr = line.strip().split('>')

			first_w = curr[0]
			curr_review, curr_rating = "", []
			if first_w == '<Content':
				flag = False
				curr_review = str(curr[1])
				if len(curr_review) < 50:
					continue
				flag = True
			elif first_w == '<Rating':
				# seven aspects
				if flag == False:
					continue
				flag = True
				curr_rating = curr[1].split('\t')
				if -1 in curr_rating:
					continue
			if flag:
				if curr_review:
					reviews.append(curr_review)
				if curr_rating:
					ratings.append(curr_rating)
	f.close()
	return reviews, ratings

def read_stop_words(file):
	stop_words = []
	f = open(file,'r')
	cnt = 0
	for line in f:
		stop_words.append(line.strip('\n'))
		cnt += 1
	return stop_words

def count_word_in_reivew(review):
	word_list = set([])
	for sentence in review:
		words = sentence.split(" ")
		for word in words:
			if word not in word_list:
				word_list.add(word)
	# for every review
	for word in word_list:
		if word not in total_freq:
			total_freq[word] = 1
		else:
			total_freq[word] += 1

# convert all the words into lower cases
# removing punctuations, stop   words
def parse_to_sentence(reviews):
	res = []
	# remove stopword
	for review in reviews:
		sentences = nltk.sent_tokenize(review)
		curr = []
		for sentence in sentences:
			tmp = sentence.lower()
			# remove punctuations
			for ch in tmp:
				if ch in punctuations:
					tmp = tmp.replace(ch, "")
			# remove stopword
			arr = tmp.split(" ")
			for word in arr:
				if word in stop_words or not word:
					# print(str(word))
					arr.remove(word)
			curr.append(tmp)
		res.append(curr)

		count_word_in_reivew(curr)

	return res

stop_words = read_stop_words('./stopwords.dat')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
dir = '../../Data/Reviews/'
total_freq = {}		# words with occurrences in reviews

# f = open(dir+"hotel_111823", "r")

aspect_list = ["room", "location","value", "cleanliness", "service"]
value_var = ["value"]
service_var = ["service"]
location_var = ["location"]
room_var = ["room"]
cleanliness_var = ["clean"]

# fp = open('words.txt','a+')
fp2 = open('../../Data/Seeds/hotel_bootstrapping.dat', 'w')
cnt = 0
num = 0
for f_name in os.listdir(dir):
	print(num)
	num += 1
	print(f_name, dir+f_name)
	reviews, ratings = load_file(dir + f_name)
	processed_res = parse_to_sentence(reviews)
# print(total_freq)

# sorted_dict = {}
# sorted_keys = sorted(total_freq, key=total_freq.get)
# for w in sorted_keys:
#     sorted_dict[w] = total_freq[w]

# write total word occurrence
# print(total_freq)
new_dict = {}
for word in total_freq:
	if word not in stop_words:
		new_dict[word] = total_freq[word]

value_list = ["value", "price","expensive", "money","cheap"]
service_list = ["service", "manager", "breakfast", "pool"]
location_list = ["location", "locate","position","latitude", "longitude"]
room_list = ["room", "rooms"]
cleanliness_list = ["clean", "dirty", "mess"]

val10 = list(sorted(new_dict.values()))[-13]

# aspect_list = ["room", "location","value", "cleanliness", "service"]
# value_var = ["value"]
# service_var = ["service"]
# location_var = ["location"]
# room_var = ["room"]
# cleanliness_var = ["clean"]

for word in new_dict:
	if total_freq[word] >= val10:
		if word in value_list and word not in value_l:
			value_var.append(word)

		### werewr
		elif word in service_list and word not in service_l:
			service_var.append(word)
		elif word in location_list and word not in location_l:
			location_var.append(word)
		elif word in room_list and word not in room_l:
			room_var.append(word)
		elif word in cleanliness_list and word not in cleanliness_l:
			cleanliness_var.append(word)

for i in aspect_list:
	fp2.write('<' + str(i) + '>')
	if i == "value":
		for j in value_var:
			fp2.write(" " + j)
		fp2.write("\n")
	# if i == "room":
	# 	for j in room_var:
	# 		fp2.write(" " + j)
	# 	fp2.write("\n")
	# if i == "location":
	# 	for j in location_var:
	# 		fp2.write(" " + j)
	# 	fp2.write("\n")
	if i == "cleanliness":
		for j in cleanliness_var:
			fp2.write(" " + j)
		fp2.write("\n")
	if i == "service":
		for j in service_var:
			fp2.write(" " + j)
		fp2.write("\n")
	if i == "room":
		for j in room_var:
			fp2.write(" " + j)
		fp2.write("\n")
	if i == "location":
		for j in location_var:
			fp2.write(" " + j)
		fp2.write("\n")
fp2.close()
