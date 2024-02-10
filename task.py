def main():
    print("Enter the size of hexagon:-")
    row, col = map(int, input().split())
    for i in range(col // 2 + 1):
        print(" ___    ", end='')
    print("")

    for i in range(2 * row):
        if i % 2 == 0:
            for j in range(col // 2):
                print("/   \\___", end='')
            print("/   \\")
        else:
            for j in range(col // 2 + 1):
                print("\\___/   ", end='')
            print()

if __name__ == "__main__":
    main()
