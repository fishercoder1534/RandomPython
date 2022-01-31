import re


def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern: {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")


test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*']  # this means zero or more ds
multi_re_find(test_patterns, test_phrase)
test_patterns = ['sd?']  # this means zero or one ds
multi_re_find(test_patterns, test_phrase)
test_patterns = ['sd+']  # this means one or more ds
multi_re_find(test_patterns, test_phrase)
test_patterns = ['sd{1,3}']  # this means one to three ds
multi_re_find(test_patterns, test_phrase)

test_patterns = ['s[sd]+']  # this means one or more either s or d
multi_re_find(test_patterns, test_phrase)


