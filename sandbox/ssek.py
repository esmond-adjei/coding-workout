def sum_of_pairs(arr, k):
    pv = arr[0]
    nx = arr[1]
    sum_k = pv + nx

    for i in range(2, len(arr)):
        if sum_k == k:
            print("=> ", pv, nx)
        
        curr = arr[i - 1]
        nx = arr[i]
        print(pv, curr, nx, sum_k)
        sum_k = curr + nx
        pv = curr


if __name__ == "__main__":
    # arr = [1,2,3,4,5]
    arr = [1,9,8,2,7,3,4,6,5,5]
    k = 10
    sum_of_pairs(arr, k)
