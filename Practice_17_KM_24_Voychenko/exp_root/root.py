def root2(num):
    try: 
        num = float(num)
    except:
        return 'Error'
    else:
        return num**(1/2)

def root3(num):
    try: 
        num = float(num)
    except:
        return 'Error'
    else:
        return num**(1/3)