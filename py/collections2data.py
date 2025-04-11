from os import scandir
from os.path import splitext
from re import fullmatch
from sys import stderr

def attrs(path: str):
    triples_count = 0
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '---':
                triples_count += 1
            else:
                m = fullmatch(r'(.+): (.+)', line)
                if not m:
                    raise ValueError('Wrong format of the line')
                yield m[0], m[1], m[2]
    if triples_count != 2:
        raise ValueError('Wrong triples count')

def collection2data(collection: str):
    with (open(f'_data/{collection}.yml', 'w') as f,
        scandir(f'_{collection}') as collection_items):
        
        for item in sorted(collection_items, key=lambda item: item.name):
            if not item.is_file():
                print(f'Non-file: {item.path}', file=stderr)
                continue
            name, ext = splitext(item.name)
            if ext != '.md':
                print(f'Non-md file: {item.path}', file=stderr)
                continue

            f.write(f'{name}:\n')
            for line, attr, value in attrs(item.path):
                if attr == 'code' and value != name:
                    print(f'Wrong code: {item.path}', file=stderr)
                f.write(f'  {line}\n')
            f.write('\n')

for collection in ['countries', 'series', 'stations', 'itus']:
    collection2data(collection)