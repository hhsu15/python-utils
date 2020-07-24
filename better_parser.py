import parse

txt = "Author:Eric V. Smith <eric@trueblade.com>"

result = parse.search("Author:{name} <{email}>", txt)
print(result.named)
print(result['name'])
print(result.spans)


txt2 = """
I am a boy.
I am a student.
I am pretty.
"""

results = parse.findall("I am {something}.", txt2)
print(results)
for r in results:
    print(r)
