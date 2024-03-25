def main():
    try:
        with open("input.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]
            total = sum(numbers)
            formatted_total = format(total, ",d")
            print(formatted_total)
    except FileNotFoundError:
        print("Error: input.txt not found")
    except ValueError:
        print("Error: input.txt contains invalid data")

if __name__ == "__main__":
    main()
