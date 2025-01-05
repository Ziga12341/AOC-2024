import unittest

s = "small_input.txt"
l = "input.txt"


def read_program(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Program: "):
                line = line.strip().split("Program: ")[1]
                # tuple first = opcode, second = operand
                program = [(int(opcode), int(operand)) for opcode, operand in
                           zip(line.split(","), line.split(",")[1:])][::2]
                return program


# register_a = 729
# register_b = 0
# register_c = 0

combo_operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    # 4: 51571418, # register_a large input,
    4: 729, # register_a small input,
    5: 0, # register_b,
    6: 0, # register_c,
    7: None  # do nothing
}

small_input: list[str] = read_program(s)
large_input: list[str] = read_program(l)
print(small_input)
print(large_input)

outputs = []
instruction_pointer = 0
max_iteration = 10
i = 0
program = read_program(s)
while instruction_pointer <= len(program) or i < max_iteration:
    i += 1

    opcode, operand = program[instruction_pointer]
    combo_operands_value = combo_operands[operand]
    if combo_operands_value is not None:

        # first operation
        if opcode == 0:
            # perform adv instruction use combo operand
            power = 2 ** combo_operands_value
            combo_operands[4] = int(combo_operands[4] // power)
        # The bxl instruction (opcode 1) - bitwise XOR of register B and the instruction's literal operand
        elif opcode == 1:
            combo_operands[5] = combo_operands[5] ^ operand
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        elif opcode == 2:
            # combo operand
            combo_operands[5] = combo_operands_value % 8
        elif opcode == 3:
            # if combo_operands[4] == 0 and instruction_pointer == len(program) - 1:
            #     print(instruction_pointer)
            #     print(len(program))
            #     break
            if combo_operands[4] == 0:
                instruction_pointer += 1
            else:
                # not zero, it jumps by setting the instruction pointer to the value of its literal operand
                # move to i - 1 because i will add instruction_pointer at the end of loop

                instruction_pointer = operand - 1
        elif opcode == 4:
            # itwise XOR of register B and register C, then stores the result in register B
            combo_operands[5] = combo_operands[5] ^ combo_operands[6]

        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        elif opcode == 5:
            outputs.append(int(combo_operands_value % 8))

        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        elif opcode == 6:
            power = combo_operands_value
            combo_operands[5] = int(combo_operands[4] // power)

        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
        elif opcode == 7:
            power = combo_operands_value
            combo_operands[6] = int(combo_operands[4] // power)
    instruction_pointer += 1



print(combo_operands[4])
print(outputs)
print(i)
# not right answer 7,3,3,5,5,1,6,5,7
## print bitwise XOR operation
# print("a ^ b =", a ^ b)

# combo operand modulo 8
# number % 8

# to get answer collect returns from out command

# i need to run program with 8 commands for the whole program and return everything what i collect from out command

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_program(s)