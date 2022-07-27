combinations = []

def replace_char(index, string):
    if string[index] == "1":
        return string[:index] + "0" + string[index + 1:]
    if string[index] == "0":
        return string[:index] + "1" + string[index + 1:]

def turing_machine(question_marks_indices, new_param):
    global combinations
    for i, index in enumerate(question_marks_indices):
        new_param = replace_char(index, new_param)
        combinations.append(new_param)
        turing_machine(question_marks_indices[:i], new_param)
        new_param = replace_char(index, new_param)
    
def possibilities(param):
    global combinations
    combinations = []
    question_marks_indices = []
    
    for i, character in enumerate(param):
        if character == "?":
            question_marks_indices.append(i)
            
    param = param.replace("?", "0")
    
    combinations.append(param)
    
    turing_machine(question_marks_indices, param)
    return combinations