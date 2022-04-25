def reverse_order(string):
  
  while True:
    # string = input("Enter a sentence and I will reverse it: ")
    try:
      str_list = string.split(' ')
      str_list[0] = str_list[0].lower()
      str_list[len(str_list)-1] = str_list[len(str_list)-1].title()
      new_str = []
      punct_list = []
      counter=0
      
      # split string into blocks separated by punctuations
      str_block=''
      for e in str_list:
        
        if (e[len(e)-1]==',' or e[len(e)-1]=='.' or e[len(e)-1] =='?'):
          punct_list.append(e[len(e)-1])
          str_block = f"{str_block} {e[:len(e)-1]}"
          counter+=1
          new_str.append(str_block)
          str_block=''
        else:
          str_block = f"{str_block} {e}"
          if e == str_list[len(str_list)-1]:
            new_str.append(str_block)
          
      # reverse list
      rev_list = []
      for e in new_str:
        
        block = e.strip().split(' ')
        block.reverse()
    
        rev_list.append(' '.join(block))
    
      rev_list.reverse()

      # append punctuations at appropriate positions.
      string=''
      for i, item in enumerate(rev_list):
        if i < len(punct_list):
          string += f"{item}{punct_list[i]} "
        else:
          string += f"{item}"
      break
    except:
      print("Inappropriate input entered")
    
      

  return f"\n\n{string}"

print(reverse_order("Hello. I'm Edwin A.J, and you?"))
"Hello. I'm Edwin A.J, and you?"
"What time is it? Hammer time."
