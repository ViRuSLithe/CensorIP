from msvcrt import putwch as TYPE_KEY, getwch as GET_KEY

def censor_ip(PROMPT = "IP Address: ", CENSOR_WITH = "*"):
    for CHARACTER in PROMPT:
        TYPE_KEY(CHARACTER)

    IP_ADDRESS = ""

    while 1:
        CHARACTER = GET_KEY()

        if CHARACTER == "\r" or CHARACTER == "\n":
            break
        if CHARACTER == "\003":
            raise KeyboardInterrupt
        if CHARACTER == "\b":
            IP_ADDRESS = IP_ADDRESS[:-1]

            TYPE_KEY("\b"), TYPE_KEY(" "), TYPE_KEY("\b")
        else:
            IP_ADDRESS += CHARACTER
            
            if IP_ADDRESS.count(".") >= 2:
                if CHARACTER == ".":
                    TYPE_KEY(".")
                else:
                    TYPE_KEY(CENSOR_WITH)
            else:
                TYPE_KEY(CHARACTER)

    TYPE_KEY("\r")
    TYPE_KEY("\n")

    return IP_ADDRESS