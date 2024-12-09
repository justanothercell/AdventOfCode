with open('input.txt') as infile:
    diskmap = [int(x) for x in infile.read().strip()]

# h1, h2: the two "heads" performing operations
h1 = 0
h2 = len(diskmap)
if h2 % 2 == 1: # we are looking at space
    h2 -= 1 # move back to last file

# the block pointer/index, used to calculate the sum
ptr = 0

checksum = 0

while h1 <= h2:
    if h1 % 2 == 0: # we are looking at a file, trivial case, we are not moving it
        filesize = diskmap[h1]
        fileid = h1 // 2 # index of file
        h1 += 1 # going to next space
    else: # we are looking at empty space
        filesize = diskmap[h2] # fetching file from the back
        spacesize = diskmap[h1]
        fileid = h2 // 2 # index of file
        if spacesize < filesize: # not enough space to fit file
            h1 += 1 # going to next file, keeping h2
            filesize = spacesize
            diskmap[h2] -= spacesize # reducing remaining fileisze
        elif spacesize == filesize: # exactly enough space to fit file
            h1 += 1 # going to next file
            h2 -= 2 # going to previous file, skipping the empty space
        else: # too much space, need to look at a second file
            h2 -= 2 # going to previous file, skipping the empty space, keeping h1 on the empty space
            diskmap[h1] -= filesize # reducing remaining space
    # modified gauss summation of: sum from k=ptr to k=ptr+filesize-1 of fileid*k
    filesum = fileid * filesize * (2 * ptr + filesize - 1) // 2
    checksum += filesum
    print(f'{fileid} x{filesize} ptr={ptr} h1={h1}, h2={h2}, filesum={filesum}')
    ptr += filesize # advance n blocks

print(checksum)
