input_path = 'input1.txt'

elf_cals = 0
elf_list = []

with open(input_path) as input_file:
    for line in input_file:

        if line != '\n':
            elf_cals += int(line.strip('\n'))
        else:
            elf_list.append(elf_cals)
            elf_cals = 0

    #Catches eof line:
    elf_list.append(elf_cals)
            
elf_list.sort()
print('Max:', elf_list[-1])

print('Sum:', sum(elf_list[-3:]))