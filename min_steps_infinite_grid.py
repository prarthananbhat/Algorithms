# Min Steps in Infinite Grid
def coverPoints(A, B):
    dis = 0
    if len(A) > 1 and len(A) == len(B):
        for i in range(1, len(A)):
            x0 = A[i - 1]
            y0 = B[i - 1]
            x1 = A[i]
            y1 = B[i]
            dis = dis + max(abs(x1 - x0), abs(y1 - y0))
    return dis

if __name__ == "__main__":
    print("Min Steps in Infinite Grid")
    A = [0, 1, 1]
    B = [0, 1, 2]
    result = coverPoints(A,B)
    print(result)


