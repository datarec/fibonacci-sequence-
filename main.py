# Fibonacci sequence in python. 23/06/2024 

def main():
    # Variable that holds the number of loops the program is up to
    count = 0

    # List used to store expression of seq
    values = [0, 1]
    
    while count != 25: 
        seq = values[0] + values[1]

        # Prints the seq expression
        print(seq)

        # Appends the expression 
        values.append(seq) 

        # Removes first index 
        values.pop(0)

        # Adds 1 to count variables to keep count of loops. 
        count += 1


if __name__ == "__main__":
    
