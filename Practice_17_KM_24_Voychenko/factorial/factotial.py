def fact(num):
    try: 
        num = int(num)
    except:
        return 'Error'
    else:
        if num == 1:
            return 1
        return num * fact(num-1)
