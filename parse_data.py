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

def print_city_list():
	places = []
	city_dict = {}
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			places.append(json.loads(line))

	city_dict = dict()
	for p in places:
		city = p['city']
		if city in city_dict:
			city_dict[city] += 1
		else: # new city
			city_dict[city] = 1

	city_dict_view = [ (v,k) for k,v in city_dict.iteritems() ]
	city_dict_view.sort(reverse=True) # natively sort tuples by first element
	for v,k in city_dict_view:
		print "%s: %d" % (k,v)

def get_all_categories():
	business_list = []
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			business_list.append(json.loads(line))
	categories_dict = dict()
	for b in business_list:
		curr_cats = b["categories"]
		for c in curr_cats:
			if c in categories_dict:
				categories_dict[c] += 1
			else:
				categories_dict[c] = 1
	return categories_dict


def parse_by_category(cat):
	business_list = []
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			business_list.append(json.loads(line))
	city_business_list = []
	for b in business_list:
		curr_cats = b['categories']
		if cat in curr_cats:
			city_business_list.append(b['business_id'])
	return city_business_list

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
	#return business_list

def parse_by_category_and_city(cat, city):
	business_list = []
	with open('yelp_academic_dataset_business.json') as f:
		for line in f:
			business_list.append(json.loads(line))
	city_business_list = []
	for b in business_list:
		curr_cats = b['categories']
		if cat in curr_cats:
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
		if item % 20 == 0:
			json.dump(winter[item], winterfile3)
			winterfile3.write("\n")
		else:
			#winterfile.write(str(winter[item]) + "\n")
			json.dump(winter[item], winterfile2)
			winterfile2.write("\n")

	for item in range(0, len(spring)/20):
		if item % 20 == 0:
			json.dump(spring[item], springfile3)
			springfile3.write("\n")
		else:
			#springfile.write(str(spring[item]) + "\n")
			json.dump(spring[item], springfile2)
			springfile2.write("\n")
		

	for item in range(0, len(summer)/20):
		if item % 20 == 0:
			json.dump(summer[item], summerfile3)
			summerfile3.write("\n")
		else:
			#summerfile.write(str(summer[item]) + "\n")		
			json.dump(summer[item], summerfile2)
			summerfile2.write("\n")
		
	for item in range(0, len(fall)/20):
		if item % 20 == 0:
			json.dump(fall[item], fallfile3)
			fallfile3.write("\n")
		else:
			#fallfile.write(str(fall[item]) + "\n")
			json.dump(fall[item], fallfile2)
			fallfile2.write("\n")
	
'''
business_list = parse_by_category("Pizza") 
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "pizza")

business_list = parse_by_category("Mexican") 
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "mexican")


business_list = parse_by_category("Sandwiches") 
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "sandwiches")

business_list = parse_by_category("Burgers")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "burgers")

business_list = parse_by_category("Fast Food")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "fast-food")

business_list = parse_by_category("Chinese")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "chinese")

business_list = parse_by_category("Breakfast & Brunch")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "breakfast-brunch")

business_list = parse_by_category("Italian")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "italian")

business_list = parse_by_category("Food")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "food")


business_list = parse_by_category("Restaurants")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "restuarants")

business_list = parse_by_category("Nightlife")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "nightlife")

business_list = parse_by_category("Bars")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "bars")

business_list = parse_by_category("Hotels & Travel")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "hotels-travel")

business_list = parse_by_category("Shopping")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "shopping")

business_list = parse_by_category("Auto Repair")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "auto-repair")

business_list = parse_by_category("Doctors")
print len(business_list)
reviews = get_reviews_from_business_list(business_list)
print len(reviews)
sort_reviews_by_season(reviews, "doctors")


#d = get_all_categories()
#for w in sorted(d, key=d.get, reverse=True):
#  print w, d[w]
'''

# Generate four text files, by season, of reviews for a specific city.
'''pittsburgh_business_list = parse_by_city("All")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "all")'''

'''
print "Las Vegas"
pittsburgh_business_list = parse_by_city("Las Vegas")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "lasvegas")

print "Phoenix"
pittsburgh_business_list = parse_by_city("Phoenix")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "phoenix")

print "Charlotte"
pittsburgh_business_list = parse_by_city("Charlotte")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "charlotte")

print "Madison"
pittsburgh_business_list = parse_by_city("Madison")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "madison")

print "Edinburgh"
pittsburgh_business_list = parse_by_city("Edinburgh")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "edinburgh")

print "Mesa"
pittsburgh_business_list = parse_by_city("Mesa")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "mesa")


pittsburgh_business_list = parse_by_city("Scottsdale")
print len(pittsburgh_business_list)
pittsburgh_reviews = get_reviews_from_business_list(pittsburgh_business_list)
print len(pittsburgh_reviews)
sort_reviews_by_season(pittsburgh_reviews, "scottsdale")
'''

