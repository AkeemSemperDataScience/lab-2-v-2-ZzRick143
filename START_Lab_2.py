def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    if (word == word[::-1]):
        return True
    else:
        return False

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    prev = 1
    curr = 2
    result = []
    if number_val > 0:
        result.append(0)
    if number_val > 1:
        result.append(1)
        result.append(1)
    while curr < number_val:
        result.append(curr)
        x = curr
        curr = curr + prev
        prev = x
    return result

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    str1 = str1.lower()
    amount = str1.count(str2)
    return amount

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    list1len = len(list1)
    list2len = len(list2)
    sum_list = []
    pos = 0
    if list1len != list2len:
        return sum_list
    while pos < list1len:
        sum_list.append(list1[pos]+list2[pos])
        pos = pos + 1
    return sum_list

def lab2Question5(password):
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    px = list(password)
    containsUpper = False
    containsLower = False
    containsNum = False
    if len(password) <= 7:
        return False
    for char in px:
        if char.isupper():
            containsUpper = True 
    if containsUpper == False:
        return False
    for char in px:
        if char.islower():
            containsLower = True
    if containsLower == False:
        return False
    for char in px:
        if char.isdigit():
            containsNum = True
    if containsNum == False:
        return False
    return True

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    px = list(password)
    containsUpper = False
    containsLower = False
    containsNum = False
    if len(password) <= 7:
        return False
    for char in px:
        if char.isupper():
            containsUpper = True 
    if containsUpper == False:
        return False
    for char in px:
        if char.islower():
            containsLower = True
    if containsLower == False:
        return False
    for char in px:
        if char.isdigit():
            containsNum = True
    if containsNum == False:
        return False
    return True

