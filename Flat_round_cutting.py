import sys
def max_regions(n):
    return n * n - n + 2
def main():
    input_data = sys.stdin.read().strip()
    numbers = list(map(int, input_data.split()))
    for n in numbers:
        print(max_regions(n))
if __name__ == "__main__":
    main()
