<h1>Steps to run search_routine.py</h1>

python search_routine.py -h
usage: search_routine.py [-h] [-o OPERATOR] query

Search your keyword in news ex: search_routine.py -o or Care,Quality,Commission

positional arguments:
  query                 search query

optional arguments:
  -h, --help            show this help message and exit
  -o OPERATOR, --operator OPERATOR
                        Search query with operator or/and
				if you not pass OPERATOR it will take default value as *or*


example :
Using OR operator:
	 python search_routine.py   -o or "general population generally"
	 and
	 python search_routine.py   "general population generally"
	 above two will result same output
	 o/p:
		6,8
Using AND operator:
	 python search_routine.py   'Care Quality Commission admission' -o and
	 o/p:
		1