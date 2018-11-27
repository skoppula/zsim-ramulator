


import sys
import re

def filterTrace(inputName):
    #outputFile = open(outputName,"w")
    totalInstructions = 0
    instr_per_cpu = []
    cores = int(sys.argv[2])
    for i in range (0, cores):
        instr_per_cpu.append(0)
    #instr_per_cpu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (0,cores):
        inputNameNew = inputName+"."+str(i)
        inputFile = open(inputNameNew, "r")

        delta = 0
        intial = 0
        final = 0
        intr = 0
        cpu_id = 0
        print inputNameNew
        for line in inputFile:
            match = re.search(r'\d\s\d\s\d+\s\w\s', line)
            if(match):
                try:
                    instr = int (match.group().split()[2])
                    type = match.group().split()[3]
                    cpu_id = int( match.group().split()[1])
                    instr_per_cpu[cpu_id] +=  (instr+1)
                    #delta = final - intial
                    #tmp =  str(final)+" - "+str(intial)+" = "+str(delta)
                    #intial = final
                    if(type == "P"):
                        totalInstructions+=instr
                    else:
                        totalInstructions+=(instr+1)
                    #outputFile.write(line)
                except:
                    print inputNameNew
                    print "Error at line - "+line


            #if(totalInstructions > maxInstructions):
            #    break

    #print "Output file: "+outputName

    print "Total Instructions: "+str(totalInstructions)
    counter = 0
    for i in instr_per_cpu:
        print "CPU " + str(counter)+ ": "+str(i)
        counter  +=1


filterTrace(sys.argv[1])










