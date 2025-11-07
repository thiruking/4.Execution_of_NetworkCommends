import os

website = input("Enter the website to traceroute: ")
result = os.popen(f"tracert {website}").read()

print("\nTraceroute Result:\n")
print(result)