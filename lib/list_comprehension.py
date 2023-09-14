#!/usr/bin/env python3

def return_evens(num_list):
    square_num=[num for num in num_list if num%2==0] 
    return square_num      
    

def make_exclamation(sentence_list):
    make_exclamation=[f'{sentence}!' for sentence in sentence_list]
    return make_exclamation
    pass