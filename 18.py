answer = input("Please enter 'A', 'B' or 'C':- ")
if not answer == 'A' or answer == 'B' or answer == 'C':
    print("[!] Only A, B or C are allowed.")
    exit(1)
if answer != 'A':
    if answer != 'B':
        print("Coconut")
    else:
        print("Banana")
else:
    print("Apple")
