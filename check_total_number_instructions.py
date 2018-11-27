import sys
import re
def filterTrace(inputName):
    #outputFile = open(outputName,"w")
    inputFile = open(inputName, "r")

    delta = 0
    intial = 0
    final = 0
    intr = 0
    cpu_id = 0
    totalInstructions = 0
    print inputName
    instr_per_cpu = [0,0,0,0]
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
		   totalInstructions+=instr+1
                #outputFile.write(line)
            except:
                print "Error at line - "+line


            #if(totalInstructions > maxInstructions):
            #    break

    print "Total Instructions: "+str(totalInstructions)
    #print "Output file: "+outputName
    counter = 0
    for i in instr_per_cpu:
        print "CPU " + str(counter)+ ": "+str(i)
        counter  +=1


filterTrace(sys.argv[1])
