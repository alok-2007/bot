arr = []

while len(arr) < 60:
    round = input("Enter The Previous Round:\n")
    arr.insert(0, round)

def make_pre(lis):
    num = 0
    consec = 0
    total_consec = 0
    prev = False
    for i in lis:
        if i == "0":
            num += 1
            if prev:
                consec += 1
            else:
                consec = 0
            if consec > total_consec:
                total_consec = consec
            prev = True
        else:
            prev = False

    print(f"Total num: {str(num)}\n")
    print(f"last three: {arr[-3]}, {arr[-2]}, {arr[-1]}\n")
    print(f"consecutive 0's: {total_consec}")
    return "yes" if num >= 37 else "no"
    
while True:
    result = make_pre(arr)
    print(result)

    arr.pop(-1)
    round = input("Enter the Previous Round (e.g., '0' for crash below 2.0x, or 'quit' to stop):\n")

    if round.lower() == "quit":
        break

    arr.insert(0, round)