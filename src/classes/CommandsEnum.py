from enum import Enum, auto
class Command(Enum):
	ADD_LIST = auto()
	REM_LIST = auto()
	ADD_ITEM = auto()
	REM_ITEM = auto()
	SHOW_LIST = auto()
	SHOW_TOTAL = auto()
	SHOW_ALL_LISTS_NAME = auto()

"""
AVAIABLE COMMAND:
ADD LIST -> add 'listname'

REM LIST -> rem 'listname'

ADD ITEM -> 'listname' 'price' 'description'

[(REM ITEM ->  del 'listname' 'price' 'description') || (REM ITEM ->  delete 'listname' 'price' 'description')] 

SHOW LIST -> show 'listname'

SHOW TOTAL LIST -> total 'listname'

"""
