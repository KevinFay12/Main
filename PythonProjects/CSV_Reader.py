import csv

with open('POSITION.LIMITS.20180130.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    symbols = []
    positionlimits = []
    
    for row in readCSV:
        symbol = row[0]
        positionlimit = row[1]

        symbols.append(symbol)
        positionlimits.append(positionlimit)

    try:
        whatSymbol = input('what symbol do you want to know the position limit of?')

        if whatSymbol in symbols:
            SymbolDex = symbols.index(whatSymbol.upper())
            theLimit = positionlimits[SymbolDex]
            print('The posiiton limit of',whatSymbol,'is',theLimit,)
        else:
            print('symbol not found')
    #except Exception, e:
    except Exception as e:
        print(e)
    print('continuing')
