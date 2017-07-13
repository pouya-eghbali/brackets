import brackets

def main():
    import sys
    import os.path
    file = sys.argv[1]
    with open(file, 'r', encoding='utf8') as f:
        compiled = brackets.translate(f.read())
    print(compiled)

if __name__ == '__main__':
    main()
