# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# FEDERAL UNIVERSITY OF UBERLANDIA
# Faculty of Electrical Engineering
# Biomedical Engineering Lab
# ------------------------------------------------------------------------------
# Author: Italo Gustavo Sampaio Fernandes
# Contact: italogsfernandes@gmail.com
# Git: www.github.com/italogfernandes
# ------------------------------------------------------------------------------
# Decription:
# ------------------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------


class Example:
    def __init__(self):
        pass
    def do_something(self):
        """
        Description.
    
        Parameters
        ----------
        
        Returns
        -------
    
        """
        pass


def test():
    my_example = Example()
    while True:
        print('-------------------------------')
        print('Example File')
        print('-------------------------------')
        print('Menu')
        print('-------------------------------')
        print('i - Info')
        print('q - Quit')
        print('-------------------------------')
        
        if sys.version_info.major == 2:
            str_key = raw_input()
        else:
            str_key = input()
        
        if str_key == 'q':
            break
        elif str_key == 'i':
        	print("This is a example")

if __name__ == '__main__':  # if we're running file directly and not importing it
   test()
