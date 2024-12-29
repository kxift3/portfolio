import sys

if len(sys.argv) > 1:
    shortest = min(sys.argv[1:], key=len)
    print(f"The shortest argument is: {shortest}")
else:
    print("No arguments provided.")
