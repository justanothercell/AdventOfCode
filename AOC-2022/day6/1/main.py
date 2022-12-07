with open('input.txt') as infile:
    buffer_bytes_samples = infile.readlines()

buffer_bytes_samples += [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',  # 7
    'bvwbjplbgvbhsrlpgdmjqwftvncz',  # 5
    'nppdvjthqldpwncqszvftbrmjlhg',  # 6
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',  # 10
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  # 11
]

for buffer_bytes in buffer_bytes_samples:
    for i in range(4, len(buffer_bytes)):
        if len(set(buffer_bytes[i-4:i])) == 4:
            print(f'packet start: {i}')  # packet start:
            break

