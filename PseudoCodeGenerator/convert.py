"""
    针对《算法导论》风格代码的伪代码行号生成器
    A pseudo code line number generator for "Introduction to Algorithms" style code

    -- 2025-03-14 19:33 by Jeb
"""
import os

def process(root, filename):
    if "_m" not in filename:
        return
    
    print(f"Processing {filename} in {root} ...")

    pre, ed = filename.split('.')
    if pre[-2:] == '_m':
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
            items = []
            for line in lines:
                item = {
                    'type': 'process',
                    'num': 0,
                    'content': '',
                }
                line = line.strip()
                if line == "":
                    item['type'] = 'empty'
                    if items and items[-1]['type'] == 'empty':
                        continue
                    item['num'] = items[-1]['num'] + 1 if items else 1
                elif line[:3] == 'Def':
                    if items and items[-1]['type'] == 'empty':
                        items[-1]['num'] = ''
                    elif items and items[-1]['type'] != 'empty':
                        items.append(item)
                    item['type'] = 'name'
                    item['content'] = line[4:]
                    print(line[0])
                    print(line[1])
                    print(line[2])
                    print(line[3])
                    print(line[4])
                    print(line[5])
                    item['num'] = 0
                else:
                    item['type'] = 'process'
                    item['num'] = items[-1]['num'] + 1 if items else 1
                    item['content'] = line
                items.append(item)

        if items:
            while items[-1]['type'] == 'empty':
                items.pop()

        with open(os.path.join(root, f"{pre[:-2]}.{ed}"), "w", encoding="utf-8") as f:
            for item in items:
                item['num'] = f'{item["num"]} ' if item['num'] != 0 else ''
                line = f"{item['num']}{item['content']}"
                print(line)
                f.write(line)


for root, dirs, files in os.walk("./"):
    for file in files:
        process(root, file)