from enum import Enum, auto

class CommandsEnum(Enum):
	ADD_LIST = auto()
	REM_LIST = auto()
	ADD_ITEM = auto()
	REM_ITEM = auto()
	SHOW_LIST = auto()
	SHOW_TOTAL = auto()
	SHOW_ALL_LISTS_NAMES = auto()

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
