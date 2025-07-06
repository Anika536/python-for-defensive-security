#1.2.10 Exercises
#Safe Float Comparison
#Implement def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0) reproducing math.isclose without using the module.
def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    diff = abs(a-b)
    max_allowed = max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return diff <= max_allowed

#test
print(almost_equal(0.1 + 0.2, 0.3)) #True

#explanation
#so, the math.isclose() tests if float numbers are close to each other as, in python, 0.1 + 0.2 == 0.3 is not true.
#we are asked to implement the math.isclose() logic
#first, we get the max of abs value of the two variables. then we multiply it with the given relative tolerance to the actual tolerance
#then we get the max of actual tolerance and absolute tolerance, which is the intended answer
#then we return true or false based on the value we got as max_allowed. if the difference value is less than or equal to 
#the max_allowed value, then it's true that the difference is close, otherwise, not.
