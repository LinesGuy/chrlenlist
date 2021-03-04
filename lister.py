word = "list()"

def num_to_lenlist(i: float) -> str:
    numlist = list(str(i))
    if "." in numlist:
        decimal = numlist.index(".")
    else:
        decimal = len(numlist)
    out = []
    for index, num in enumerate(numlist):
        if num == ".":
            continue
        tout = "len([" + ",".join([word]*int(num)) + "])*len([" + (word + ",") * 9 + word + "])**"
        if index < decimal:
            tout += "len(["
        else:
            tout += "-len([" + word + ","
        tout += ",".join([word] * (abs(decimal - index)-1)) + "])"
        out.append(tout)

    return "+".join(out)

def str_to_chrlenlist(string: str) -> str:
    out = []
    for c in string:
        out.append("chr("+num_to_lenlist(ord(c))+")")
    return "+".join(out)

##with open("beemovie.txt") as file:
##    content = "".join(file.readlines())
##
##with open("output.txt", "w+") as file:
##    file.write(str_to_chrlenlist(content))
print(str_to_chrlenlist("chris rocks!"))
