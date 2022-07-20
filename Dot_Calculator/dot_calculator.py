def calculator(txt):
    count_string = lambda x: str(x.count('.'))
    
    txt = txt.split(" ")
    
    first = count_string(txt[0])
    second = count_string(txt[2])
    
    result = eval(first + txt[1] + second)
    return "." * result