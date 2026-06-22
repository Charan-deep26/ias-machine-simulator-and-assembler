PC = 0
AC = 0
MAR = 0
MBR = "0" * 40
IR  = "0" * 8
IBR = "0" * 20

def b2i(b): 
    val = int(b, 2)
    # If it is a 40-bit string and starts with '1', it is negative
    if len(b) == 40 and b[0] == '1':
        val -= (1 << 40)
    return val
def i2b(i): 
    return format(i & ((1<<40)-1), "040b")

OP = {
    "LOAD":  "00000001",
    "ADD":   "00000101",
    "STOR":  "00100001",
    "JUMP":  "00001101",
    "JUMP+": "00001111",
    "HALT":  "11111111"
}

# --- DISK OPERATIONS ---
def disk_read(addr):
    try:
        with open("binary.txt", "r") as f:
            lines = f.readlines()
        if addr < len(lines):
            return lines[addr].strip()
        else:
            return "0" * 40
    except FileNotFoundError:
        return "0" * 40

def disk_write(addr, val):
    lines = []
    try:
        with open("binary.txt", "r") as f:
            lines = [line.strip() for line in f]
    except FileNotFoundError:
        lines = []

    while len(lines) <= addr:
        lines.append("0" * 40)
    lines[addr] = val
    with open("binary.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")

def get_file_len():
    try:
        with open("binary.txt", "r") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
# -----------------------

def show():
    print("-" * 50)
    print(f"IR  -> {IR}")
    print(f"MAR -> {MAR}")
    print(f"MBR -> {MBR}")
    print(f"IBR -> {IBR}")
    print(f"AC  -> {AC}")
    print(f"PC  -> {PC}")
    print("-" * 50)

print("\nIAS Processor started (Disk Mode)")

while True:
    if PC >= get_file_len(): break

    # Fetch Cycle
    MAR = PC
    MBR = disk_read(MAR)

    LEFT  = MBR[:20]
    RIGHT = MBR[20:]

    # ===== LEFT INSTRUCTION CYCLE =====
    IR = LEFT[:8]
    MAR = b2i(LEFT[8:])
    IBR = RIGHT  # IBR holds the right instruction
    
    show() # Print state before Left execution

    if IR == OP["LOAD"]:   AC = b2i(disk_read(MAR))
    elif IR == OP["ADD"]:  AC += b2i(disk_read(MAR))
    elif IR == OP["STOR"]: disk_write(MAR, i2b(AC))
    elif IR == OP["JUMP"]: 
        PC = MAR
        continue
    elif IR == OP["JUMP+"]:
        if AC > 0:
            PC = MAR
            continue
    elif IR == OP["HALT"]:
        print("HALT encountered")
        break

    # ===== RIGHT INSTRUCTION CYCLE =====
    IR = IBR[:8]
    MAR = b2i(IBR[8:])
    IBR = "0" * 20 # Clear IBR as it is now being executed
    
    show() # Print state before Right execution

    if IR == OP["LOAD"]:   AC = b2i(disk_read(MAR))
    elif IR == OP["ADD"]:  AC += b2i(disk_read(MAR))
    elif IR == OP["STOR"]: disk_write(MAR, i2b(AC))
    elif IR == OP["JUMP"]: 
        PC = MAR
        continue
    elif IR == OP["JUMP+"]:
        if AC >= 0:
            PC = MAR
            continue
    elif IR == OP["HALT"]:
        print("HALT encountered")
        break

    PC += 1

print("\nFINAL RESULT:")
print("Sum stored at M(25) =", b2i(disk_read(25)))
