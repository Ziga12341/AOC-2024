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


register_a = 729
register_b = 0
register_c = 0

combo_operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: register_a,
    5: register_b,
    6: register_c,
    7: None  # do nothing
}

small_input: list[str] = read_program(s)
large_input: list[str] = read_program(l)
print(small_input)
print(large_input)

outputs = []
instruction_pointer = 0
program = read_program(s)
while instruction_pointer != len(program):
    opcode, operand = program[instruction_pointer]
    if combo_operands[operand] is not None:
        combo_operands_value = combo_operands[operand]

        # first operation
        if opcode == 0:
            # perform adv instruction use combo operand
            power = combo_operands_value
            register_a = int(register_a // power)
        # The bxl instruction (opcode 1) - bitwise XOR of register B and the instruction's literal operand
        elif opcode == 1:
            register_b = register_b ^ operand
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        elif opcode == 2:
            # combo operand
            register_b = combo_operands_value % 8
        elif opcode == 3:
            if register_a == 0:
                continue
            else:
                # not zero, it jumps by setting the instruction pointer to the value of its literal operand
                # do not know how to implement this
                # move to i - 1 because i will add instruction_pointer at the end of loop
                for i, tuple_instruction in enumerate(program):
                    opcode_0, operand_0 = tuple_instruction
                    if operand_0 == operand:
                        instruction_pointer = i - 1
        elif opcode == 4:
            # itwise XOR of register B and register C, then stores the result in register B
            register_b = register_b ^ register_c

        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        elif opcode == 5:
            outputs.append(int(combo_operands_value % 8))

        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        elif opcode == 6:
            power = combo_operands_value
            register_b = int(register_a // power)
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
        elif opcode == 7:
            power = combo_operands_value
            register_c = int(register_a // power)
    instruction_pointer += 1



print(register_a)
print(outputs)
## print bitwise XOR operation
# print("a ^ b =", a ^ b)

# combo operand modulo 8
# number % 8

# to get answer collect returns from out command

# i need to run program with 8 commands for the whole program and return everything what i collect from out command

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_program(s)