from collections import defaultdict

def non_repeat_substring(str):
    """Longest Substring with Distinct Characters
    
    Args:
        str (str): word

    Returns:
        longest (int): integer size of longest substring found in str
    """

    n = len(str)
    i = window_start = 0
    longest = 1
    found = {} 
    
    while i < n:
        current = str[i]

        if current in found:
            if found[current] >= window_start:
                window_start = found[current] + 1
                found[current] = i

        longest = max(longest, i - window_start + 1)

        if current not in found:
            found[current] = i
        i+= 1

    return longest

def longest_substring_with_k_distinct(str, k):
    """Longest Substring with maximum K Distinct Characters

    Parameters
    ----------
    str : str
        string
    k : int
        maximun int characters in str    

    Returns
    -------
    max_len : int
        integer size of longest substring
    """

    n = len(str) 
    start, max_len, freq = 0, 0, {}

    for end in range(n):
        char = str[end]
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

        while len(freq) > k:
            left_char = str[start]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len

def length_of_longest_substring(str, k):
    # TODO: Write your code here
    n = len(str)
    freq = defaultdict(int)
    max_len = float('-inf')
    window_start = 0

    for i in range(n):
        char = str[i]
        freq[char] += 1

        if i - window_start + 1 > freq[str[window_start]] + k:
            freq[str[window_start]] -= 1
            if freq[str[window_start]] == 0:
                del freq[str[window_start]]
            window_start += 1

        max_len = max(max_len, i - window_start + 1)
  
def length_of_longest_substring(arr, k):
    """Longest Subarray with Ones after Replacement (hard)

    Parameters
    ----------
    arr : array of 0's and 1's
        array ints
    k : int
        maximun int chars 0's to replace in array   

    Returns
    -------
    max_len : int
        longest contiguous subarray having all 1s.
    """
    start = ones = zeros = 0
    max_len = float('-inf')

    for end in range(len(arr)):
        current = arr[end]
        if current == 0: 
            zeros += 1
        else:
            ones += 1

        while zeros > k:
            if arr[start] == 0:
                zeros -= 1
            else:
                ones -= 1
            start += 1
            
        max_len = max(max_len, ones + zeros)

    
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length

    



