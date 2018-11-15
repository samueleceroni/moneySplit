from enum import Enum, unique
@unique
class CommandsEnum(Enum):
	ADD_LIST = 0
	REM_LIST = 1
	ADD_ITEM = 2
	REM_ITEM = 3
	SHOW_LIST = 4
	SHOW_TOTAL = 5
	SHOW_ALL_LISTS_NAMES = 6

"""

AVAIABLE COMMAND:
*-> = available with one list only
ADD LIST -> add 'listname'

REM LIST -> remlist 'listname'
        *-> remlist

REM ITEM ->  remitem 'listname' 'num'
        *->  remitem 'num'

SHOW LIST -> show 'listname'
         *-> show

SHOW TOTAL LIST -> total 'listname'

ADD ITEM -> 'listname' 'price' 'description'
        *-> 'price' 'description'

SHOW ALL LISTS NAME -> ls


"""
