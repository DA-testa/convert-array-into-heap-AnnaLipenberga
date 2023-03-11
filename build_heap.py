# python3

def heapify(data, n, i, swaps):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and data[left] < data[smallest]:
        smallest = left
    if right < n and data[right] < data[smallest]:
        smallest = right
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, n, smallest, swaps)
        

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
 


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    assert 1 <= n <= 10**5
    assert all(0 <= a <= 10**9 for a in data)

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert 0 <= len(swaps) <= 4*n


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
