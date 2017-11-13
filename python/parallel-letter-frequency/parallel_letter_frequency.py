

def calculate(text_input):
    print (text_input)
    big_dict = dict()
    
    # # parse input
    pop_input = ""
    if type(text_input) == list:
        for x in text_input:
            pop_input += x
    else:
        pop_input = text_input
        print (pop_input)



    text_list = [char for char in pop_input]
    filtered_list = []
    for x in text_list:
     if x.isalpha():
       filtered_list.append(x.lower())

    print (filtered_list)
    for x in filtered_list:
      try:
        big_dict[x] += 1
      except:
        big_dict[x] = 1
    return big_dict
