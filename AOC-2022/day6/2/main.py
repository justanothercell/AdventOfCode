with open('input.txt') as infile:
    buffer_bytes_samples = infile.readlines()

buffer_bytes_samples += [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',  # 19
    'bvwbjplbgvbhsrlpgdmjqwftvncz',  # 23
    'nppdvjthqldpwncqszvftbrmjlhg',  # 23
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',  # 29
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  # 26
]

for buffer_bytes in buffer_bytes_samples:
    for i in range(14, len(buffer_bytes)):
        if len(set(buffer_bytes[i-14:i])) == 14:
            print(f'packet start: {i}')
            break

# packet start: 3380
# packet start: 19
# packet start: 23
# packet start: 23
# packet start: 29
# packet start: 26
