import argparse
import unittest 
from search_routine import perform_search

class TestSearchRoutine(unittest.TestCase):
	"""
	Test case class for search routine module
	"""
	def setUp(self):
		"""
		use steup to initialize the argument parser
		"""
		self.parser = self.create_parser()
	
	def create_parser(self):
		"""
		Argument parser
		"""
		_parser = argparse.ArgumentParser(description='Search your keyword in news ex: search_routine.py -o or -p Care,Quality,Commission')
		_parser.add_argument('-o','--operator', type=str, help='Search operator or/and only ', default='or')
		_parser.add_argument('query', type=str, help='search query')
		return _parser
	
	def test_perform_search_query_one(self):
		"""
		Test case for first query
		i.e. python search_routine.py -o or "Care Quality Commission admission"
		"""
		parsed=self.parser.parse_args(['-o', 'or','Care Quality Commission admission'])
		result = perform_search(parsed)
		self.assertEqual(result,'0,1,2,3,4,5,6')
	
	def test_perform_search_query_second(self):
		"""
		Test case for second query
		i.e. python search_routine.py -o or "September 2004"
		"""
		parsed=self.parser.parse_args(['-o', 'or','September 2004'])
		result = perform_search(parsed)
		self.assertEqual(result,'9')
	
	def test_perform_search_query_third(self):
		"""
		Test case for third query
		i.e. python search_routine.py -o or "general population generally"
		"""
		parsed=self.parser.parse_args(['-o', 'or','general population generally'])
		result = perform_search(parsed)
		self.assertEqual(result,'6,8')
	
	def test_perform_search_query_fourth(self):
		"""
		Test case for fourth query
		i.e. python search_routine.py -o and "Care Quality Commission admission"
		"""
		parsed=self.parser.parse_args(['-o', 'and','Care Quality Commission admission'])
		result = perform_search(parsed)
		self.assertEqual(result,'1')
	
	def test_perform_search_query_fifth(self):
		"""
		Test case for fifth query
		i.e. python search_routine.py -o and "general population Alzheimer"
		"""
		parsed=self.parser.parse_args(['-o', 'and','general population Alzheimer'])
		result = perform_search(parsed)
		self.assertEqual(result,'6')
	