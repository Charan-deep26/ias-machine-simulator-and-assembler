# IAS Architecture Simulator

## Overview
This project is a functional implementation of the **IAS (Institute for Advanced Study)** computer architecture. It demonstrates the Von Neumann stored-program concept by simulating a processor that can modify its own instructions in real-time to iterate through arrays.

## Components
* **`ias.py`**: The processor simulator. It features a **disk-based memory system**, reading and writing directly to `binary.txt` to simulate persistent storage.
* **`assembler.py`**: Converts the assembly language (`assembly.txt`) into 40-bit machine code (`binary.txt`).
* **`assembly.txt`**: Contains the source code, specifically an **Array Iterator** algorithm that sums a list of numbers.

## How It Works (The Array Iterator)
The assembly program calculates the sum of an array `[10, 20, 30, 40, 50]` by utilizing **Address Modification**.
1.  **Dynamic Instruction:** The instruction `ADD M(30)` is loaded into the processor.
2.  **Self-Modification:** Inside the loop, the program adds `1` to the instruction itself, changing `M(30)` to `M(31)`, then `M(32)`, and so on.
3.  **Execution:** The processor stores this modified instruction back into memory and executes it in the next cycle.

## Usage

### 1. Assemble
Convert the assembly code into machine code:
```bash
python assembler.py
python ias.py
