def arithmetic_arranger(problems, showAnswers):
    numbers = list()
    operators = list()

    tempList = list()

    ## Checking for errors
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in problems:
        tempList.append(i.split())
        
    temp = 0
    for i in tempList:
        numbers.append(tempList[temp][0])
        numbers.append(tempList[temp][2])
        operators.append(tempList[temp][1])
        temp += 1

    for i in numbers:
        if len(str(i)) > 4:
            return "Error: Numbers cannot be more than four digits."
        if str(i).isdigit():
            continue
        else:
            return "Error: Numbers must only contain digits."

    for i in operators:
        if i != '+' and i != '-':
            return "Error: Operator must be '+' or '-'."

    ## Arranging problems
    for i in range(int(len(numbers)/2)):
        higherLen = len(numbers[i*2])
        if higherLen < len(numbers[i*2+1]):
            higherLen = len(numbers[i*2+1])
            for j in range(higherLen + 2 - len(numbers[i*2])):
                print(" ", end = '')
        else:
            for j in range(len(numbers[i*2]) + 2 - higherLen):
                print(" ", end = '')
        print (numbers[i*2], end = '')
        print ("    ", end = '')

    print ("\n", end = '')

    for i in range(1, len(numbers), 2):
        print (operators[int(i/2)], end = ' ')
        higherLen = len(numbers[i])
        if higherLen < len(numbers[i-1]):
            higherLen = len(numbers[i-1])
            for j in range(higherLen - len(numbers[i])):
                print (" ", end = '')
        else:
            for j in range(len(numbers[i]) - higherLen):
                print (" ", end = '')
        print (numbers[i], end = '')
        print ("    ", end = '')

    print ("\n", end = '')

    for i in range(int(len(numbers)/2)):
        higherLen = len(numbers[i*2])
        if higherLen < len(numbers[i*2+1]):
            higherLen = len(numbers[i*2+1])
        for j in range(higherLen + 2):
            print ("-", end = '')
        print ("    ", end = '')

    ## Showing results
    print ("\n", end = '')
    if showAnswers == True:
        for i in range(int(len(numbers)/2)):
            higherLen = len(numbers[i*2])
            if higherLen < len(numbers[i*2+1]):
                higherLen = len(numbers[i*2+1])
            if operators[i] == '+':
                answer = int(numbers[i*2]) + int(numbers[i*2+1]) 
            else:
                answer = int(numbers[i*2]) - int(numbers[i*2+1])
            for j in range(higherLen + 2 - len(str(answer))):
                print (" ", end = '')
            print (answer, end = '')
            print ("    ", end = '')
            
    ## End of the program        
    return "\nFinished."

print(arithmetic_arranger(["32 + 8", "1 - 3801", "114 - 132"], True))