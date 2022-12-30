import re


def isValidIFSCode(str):

    # Regex to check valid IFSC Code.
    regex = "^[A-Z]{4}0[A-Z0-9]{6}$"

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

# Driver code


# Test Case 1:
# str1 = "SBIN0125620"
# print(isValidIFSCode(str1))

# # Test Case 2:
# str2 = "SBIN0125"
# print(isValidIFSCode(str2))

# # Test Case 3:
# str3 = "1234SBIN012"
# print(isValidIFSCode(str3))

# # Test Case 4:
# str4 = "ABHY0065002"
# print(isValidIFSCode(str4))
