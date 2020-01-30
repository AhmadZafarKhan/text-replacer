import os

def main():

    path = input("enter path: ")
    replacement = "2 "
    current_text = "0 "
    for dname, dirs, files in os.walk(path):
        for fname in files:
            fpath = os.path.join(dname, fname)
            print(fname)
            if not fname.startswith("."):
                with open(fpath, "r") as f:
                    s = f.read()
                    print(fname)
                s = s.replace(current_text, replacement)
                with open(fpath, "w") as f:
                    f.write(s)
if __name__ == '__main__':
    main()
