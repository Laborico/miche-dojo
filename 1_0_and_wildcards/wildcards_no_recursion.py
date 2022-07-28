def possibilities(param):
    combinations = []
    
    for i, character in enumerate(param):
        if character == '?':
            if len(combinations):
                tmp = []
                for previos_com in combinations:
                    tmp.append(previos_com[:i] + "0" + previos_com[i+1:])
                    tmp.append(previos_com[:i] + "1" + previos_com[i+1:])
                combinations.extend(tmp)
            else:
                combinations.append(param[:i] + "0" + param[i+1:])
                combinations.append(param[:i] + "1" + param[i+1:])
   
    combinations = [comb for comb in combinations if "?" not in comb]

    return combinations