def sliding_window_max_sum(arr, window_size):
    if len(arr) < window_size:
        return sum(arr)
    window_sum = sum(arr[:window_size])
    max_sum = window_sum
    for i in range(len(arr) - window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(max_sum, window_sum)
    return max_sum

def test_sliding_window_max_sum():
    arr = [2, 1, 5, 1, 3, 2, 8, 4, 1, 9]
    window_size = 3
    max_sum = sliding_window_max_sum(arr, window_size)
    print(f"Maximum sum of a sliding window of size {window_size} is: {max_sum}")
