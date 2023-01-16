def main(first_num:int,past_num:int,method:str):
    if method=="+":   return first_num + past_num
    elif method=="-": return first_num - past_num
    elif method=="*": return first_num * past_num
    elif method==":": return first_num / past_num
    else:             print('Error, try again.')

print(main(1,2,'+'))