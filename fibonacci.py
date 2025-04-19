def fibonacci(n):
    """Calculate Fibonacci series up to nth term
    Args:
        n (int): Number of terms to generate
    Returns:
        list: List containing the Fibonacci series
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

# Example usage
if __name__ == '__main__':
    # Generate first 10 numbers of Fibonacci series
    result = fibonacci(10)
    print(f'First 10 numbers of Fibonacci series: {result}')