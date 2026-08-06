def find_common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common_chars = set1.intersection(set2)

    return common_chars


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = find_common_characters(str1, str2)

print("Common characters:", common_chars)