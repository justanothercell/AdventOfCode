class Segment:
    def __init__(self, prev, filesize, fileid, spacesize):
        self.prev = prev
        if self.prev is not None:
            self.prev.next = self
        self.next = None
        self.filesize = filesize
        self.spacesize = spacesize
        self.id = fileid

    def extract_self(self):
        assert self.prev is not None, 'Cannot extract first file, just manually move somethign else there'
        self.prev.next = self.next
        self.prev.spacesize += self.spacesize + self.filesize
        if self.next is not None:
            self.next.prev = self.prev
        self.spacesize = 0
        self.prev = None
        self.next = None

    def insert_after(self, node):
        assert self.prev is None, f'{self} should have no backlink {self.prev} as it is not in the file system'
        assert self.next is None, f'{self} should have no forward link {self.next} as it is not in the file system'
        assert self.spacesize == 0, f'{self} should have no space allocated as it is not in the file system'
        # node.prev = A, node.next = B, self.prev = None, self.next = None
        self.prev = node
        # node.prev = A, node.next = B, self.prev = node, self.next = B
        self.next = node.next
        # node.prev = A, node.next = self, self.prev = node, self.next = B
        node.next = self
        # b.prev = self
        self.next.prev = self

        assert self.prev.spacesize >= self.filesize, f'Cannot insert file, not enough space: {self.prev} too small for {self} '
        self.prev.spacesize -= self.filesize
        self.spacesize = self.prev.spacesize
        self.prev.spacesize = 0

    def __repr__(self):
        return f'[{self.id} x{self.filesize}][x{self.spacesize}]'

def print_disk(head):
    s = head
    p = head.prev
    while s is not None:
        print(s, end=' ')
        p = s
        s = s.next
    print()

with open('input.txt') as infile:
    diskmap = [int(x) for x in infile.read().strip()]

if len(diskmap) % 2 == 1:
    diskmap.append(0) # add zero sized space

head = None
tail= None

for i in range(0, len(diskmap), 2):
    tail = Segment(tail, diskmap[i], i // 2, diskmap[i+1])
    if head is None:
        head = tail

s = tail
id = s.id
while s is not None:
    # we should check each file only once and in reverse order, 
    # so if current id > last id we already checked current i
    if s.id > id:
        s = s.prev
        continue
    id = s.id
    # print(f'checking {s.id}')
    k = head
    while k.id != s.id: # shoudl only replace forward
        if k.spacesize >= s.filesize:
            print(f'> putting {s.id} after {k.id}')
            m = s.prev
            s.extract_self()
            s.insert_after(k)
            s = m
            break
        k = k.next
    else:
        s = s.prev

print()

print_disk(head)

print()

# the block pointer/index, used to calculate the sum
ptr = 0

checksum = 0

s = head
while s is not None:
    # modified gauss summation of: sum from k=ptr to k=ptr+filesize-1 of fileid*k
    filesum = s.id * s.filesize * (2 * ptr + s.filesize - 1) // 2
    checksum += filesum
    # print(f'{s.id} x{s.filesize} ptr={ptr}, filesum={filesum}')
    ptr += s.filesize + s.spacesize # advance n blocks
    s = s.next

# enable mroe printss for the small one, the bug one just has too many elements
print(checksum)
