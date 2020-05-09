days = dict()
fname = input ('Enter a file name:')
times = dict()
try :
    fh = open (fname)
except:
    print ('This file dose not exist')
    quit()
for line in fh:
    if not line.startswith('From '): continue
    line = line.rstrip()    
    print(line)
    words = line.split()
    #if len(words)<6 : continue
    time = words[5].split(':')
    #print(time)
    times[time[0]]=times.get(time[0],0)+1
#print(times)
lis=list()
for key,value in times.items():
    lis.append((key,value))
#print (lis)
lis.sort()
for key,value in lis:
    print (key,value) 