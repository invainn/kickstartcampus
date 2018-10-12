def gbus_count(gbusRoutes, city):
    counter = 0

    for route in gbusRoutes:
        if (city >= route[0] and city <= route[1]):
            counter += 1

    return counter 

testCases = int(input(""))
overallResults = []

for i in range(testCases):
    results = []
    gbusCount = ""

    while(gbusCount == ""):
        gbusCount = input("")
   
    gbusCount = int(gbusCount)

    gbusRoutes = input("").split()

    gbusTuples = [ (int(gbusRoutes[i-1]), int(gbusRoutes[i])) for i in range(1, len(gbusRoutes), 2) ] 

    interested = int(input())

    # will have all interested cities in this list
    interestedList = []

    for j in range(interested):
        interestedList.append(int(input()))

    for interested in interestedList:
        results.append(gbus_count(gbusTuples, interested))

    overallResults.append(results)


for i in range(0, len(overallResults)):
    print("Case #" + str(i+1) + ":", end=" ")
    print(*overallResults[i])
