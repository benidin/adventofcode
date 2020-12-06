def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def validate_fields(passport):
    pp = [x.rstrip("\n") for x in passport]
    pp = " ".join(pp).split()
    for field in pp:
        key, value = field.split(':')
        if key == 'byr':
            if len(value) == 4 and (1920 <= int(value) <= 2003):
                continue
            else:
                return False
        elif key == 'iyr':
            if len(value) == 4 and (2010 <= int(value) <= 2020):
                continue
            else:
                return False
        elif key == 'eyr':
            if len(value) == 4 and (2020 <= int(value) <= 2030):
                continue
            else:
                return False
        elif key == 'hgt':
            if not value.isdigit():
                if value[-2:] == "in" and (59 <= int(value[:-2]) <= 76):
                    continue
                elif value[-2:] == "cm" and (150 <= int(value[:-2]) <= 193):
                    continue
            return False
        elif key == 'hcl':
            if value[0] == '#' and len(value[1:]) == 6 and all(c in '0123456789abcdef' for c in value[1:]):
                continue
            return False
        elif key == 'ecl':
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue
            return False
        elif key == 'pid':
            if value.isdigit() and len(value) == 9:
                continue
            return False
    return True


# return 1 if good 0 if not.
def validate(passpt):
    # lets get teh data we need.
    fieldsMinusCID = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    fieldsPresent = [x.split(":")[0] for x in " ".join(passpt).split()]
    if len(fieldsPresent) == 8 or fieldsMinusCID == sorted(fieldsPresent):
        return 1 if validate_fields(passpt) else 0
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
