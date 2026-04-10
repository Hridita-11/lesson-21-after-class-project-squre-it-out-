def square_values(start, end):
    squares = []
    for num in range(start, end + 1):
        squares.append(num * num)
    return squares
def filter_odd_even(numbers):
    odd = []
    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return odd, even
def main():
    print("Square Value Finder")
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    squares = square_values(start, end)
    odd_squares, even_squares = filter_odd_even(squares)
    print("\nAll square values:", squares)
    print("Odd square values:", odd_squares)
    print("Even square values:", even_squares)
if __name__ == "__main__":
    main()
