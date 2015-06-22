all: test

test: singly_linked_list.py
	py.test $<

singly-linked-list-test: singly-linked-list.h \
	singly-linked-list.c \
	singly-linked-list-test.py
	py.test singly-linked-list-test.py

doubly-linked-list-test: doubly-linked-list.h \
	doubly-linked-list.c \
	doubly-linked-list-test.py
	py.test doubly-linked-list-test.py


clean:
	rm -f singly-linked-list{,.dylib}
	rm -f doubly-linked-list{,.dylib}
	rm -rf __pycache__ *.pyc
