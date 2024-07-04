def solution(N):
    # Calculate the number of different letters
    num_letters = N // 26 if N % 26 == 0 else N // 26 + 1
    
    # Calculate the number of occurrences of each letter
    occurrences = N // num_letters
    
    # Calculate the remaining letters
    remaining = N % num_letters
    
    # Initialize the result string
    result = ''
    
    # Add the letters with the maximum occurrences
    for i in range(26):
        if i < num_letters:
            result += chr(ord('a') + i) * occurrences
        else:
            break
    
    # Add the remaining letters
    for i in range(remaining):
        result += chr(ord('a') + i)
    
    return result