from itertools import permutations

def solve_cryptarithmetic(equation):
    # Remove spaces
    equation = equation.replace(" ", "")
    
    # Extract unique letters
    letters = set(filter(str.isalpha, equation))
    
    if len(letters) > 10:
        print("Too many letters! Cannot solve.")
        return
    
    letters = list(letters)
    
    # Prepare digits
    digits = range(10)
    
    # Try all possible permutations of digits for the letters
    for perm in permutations(digits, len(letters)):
        # Map letters to digits
        mapping = dict(zip(letters, perm))
        
        # Skip if any number starts with zero
        skip = False
        for word in equation.replace("+", " ").replace("-", " ").replace("=", " ").split():
            if mapping[word[0]] == 0:
                skip = True
                break
        if skip:
            continue
        
        # Replace letters with digits in the equation
        expr = equation
        for letter, digit in mapping.items():
            expr = expr.replace(letter, str(digit))
        
        # Check if equation is valid
        left, right = expr.split("=")
        if eval(left) == eval(right):
            print("Solution Found:")
            for letter in mapping:
                print(f"{letter} -> {mapping[letter]}")
            print("Equation:", expr)
            return
    
    print("No solution exists.")

# Dynamic input
user_equation = input("Enter a cryptarithmetic equation (e.g., SEND + MORE = MONEY): ")
solve_cryptarithmetic(user_equation)