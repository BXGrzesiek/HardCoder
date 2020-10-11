from googlesearch import search

query = "wikipedia"

search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
print(i)

# try:
# 	from googlesearch import search
# except ImportError:
# 	print("No module named 'google' found")

# to search
# query = "Geeksforgeeks"

# for j in search(query, tld="co.in", num=10, stop=10, pause=2):
# 	print(j)

# try:
# 	from searchgoogle import search
# except ImportError:
# 	print("No module named 'google' found")

# to search
# query = "A computer science portal"

# for j in search(query, tld="co.in", num=10, stop=10, pause=2):
# 	print(j)