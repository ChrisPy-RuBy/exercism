def calculate(text_input):
    big_dict = dict()
    
    # parse input
    text_list = list(text_list)
    

    for x in text_input:
      try:
        big_dict[x] += 1
      except:
        big_dict[x] = 1
    return big_dict
