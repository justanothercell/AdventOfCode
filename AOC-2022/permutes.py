def permute(arr, consumer):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        consumer(arr)
        return
    for i in range(len(arr)):
        m = arr[i]
        rem_list = arr[:i] + arr[i+1:]
        permute(rem_list, lambda x: consumer([m] + x))

permute([1, 2, 3], print)
print()
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]


def permute_tls(arr, elem_index, consumer):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        consumer(arr)
        return
    def permute_tls_sub(arr, consumer):
        if len(arr) == 0:
            return
        if len(arr) == 1:
            consumer(arr)
            return
        for i in range(len(arr)):
            m = arr[i]
            rem_list = arr[:i] + arr[i + 1:]
            permute_tls_sub(rem_list, lambda x: consumer([m] + x))

    m = arr[elem_index]
    rem_list = arr[:elem_index] + arr[elem_index + 1:]
    permute_tls_sub(rem_list, lambda x: consumer([m] + x))


permute_tls([1, 2, 3], 0, print)
print()
permute_tls([1, 2, 3], 1, print)
print()
permute_tls([1, 2, 3], 2, print)
print()
