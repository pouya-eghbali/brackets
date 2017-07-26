import brackets

def main():
    import sys
    import os.path
    file = sys.argv[1]
    with open(file, 'r', encoding='utf8') as f:
        compiled, debug, original = brackets.translate(f.read(), True)
    print(compiled)

if __name__ == '__main__':
    main()
