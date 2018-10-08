def roman_to_integer(r_str):
    roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(r_str)):
        if i > 0 and roman_val[r_str[i]] > roman_val[r_str[i - 1]]:
            int_val += roman_val[r_str[i]] - 2 * roman_val[r_str[i - 1]]
        else:
            int_val += roman_val[r_str[i]]
    return int_val


print roman_to_integer('IX')