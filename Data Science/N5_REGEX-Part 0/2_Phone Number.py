import re


def parse_phone1(s):
    re_phone1 = re.compile(
        r"""
                          ^\s*
                          \((?P<areacode>[0-9]{3})\)
                          \s*
                          (?P<firstThree>[0-9]{3})
                          -
                          (?P<lastThree>[0-9]{4})
                          \s*$
                          """,
        re.VERBOSE,
    )
    res = re_phone1.fullmatch(s)

    if res:
        u = res.group("areacode")
        d = res.group("firstThree")
        e = res.group("lastThree")
        return (u, d, e)
    else:
        raise ValueError


# print(parse_phone1('(404) 121-2121    '))


def parse_phone2(s):
    re_phone2 = re.compile(
        r"""
                          ^\s*
                          \((?P<areacode>[0-9]{3})\)
                          -*\s*
                          (?P<firstThree>[0-9]{3})
                          -*
                          (?P<lastFour>[0-9]{4})
                          \s*$
                          """,
        re.VERBOSE,
    )

    re_phone3 = re.compile(
        r"""
                          ^\s*
                          (?P<areacode>[0-9]{3})
                          -*
                          (?P<firstThree>[0-9]{3})
                          -*
                          (?P<lastFour>[0-9]{4})
                          \s*$
                          """,
        re.VERBOSE,
    )

    res2 = re_phone2.fullmatch(s)
    res3 = re_phone3.fullmatch(s)

    if res2:
        u = res2.group("areacode")
        d = res2.group("firstThree")
        e = res2.group("lastFour")
        return (u, d, e)
    elif res3:
        u = res3.group("areacode")
        d = res3.group("firstThree")
        e = res3.group("lastFour")
        return (u, d, e)
    else:
        raise ValueError


# pass
print(parse_phone2("(404)555-0012"))
print(parse_phone2("(404)   555-0013   "))
print(parse_phone2("(404)5550015"))
print(parse_phone2("404-555-0016"))
print(parse_phone2("404-5550017"))
print(parse_phone2("404555-0018"))
print(parse_phone2("4045550019"))
# fail
print(parse_phone2("(404 121 0022"))
print(parse_phone2("404 121 0021"))
print(parse_phone2("404 121-0020"))
