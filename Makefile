##
## EPITECH PROJECT, 2020
## Python Makefile
## File description:
## Makefile
##

NAME1 = challenge01

NAME1F = challenge01.py

NAME2 = challenge02

NAME2F = challenge02.py

NAME3 = challenge03

NAME3F = challenge03.py

NAME4 = challenge04

NAME4F = challenge04.py

NAME5 = challenge05

NAME5F = challenge05.py

NAME6 = challenge06

NAME6F = challenge06.py

RM = rm -f

all: ${NAME1} ${NAME2} ${NAME3} ${NAME4} ${NAME5} ${NAME6}

$(NAME1):
	cp ${NAME1F} ${NAME1}
	chmod +x ${NAME1}

$(NAME2):
	cp ${NAME2F} ${NAME2}
	chmod +x ${NAME2}

$(NAME3):
	cp ${NAME3F} ${NAME3}
	chmod +x ${NAME3}

$(NAME4):
	cp ${NAME4F} ${NAME4}
	chmod +x ${NAME4}

$(NAME5):
	cp ${NAME5F} ${NAME5}
	chmod +x ${NAME5}

$(NAME6):
	cp ${NAME6F} ${NAME6}
	chmod +x ${NAME6}

clean:
	${RM} ${NAME1} ${NAME2} ${NAME3} ${NAME4} ${NAME5} ${NAME6}

fclean:
	${RM} ${NAME1} ${NAME2} ${NAME3} ${NAME4} ${NAME5} ${NAME6}

re: clean all

.PHONY: all re clean fclean