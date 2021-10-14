def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return(str)
    dup = ""
    for i in range(0, len(str)):
        if i != n:
            dup = dup + str[i]
    return(dup)
