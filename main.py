import json
import math
alphabeth_lowercase = 'abcdefghijklmnopqrstuvwxyz '

combinations_1 = {}
combinations_2 = {}
combinations_3 = {}
counter = 0

def combinations():
    '''
    Make combinations of every letter in the alphabet
    Receives:
        NULL 
    Return:
        NULL
    '''
    for letter in alphabeth_lowercase:
        combinations_1[letter] ={'Repeticion':0,
                                 'Probabilidad':0
                                 }
        for second_letter in alphabeth_lowercase:
            combinations_2[letter+second_letter] ={'Repeticion':0,
                                 'Probabilidad':0
                                 }
        for third_letter in alphabeth_lowercase:
            combinations_3[letter+second_letter+third_letter] ={'Repeticion':0,
                                 'Probabilidad':0
                                 }
 
def read_file():
    '''
    Read file 
    Receives:
        NULL
    Return:
        total_char_one,total_char_two,total_char_three type int
    '''
    with open('book_fr.txt', 'r') as file:
        cont = 0
        total_char_one = 0
        total_char_two = 0
        total_char_three = 0
        for line in file:
            cont+=1
            for value in combinations_1.keys():
                counter = line.count(value)
                combinations_1[value]["Repeticion"]= combinations_1[value]["Repeticion"] + counter
                total_char_one = total_char_one+counter
            for value in combinations_2.keys():
                counter = line.count(value)
                total_char_two = total_char_two +counter
                combinations_2[value]["Repeticion"]= combinations_2[value]["Repeticion"] + counter
            for value in combinations_3.keys():
                counter = line.count(value)
                total_char_three = total_char_three+ counter
                combinations_3[value]["Repeticion"]= combinations_3[value]["Repeticion"] + counter
        return total_char_one,total_char_two,total_char_three
                
def probability(total_char_one,total_char_two,total_char_three):
    '''
    Calculates the probability of the occurrence of a character
    
    Receives:
        total_char_one,total_char_two,total_char_three
    Return:
        NULL
    '''
    average_length_1 =0
    average_length_2 =0
    average_length_3 =0
    
    for value in combinations_1.values():
        value['Probabilidad'] = value['Repeticion']/total_char_one
        average_length_1 = average_length_1 +value['Probabilidad'] 
    for value in combinations_2.values():
        value['Probabilidad'] = value['Repeticion']/total_char_two
        average_length_2 = average_length_2 +value['Probabilidad'] 
    for value in combinations_3.values():
        value['Probabilidad'] = value['Repeticion']/total_char_three  
        average_length_3 = average_length_3 +value['Probabilidad'] 
    return average_length_1, average_length_2, average_length_3

def entropy():
    entropy_1 = 0
    entropy_2 = 0
    entropy_3 = 0
    for value in combinations_1.values():
        try:
            entropy_1 = entropy_1+ value['Probabilidad'] * math.log2(1/value['Probabilidad'])
        except:
            entropy_1 = entropy_1+0
    for value in combinations_2.values():
        try:
            entropy_2 = entropy_2+ value['Probabilidad'] * math.log2(1/value['Probabilidad'])
        except:
            entropy_2 = entropy_2+0

    for value in combinations_3.values():
        try:
            entropy_3 = entropy_3+ value['Probabilidad'] * math.log2(1/value['Probabilidad'])
        except:
            entropy_3 = entropy_3+0
    return entropy_1, entropy_2, entropy_3 



def source_efficiency(average_length_1, average_length_2, average_length_3,\
                      entropy_1, entropy_2, entropy_3):
    source_efficiency_1 = entropy_1/average_length_1
    source_efficiency_2 = entropy_2/average_length_2
    source_efficiency_3 = entropy_3/average_length_3
    return source_efficiency_1, source_efficiency_2,source_efficiency_3



if __name__ == "__main__":
    combinations()
    total_char_one,total_char_two,total_char_three = read_file()
    average_length_1, average_length_2, average_length_3=probability(\
        total_char_one,total_char_two,total_char_three)
    entropy_1, entropy_2, entropy_3 =entropy()
    source_efficiency_1, source_efficiency_2,source_efficiency_3= source_efficiency(\
        average_length_1, average_length_2, average_length_3,\
                      entropy_1, entropy_2, entropy_3)
    print(combinations_1)
    #print(entropy_2,json.dumps(combinations_2, indent=4))
    #print(entropy_3,json.dumps(combinations_3, indent=4))
    print("Entropia (longitud 1):", entropy_1)
    print("Eficiencia de la fuente (longitud 1):", source_efficiency_1)
    print("Longitud promedio (longitud 1):", average_length_1)
    for k,v in combinations_1.items():
        for val in v.values():
            print(k,val)
    #print("Entropia longitud 2:", entropy_2)
    #print("Entropia longitud 3:", entropy_3)
    
    
