raw_disk = []

with open('inputs/day9') as fp:
    raw_disk.extend(list(fp.read()))

disk, file_id = [], 0

for i in range(0, len(raw_disk)):
    if i & 1:
        disk.extend(['.']*int(raw_disk[i]))
    else:
        disk.extend([str(file_id)]*int(raw_disk[i]))
        file_id += 1


def calculate_checksum(disk):
    checksum = 0
    for i, val in enumerate(disk):
        if val == '.': continue
        checksum += (i * int(val))
    return checksum


# part 1
i, j = 0, len(disk) - 1
disk_p1 = disk.copy()

while i < j:
    while disk_p1[i] != '.':
        i += 1
    while disk_p1[j] == '.':
        j -= 1

    if i < j:
        temp = disk_p1[j]
        disk_p1[j] = disk_p1[i]
        disk_p1[i] = temp


print(f'part 1: {str(calculate_checksum(disk_p1))}')

# part 2
i, j = 0, len(disk) - 1
disk_p2 = disk.copy()

while i < j:
    # slide until we maybe find a file
    while disk_p2[j] == '.':
        j -= 1

    if disk_p2[j] != '.':
        # slide again to capture the entire file
        end_of_file_index = j
        while disk_p2[end_of_file_index - 1] == disk_p2[j]:
            end_of_file_index -= 1

        # now slide i to try to find gaps for the files to fit into
        while disk_p2[i] != '.':
            i += 1

        beginning_of_gap_index = i

        while beginning_of_gap_index < end_of_file_index:
            if disk_p2[beginning_of_gap_index] == '.':
                end_of_gap_index = beginning_of_gap_index
                while disk_p2[end_of_gap_index + 1] == disk_p2[beginning_of_gap_index]:
                    end_of_gap_index += 1
            
            if j - end_of_file_index <= end_of_gap_index - beginning_of_gap_index:
                l = j - end_of_file_index + 1

                disk_p2[beginning_of_gap_index:beginning_of_gap_index+l], disk_p2[end_of_file_index:end_of_file_index+l] = \
                    disk_p2[end_of_file_index:end_of_file_index+l], disk_p2[beginning_of_gap_index:beginning_of_gap_index+l]

                beginning_of_gap_index += l
                break
            else:
                beginning_of_gap_index = end_of_gap_index + 1
                while disk_p2[beginning_of_gap_index] != '.':
                    beginning_of_gap_index += 1

    j = end_of_file_index - 1

print(f'part 2: {str(calculate_checksum(disk_p2))}')