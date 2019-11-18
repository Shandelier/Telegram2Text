import re

text, author1, content, author2 = "", "", "", ""

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for line in input_file:
    line.rstrip()
    if line.isspace():
        continue
    if (re.search("\[In reply", line)):
        text += "[reply] "
        continue
    if (re.search(".*\[.*\]", line)):
        author2 = author1
        author1 = re.split(",.\[", line, 1)[0]
        if author1 == author2 or not author1 and not author2:
            continue
        text += "\n" + line
    else:
        text += line

output_file.write(text)
print(text)

input_file.close()
output_file.close()
