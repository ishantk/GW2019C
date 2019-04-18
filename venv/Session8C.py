# main represents main thread which executes instructions
# in the program in a sequence

def main():
    a = 10
    b = [10, 20, 30, 40, 50]

    print(a)
    print(b)

print("Hello")
print(__name__) # -> __main__

if __name__ == "__main__":
    main()