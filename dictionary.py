import sys
word = sys.argv[1]
path = 'gene.txt'
with open(path) as f:
    value = f.readlines()
line_count = 0
for result in value:
    line_count +=1
    result_replace = result.replace("\n","")
    if word == result_replace:
        print(value[line_count],end="")
    else:
        pass
