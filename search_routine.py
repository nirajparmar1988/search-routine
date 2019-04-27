import argparse

def parse_args():
	_parser = argparse.ArgumentParser(description='Search your keyword in news ex: search_routine.py -o or Care,Quality,Commission')
	_parser.add_argument('-o','--operator', type=str, help='Search query with operator or/and', default='or')
	_parser.add_argument('query', type=str, help='search query')
	return _parser.parse_args()

def perform_search(parsed_args):
	parameters = parsed_args.query.split(" ")
	result=[]
	counter = 0
	with open("hscic-news", "r") as news:
		for num, line in enumerate(news):
			for parameter in parameters:
				if parsed_args.operator.upper() == 'AND':
					if parameter in line:
						counter += 1
					else:
						counter = 0
					if counter == len(parameters):result.append(num)
				elif parsed_args.operator.upper() == 'OR':
					if all([parameter in line, num not in result]):
						result.append(num)
				else:
					return "provided search operator is not valid, please use or/and operator only"
	
	
	if not result:
		return "No Records found"
	result.sort()
	return ",".join(str(x) for x in result)

if __name__=='__main__':
	parsed_args = parse_args()
	result = perform_search(parsed_args)
	print(result)
	


