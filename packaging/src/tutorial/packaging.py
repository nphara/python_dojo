import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

message= f" Python package example! "

message2="""

In the same directory of .toml, run :

py -m build

References
==========

[1] https://packaging.python.org/en/latest/tutorials/packaging-projects/
[2] https://realpython.com/python-modules-packages/
"""

contents = {"Introduction": 1, "Python Basics": 5, "Creating Your First Program": 12, "Operators and Variables": 29}

print(f"\n{message:*^50}\n")

print(f"\n{message2:^100}\n")

for chapt, page in contents.items():
    print(f"{chapt:.<30}{page:.>5}")

