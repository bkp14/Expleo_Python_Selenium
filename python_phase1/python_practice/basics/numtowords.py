example = input("enter a number : ")
dict = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}


def words(example):
    for i in example:
       print(dict.get(i),end=" ")

words(example)                    
