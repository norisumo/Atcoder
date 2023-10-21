A,B,C = map(int, input().split())

if 0 <= A and 0 <= B:
    if A > B:
        exit(print(">")) 
    elif B > A:
        exit(print("<"))
    else:
        exit(print("="))
elif A < 0 and B < 0:
    if C % 2 == 0:
        if abs(A) > abs(B):
            exit(print(">")) 
        elif abs(A) < abs(B):
            exit(print("<")) 
        else:
            exit(print("=")) 
    else:
        if abs(A) > abs(B):
            exit(print("<")) 
        elif abs(A) < abs(B):
            exit(print(">")) 
        else:
            exit(print("=")) 

else:
    if C % 2 == 0:
        if abs(A) > abs(B):
            exit(print(">")) 
        elif abs(A) < abs(B):
            exit(print("<")) 
        else:
            exit(print("=")) 
    else:
        if A > B:
            exit(print(">")) 
        elif A < B:
            exit(print("<")) 
        else:
            exit(print("=")) 
