def is_ssn(s):
    if (s[:3].isdigit() and s[3:4] == "-" and s[4:6].isdigit() and s[6:7] == "-" and s[7:].isdigit()):
        return True
    return False


print(is_ssn('832-bc-3847'))


x = "bc"
print(x.isdigit)
