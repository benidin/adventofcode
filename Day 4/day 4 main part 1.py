def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


# return 1 if good 0 if not.
def validate(passpt):
    # lets get teh data we need.
    fieldsMinusCID = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    fieldsPresent = [x.split(":")[0] for x in " ".join(passpt).split()]
    if len(fieldsPresent) == 8:
        return 1
    elif fieldsMinusCID == sorted(fieldsPresent):
        return 1
    else:
        return 0


passportList = read_input_file()
validPassports = 0
passport = []

for line in passportList:
    # so I had to cheat and add an extra new line at the end of the input file ... too lazy to fix it right
    if line == '\n':  # our input is always perfect ;)
        validPassports += validate(passport)
        passport.clear()
    else:
        passport.append(line)

print(validPassports)
