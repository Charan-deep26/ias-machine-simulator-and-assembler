opcode = {
    "NOP":   "00000000",
    "LOAD":  "00000001",
    "ADD":   "00000101",
    "STOR":  "00100001",
    "JUMP":  "00001101",     # unconditional jump
    "JUMP+": "00001111",     # jump if AC >= 0
    "HALT":  "11111111"
}

def to_bin(n, bits):
    # The & mask handles Two's Complement for negative numbers
    mask = (1 << bits) - 1
    return format(int(n) & mask, f"0{bits}b")

def mem(x):
    return x.replace("M(", "").replace(")", "")

memory = {}

with open("assembly.txt") as f:
    for line in f:
        # --- THE FIX IS HERE ---
        # 1. Remove comments by splitting at '//' and taking the first part
        # 2. Strip whitespace from both ends
        line = line.split("//")[0].strip()
        
        # If the line is empty (was just a comment or blank), skip it
        if not line:
            continue
        # -----------------------

        # DATA
        if ":" in line and "|" not in line:
            a, v = line.split(":")
            memory[int(a)] = to_bin(v.strip(), 40)
            continue

        # INSTRUCTION
        addr_part, inst_part = line.split(":")
        addr = int(addr_part)

        left, right = inst_part.split("|")
        left = left.strip().split()
        right = right.strip().split()

        def encode(inst):
            if inst[0] in ("HALT", "NOP"):
                return opcode[inst[0]] + "0"*12
            return opcode[inst[0]] + to_bin(mem(inst[1]), 12)

        memory[addr] = encode(left) + encode(right)

# write machine code
if memory:
    max_addr = max(memory)
    with open("binary.txt", "w") as f:
        for i in range(max_addr + 1):
            f.write(memory.get(i, "0"*40) + "\n")

    print("Assembler done → binary.txt generated")
else:
    print("Error: No valid lines found in assembly.txt")