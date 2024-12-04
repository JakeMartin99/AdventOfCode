import json
def check(val, field) -> bool:
    if field == "byr":
        try:
            val = int(val)
            return 1920 <= val <= 2002
        except:
            return False
    elif field == "iyr":
        try:
            val = int(val)
            return 2010 <= val <= 2020
        except:
            return False
    elif field == "eyr":
        try:
            val = int(val)
            return 2020 <= val <= 2030
        except:
            return False
    elif field == "hgt":
        t = val[-2:-1] + val[-1]
        try:
            val = int(val[:-2])
            return (t == "cm" and 150 <= val <= 193) or (t == "in" and 59 <= val <= 76)
        except:
            return False
    elif field == "hcl":
        b = (val[0] == '#')
        val = val[1:]
        try:
            val2 = int(val, 16)
            return len(val) == 6
        except:
            return False
    elif field == "ecl":
        return (val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    elif field == "pid":
        try:
            val2 = int(val)
            return len(val) == 9
        except:
            return False
    else:
        return True

file = open("day4.txt")
passports = file.read().split("\n\n")
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
count1 = 0
count2 = 0
for ps in passports:
    if all(f in ps for f in fields):
        count1 += 1
        ps2 = json.loads("{\"" + ps.replace('\n', " ").replace(" ", "\", \"").replace(":", "\":\"") + "\"}")
        if all(check(ps2[f], f) for f in fields):
            count2 += 1
print("Part 1: " + str(count1))
print("Part 2: " + str(count2))
file.close()
