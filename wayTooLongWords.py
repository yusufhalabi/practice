for i in range(input()):
    s = raw_input()
    if s.len()<10: 
        print s 
    else: 
        print "%s %d %s" % (s[0],s.len()-2,s[-1]) 