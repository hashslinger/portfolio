# This script will parse the video game txt and make a JSON file structured the way our viz will use it

## Important
## Important

# regex is not picking up all the games yet. 15000 missing

## Important
## Important
import re
import json

def parse_video_games(game_file):
	makers = {}
	platforms = {}
	n_bad = 0
	n_good = 0

	sorted_by_n_games = []
	for i, line in enumerate(game_file):
		m = re.match(r"(.+?)(\(.+?\))? \((\d{4}), (.+?)(\(.+?\))?\) \((.+)\)", line)

		#some lines dont match yet
		if not m:
			n_bad += 1
			

		#these we matches successfully ~75000
		else:
			maker = m.group(4).strip()

			# if maker == '?' or maker == 'author':
			# 	continue

			title = m.group(1).strip()
			year = int(m.group(3).strip())
			platform = m.group(6).strip()

			if maker.replace(' ', '') in makers:
				maker = maker.replace(' ', '')

			if maker not in makers:
				makers[maker] = {}
				makers[maker]['minyear'] = makers[maker]['maxyear'] = year
				makers[maker]['count'] = 1
			else:
				makers[maker]['minyear'] = \
					min(year, makers[maker]['minyear'])
				makers[maker]['maxyear'] = \
					max(year, makers[maker]['maxyear'])
				makers[maker]['count'] += 1


			makers[maker][title] = {
				'year': year,
				'platform': platform
			}
			if platform in platforms:
				platforms[platform] += 1
			else:
				platforms[platform] = 0

			# n_good += 1
			# string = ''
			# for group in m.groups():
			# 	if group:
			# 		newgroup = group.strip().replace('(', '')
			# 		newgroup = newgroup.replace(')', '') 
			# 		string += newgroup + ', '
			# print string

		# if i == 1000:
		#  	break
		if i % 1000 == 0:
		 	print i
	# print 'good:', n_good, 'bad: ', n_bad
	return makers


def stats_report(makers):
	print len(makers.keys()), 'makers'

	print 'biggest makers:'
	n_games_by_maker = []
	n_games = 0
	for maker in makers:
		n_games += makers[maker][0]
		n_games_by_maker.append( (maker, makers[maker][0]) ) 
	blah = sorted(n_games_by_maker, key=lambda maker: maker[1], reverse=True)
	string = ''
	for i in range(0,30):
		print blah[i],
	print '\ntotal of ', n_games, ' games'

def show_maker(maker):
	for game in maker:
		print game

def clean_data(makers):
	makers.pop('', None)

makers = parse_video_games(open('allofthegames.txt'))
clean_data(makers)
json_file = open('allofthegamesjson.json', 'w')
json_file.write(json.dumps(makers))

# stats_report(makers)
