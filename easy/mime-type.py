#https://www.codingame.com/ide/puzzle/mime-type


n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_dict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt
for i in range(q):
    fname = input().lower() 
    if "." in fname:
        ext = fname.rsplit(".", 1)[-1]
        if ext in mime_dict:
            print(mime_dict[ext])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")


