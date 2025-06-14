import requests
book=requests.get("https://www.gutenberg.org/cache/epub/76269/pg76269.txt")
r=book.text
with open ('file.txt','w') as f:
    f.writelines(r)
