def reverse_string(s):
    reverse = ""
    index = len(s)
    while index > 0:
        reverse += s[index - 1]
        index = index - 1
    return reverse
    
    
