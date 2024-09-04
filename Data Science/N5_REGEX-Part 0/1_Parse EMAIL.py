import re


def parse_email(s):
    """Parses a string as an email address, returning an (id, domain) pair."""
    re_email = re.compile(r'''
                          ^(?P<userid>[a-zA-Z0-9_\.+-]+)
                          @
                          (?P<domain>[a-zA-Z0-9_\.+-]+[a-zA-Z0-9_\.-]+[a-zA-Z]+)$
                          ''', re.VERBOSE)
    res = re_email.fullmatch(s)
    print(res)

    if res:
        u = res.group('userid')
        d = res.group('domain')
        return (u, d)
    else:
        raise ValueError


print(parse_email('ritchie@cc.gatech.edu'))
print(parse_email('what-do-you-know+not-much@gmail'))
print(parse_email('ritchie@cc.gatech.edu7'))
print(parse_email('x @hpcgarage.org'))


def validate_email(email):

    # RegexObject = re.compile( Regular expression, flag )
    # Compiles a regular expression pattern into
    # a regular expression object
    regex_email = re.compile(r""" 
                           ^([\w]+)                 # local Part 
                           @                             # single @ sign 
                            ([\w]+\.[\w]+)$                 # Top level Domain      
                           """, re.VERBOSE | re.IGNORECASE)

    # RegexObject is matched with the desired
    # string using fullmatch function
    # In case a match is found, search()
    # returns a MatchObject Instance
    res = regex_email.fullmatch(email)

    # If match is found, the string is valid
    if res:
        print("{} is Valid. Details are as follow:".format(email))

        # prints first part/personal detail of Email Id
        print("Local:{}".format(res.group(1)))

        # prints Domain Name of Email Id
        print("Domain:{}".format(res.group(2)))

    else:
        # If match is not found,string is invalid
        print("{} is Invalid".format(email))


# Driver Code
validate_email("expectopatronum@gmail.com")
validate_email("avadakedavra@yahoo.com@")
validate_email("Crucio@.com")
