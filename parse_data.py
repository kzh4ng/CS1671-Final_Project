import json

def parse_all_reviews_by_season():
	reviews = []
	with open('yelp_academic_dataset_review.json') as f:
		for line in f:
			reviews.append(json.loads(line))

	winter = []
	spring = []
	summer = []
	fall = []

	wintermonths = {'12': None, '01': None, '02': None}
	springmonths = {'03': None, '04': None, '05': None}
	summermonths = {'06': None, '07': None, '08': None}
	fallmonths = {'09': None, '10': None, '11': None}

	for r in reviews:
		month = r['date'][5:7] 
		if month in wintermonths:
			winter.append(r)
		elif month in springmonths:
			spring.append(r)
		elif month in summermonths:
			summer.append(r)
		else: # month in fallmonths
			fall.append(r)

	winterfile = open("winter.txt", "w")
	springfile = open("spring.txt", "w")
	summerfile = open("summer.txt", "w")
	fallfile = open("fall.txt", "w")

	print len(winter)
	print len(spring)
	print len(summer)
	print len(fall)

	for item in range(0, len(winter)/20):
		winterfile.write(str(winter[item]) + "\n")

	for item in range(0, len(spring)/20):
		springfile.write(str(spring[item]) + "\n")

	for item in range(0, len(summer)/20):
		summerfile.write(str(summer[item]) + "\n")		

	for item in range(0, len(fall)/20):
		fallfile.write(str(fall[item]) + "\n")

	winterfile.close()
	springfile.close()
	summerfile.close()
	fallfile.close()


def get_city_list():
	cities = open("city_list.txt", "w")
	places = []
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			places.append(json.loads(line))

	city_dict = dict()
	for p in places:
		city = p['city']
		if city in city_dict:
			city_dict[city].append(p)
		else: # new city
			city_dict[city] = list(p)

	for c in city_dict.keys(): 
		cities.write(c) 

def parse_by_city(city):
	business_list = []
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			business_list.append(json.loads(line))
	city_business_list = []
	for b in business_list:
		if b['city'] == city:
			city_business_list.append(b['business_id'])
	return city_business_list

def get_reviews_from_business_list(business_list):
	reviews = []
	subset_reviews = []

	with open('yelp_academic_dataset_review.json') as f:
		for line in f:
			reviews.append(json.loads(line))

	# create dict to improve runtime.
	business_dict = dict()
	for b in business_list:
		business_dict[b] = True

	print len(business_dict)
	print len(reviews)
	count = 0 
	for r in reviews:
		if count % 100000 == 0:
			print count
		curr_b_id = r['business_id']
		if curr_b_id in business_dict:
			subset_reviews.append(r)
		count += 1
	return subset_reviews

def sort_reviews_by_season(reviews, city):
	winter = []
	spring = []
	summer = []
	fall = []

	wintermonths = {'12': None, '01': None, '02': None}
	springmonths = {'03': None, '04': None, '05': None}
	summermonths = {'06': None, '07': None, '08': None}
	fallmonths = {'09': None, '10': None, '11': None}

	print len(reviews)
	for r in reviews:
		month = r['date'][5:7] 
		if month in wintermonths:
			winter.append(r)
		elif month in springmonths:
			spring.append(r)
		elif month in summermonths:
			summer.append(r)
		else: # month in fallmonths
			fall.append(r)

	winterfile = open("winter-" + city + ".txt", "w")
	springfile = open("spring-" + city + ".txt", "w")
	summerfile = open("summer-" + city + ".txt", "w")
	fallfile = open("fall-" + city + ".txt", "w")

	print len(winter)
	print len(spring)
	print len(summer)
	print len(fall)


	winterfile2 = open("winter-" + city + ".json", "w")
	springfile2 = open("spring-" + city + ".json", "w")
	summerfile2 = open("summer-" + city + ".json", "w")
	fallfile2 = open("fall-" + city + ".json", "w")

	winterfile3 = open("winter-" + city + "-training.json", "w")
	springfile3 = open("spring-" + city + "-training.json", "w")
	summerfile3 = open("summer-" + city + "-training.json", "w")
	fallfile3 = open("fall-" + city + "-training.json", "w")

	for item in range(0, len(winter)/20):
		winterfile.write(str(winter[item]) + "\n")
		json.dump(winter[item], winterfile2)
		winterfile2.write("\n")
		if item % 20 == 0:
			json.dump(winter[item], winterfile3)
			winterfile3.write("\n")

	for item in range(0, len(spring)/20):
		springfile.write(str(spring[item]) + "\n")
		json.dump(spring[item], springfile2)
		springfile2.write("\n")
		if item % 20 == 0:
			json.dump(spring[item], springfile3)
			springfile3.write("\n")

	for item in range(0, len(summer)/20):
		summerfile.write(str(summer[item]) + "\n")		
		json.dump(summer[item], summerfile2)
		summerfile2.write("\n")
		if item % 20 == 0:
			json.dump(summer[item], summerfile3)
			summerfile3.write("\n")

	for item in range(0, len(fall)/20):
		fallfile.write(str(fall[item]) + "\n")
		json.dump(fall[item], fallfile2)
		fallfile2.write("\n")
		if item % 20 == 0:
			json.dump(fall[item], fallfile3)
			fallfile3.write("\n")

# Generate four text files, by season, of reviews for a specific city.
pittsburgh_business_list = parse_by_city("Pittsburgh")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "pittsburgh")




