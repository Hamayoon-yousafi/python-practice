#____________________________________________________first question

my_list = [12312, [23423,234], "something", ["test", 'test'], [23,43,3], "again", ["somehting"]]

def num_of_sublists(subject_list):
    """ this function counts sublists in a given list ignoring everything else in the list (e.g. string, integer) """
    total_number_sublists = 0
    for i in subject_list:
        if isinstance(i, list):
            total_number_sublists += 1
    return total_number_sublists 

print(f"Q1: The number of sublists: {num_of_sublists(my_list)}")


#___________________________________________________second question
# our list
list_for_gap = [9,4,26,26,0,0,5,20,6,25,5]
# sorting the list
list_for_gap.sort()
# we make each two elements in the list a couple. if an element is left alone wihtout couple then 0 will be its couple 
if not len(list_for_gap) % 2 == 0:
        list_for_gap.append(0) 
# making the list iterable so the method next() can work        
list_for_gap = iter(list_for_gap)
# we need to have list that contains each couple
couples = []
# running loop to append element and its couple to couples list
for i in list_for_gap: 
    x = next(list_for_gap)
    couples.append([i,x]) 
# having list for all the gaps between the given couples
gaps = []
# appending gaps to gaps[] list. ignoring 0 and gap below 0
for i in couples:
    gap = i[1] - i[0]
    if gap > 0:
        gaps.append(i[1] - i[0])
# getting largest gap from gaps list
largest_gap = max(gaps)
# printing the gap
print(f"Q2: the biggest gap between couples in given sorted list: {largest_gap}")

#___________________________________________________third question
def censor_string(message, words_tobe_censored, censoring_char):
    words_from_msg = message.split()

    for i in range(len(words_from_msg)): 
        for tobe_censored_word in words_tobe_censored:
            if words_from_msg[i] == tobe_censored_word:
                words_from_msg[i] = censoring_char * len(tobe_censored_word) 

    censored_sentence = ' '.join(words_from_msg)

    return censored_sentence

print(f"Q3: censored version of sentence: {censor_string('today is a wednesday.', ['today', 'a'], '_')}")  
 
