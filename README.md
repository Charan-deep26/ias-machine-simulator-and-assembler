# IAS Machine Simulator and Assembler

A Python-based implementation of the IAS (Institute for Advanced Study) computer architecture featuring a custom assembler and processor simulator capable of executing 40-bit machine instructions.

## Overview

This project simulates the IAS computer architecture, one of the earliest stored-program computers and the foundation of the modern Von Neumann architecture.

The system consists of:

- A custom assembler that converts IAS assembly programs into 40-bit machine code.
- An IAS processor simulator implementing the complete fetch-decode-execute cycle.
- A disk-based memory model for storing instructions and data.
- Support for self-modifying code and dynamic address modification.

## Features

- IAS architecture simulation
- Custom assembler for IAS assembly language
- 40-bit instruction execution
- Fetch-Decode-Execute cycle simulation
- Instruction Register (IR)
- Instruction Buffer Register (IBR)
- Memory Buffer Register (MBR)
- Memory Address Register (MAR)
- Program Counter (PC)
- Accumulator (AC)
- Disk-based memory system
- Self-modifying code support
- Conditional and unconditional jumps

## Supported Instructions

| Instruction | Description |
|------------|-------------|
| LOAD | Load memory value into AC |
| ADD | Add memory value to AC |
| STOR | Store AC into memory |
| JUMP | Unconditional jump |
| JUMP+ | Jump if AC is positive |
| HALT | Stop execution |
| NOP | No operation |

## Project Structure

```text
.
├── assembler.py
├── Ias_processor.py
├── assembly.txt
├── binary.txt
├── Report.pdf
└── README.md
```

## Example Program

The included program computes the sum of an array:

```text
[10, 20, 30, 40, 50]
```

using dynamic address modification.

Instead of hardcoding multiple LOAD instructions, the program modifies instruction addresses during execution, allowing it to iterate through array elements using self-modifying code.

## How It Works

1. The assembler converts IAS assembly code into 40-bit machine instructions.
2. The simulator loads instructions from memory.
3. Instructions pass through the fetch and execute cycles.
4. Registers such as PC, AC, MAR, MBR, IR, and IBR are updated during execution.
5. The program dynamically modifies instruction operands to traverse the array.
6. The final sum is stored in memory location M(25).

For the provided input array:

```text
10 + 20 + 30 + 40 + 50 = 150
```

## How to Run

### Assemble the Program

```bash
python assembler.py
```

This generates:

```text
binary.txt
```

### Run the Simulator

```bash
python Ias_processor.py
```

The simulator displays:

- Current register contents
- Memory accesses
- Fetch cycle activity
- Execute cycle activity
- Program execution progress

## Concepts Demonstrated

- Computer Architecture
- IAS Architecture
- Von Neumann Architecture
- Stored Program Concept
- Assembly Language Programming
- Processor Design
- Memory Organization
- Fetch-Decode-Execute Cycle
- Self-Modifying Code
- Dynamic Address Modification

## Technologies Used

- Python
- Computer Architecture
- Assembly Language
- Processor Simulation

## Author

Charan Deep
