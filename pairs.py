import sys

def find_pairs(numbers):
    pairs = []     
    seen = set()   

    for num in numbers:   
        complement = 10 - num   

        if complement in seen:  
            pairs.append((complement, num))   
        seen.add(num)  

    return pairs


if __name__ == "__main__":
    args = sys.argv[1:]  
    numbers = [int(num) for num in args]  
    pairs = find_pairs(numbers)  
    for pair in pairs:   
        print(f"{pair[0]} + {pair[1]}")
