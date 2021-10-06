numberindexinput=input("how index fibonachi:")
Fibonacci=[1,2]

for i in range(3,int(numberindexinput)+1):
    Fibonacci.append(Fibonacci[i-2]+Fibonacci[i-3])
        
print(f"Fibonacci sequence numbers are entered up to that index = {Fibonacci}")
print(f"The desired number of the Fibonacci sequence:{Fibonacci[i-1]}")