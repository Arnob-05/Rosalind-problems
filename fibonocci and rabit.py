def fib_bottom_up_algo(num):
    # if we type 1st or 2nd it will always give back 1 (fibonacci num = 1,1,2,3,5,8,----,n)
    if num == 1 or num == 2:
        return 1
    # creating an array which length is (n+1) and putting 2nd and 3rd value of this array , cause range(5) = 0 to 4)
    bottom_up = [None] * (num+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, num+1):
        bottom_up[i] = (bottom_up[i-1]) + (bottom_up[i - 2])
        # here [i-1] and [i-2] means [i - 1st previous value of array] and [i - 2nd previous value of array]
    return bottom_up[num]


print(fib_bottom_up_algo(25))


# another way

def fibonacci(num):
    new, old = 1, 1
    for i in range(num - 1):
        # print(i)
        new, old = old, old + new  # 1st month(beginning) = (1,1) and store it in 21th line
                                    # 2nd month(beginning) = (new, old = 1, 1) child rabit becomes mature
                                   #3rd month(beginning) = (new, old = 1, 2)
                                   # 4rth mpnth(beginning) = (new, old = 2, 3)
                                   #5th month(beginning) = (new, old = 3, 5)
                                    #6th month(beginning) or end of month 5 = (new,old = 5, 8)
        # here after for loop(22th line) this statement defines that until for range (n-1) exp:5 > (5-1)=4 or 4 times the
        # old value will add (old + new) and store it in 18th line
    return new
print(fibonacci(25))

# if the parents produce more than 1 offsprings

def fibonacci(month, offsprings):
    child, parent = 1, 1
    for i in range(month - 1):
        # print(i)
        child, parent = parent, parent + (child * offsprings)  # number of offspring produces = 2 in every month
        # 1st month beginning (child(previous total), parent(total)) = (1,1)
        # 2nd month  begi     (child(prev), parent(total) = 1, 1) child rabbit becomes mature
        # 3rd month  begi     (child(prev), parent(total) = 1, 3)
        # 4rth month begi     (child(prev), parent(total) = 3, 5)
        # 5th month  begi     (child(prev), parent(total) = 5, 11)                     #(new, old = 5, 8)
        # 6th month  begi     (child(prev), parent(total) = 11, 21) (end of month 5)
        # here after for loop(40th line) this statement defines that until for range (n-1) exp:5 > (5-1)=4 or 4 times the
        # old value will add (old + new) and store it in 37th line
    return child
print(fibonacci(5, 2))