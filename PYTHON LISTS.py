if __name__ == '__main__':
    N = int(input())   # Number of commands
    lst = []           # Initialize empty list
    
    for _ in range(N):
        command = input().split()
        operation = command[0]
        
        if operation == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif operation == "print":
            print(lst)
        elif operation == "remove":
            e = int(command[1])
            lst.remove(e)
        elif operation == "append":
            e = int(command[1])
            lst.append(e)
        elif operation == "sort":
            lst.sort()
        elif operation == "pop":
            lst.pop()
        elif operation == "reverse":
            lst.reverse()
