TODO: Reflect on what you learned this week and what is still unclear.
def apply_rules(letter, guard):
            """
        if letter == "a":
            return "bba"
        elif letter == "b":
            return "aob"
        elif letter == "o":
            return "oa"
        else:
            return letter

    part_new = list(source)
    # result = list(map(apply_rules, part_new, guard)) 
    # --> function does not work in updated version of python use below 
    result = [apply_rules(part, guard) for part in part_new]
    new_abba = "".join(result)
    # " " doesnt work as there is no space in abba
    guard -= 1
    if guard > 0:
        return abba(new_abba, guard)
    else:
        return new_abba
    