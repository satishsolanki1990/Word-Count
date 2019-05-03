from sys import argv
import re
if len(argv)==3:
    count=0
    a=set()
    with open(argv[1],'r') as f1:
        for line in f1:
            s= re.sub(r'[^\w\s]',' ',line)
            word=s.split()
            count+=len(word)
            for i in word:
                a.add(i.casefold())
    print('\n%s: \n   %d words \n   Unique: %d ' %(argv[1],count, len(a)))
    count=0
    b=set()
    with open(argv[2],'r') as f2:
        for line in f2:        
            s= re.sub(r'[^\w\s]',' ',line)
            word=s.split()
            count+=len(word)
            for i in word:
                b.add(i.casefold())
    print('%s: \n   %d words \n   Unique: %d ' %(argv[2],count, len(b)))
    print('Only %s: %d'%(argv[1],len(a-b)))
    print('Only %s: %d'%(argv[2],len(b-a)))
    print('Both files: %d'%len(a.intersection(b)))
else:
    raise ValueError('only two argumentsare allowed')
    exit()
