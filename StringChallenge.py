 # -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:38:49 2022

@author: bosimanurung
"""

def StringChallenge(strParam):
    # not_here = [" ", "-", "!", "@", ".", "#", "\", "/", "%", "&", "^", "*", "(", ")", "_", "=", "+"]
    specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", "_", "=", "<", ">", "/", " "]
    first = 1
    result = result_k = ""
    count = 0
    for i in strParam:
        count += 1
        if i in specialChars:
            if (first==1):                
                for j in range (0,count-1):
                    result += strParam[j].lower() #Daniel LikeS-coding result: DanielLikesCoding
                    print(result)
                first += 1                      #cats AND*Dogs-are Awesome result: CatsAndDogsAreAwesome
                count_first = count
                result = result.capitalize()
            else:
                result_k = ""
                for k in range (count_first,count-1):
                    result_k += strParam[k].lower()
                    print(result_k)
                first += 1
                count_first = count
                result += result_k.capitalize()

    result_k = ""
    for k in range (count_first,count):
        result_k += strParam[k].lower()
        print(result_k)
    first += 1
    result += result_k.capitalize()
                            
    strParam = result
    return strParam

print(StringChallenge("Daniel LikeS-coding")) #result: DanielLikesCoding
#print(StringChallenge("cats AND*Dogs-are Awesome")) #result: CatsAndDogsAreAwesome