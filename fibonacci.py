def fibonacci_series(n):
    """Generate Fibonacci series up to n terms
    
    Args:
        n (int): Number of terms in the series
        
    Returns:
        list: List containing the Fibonacci series
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the series with first two numbers
    fib_series = [0, 1]
    
    # Generate subsequent numbers
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

# Example usage
if __name__ == '__main__':
    # Generate first 10 numbers in Fibonacci series
    result = fibonacci_series(10)
    print(f'First 10 numbers in Fibonacci series: {result}')