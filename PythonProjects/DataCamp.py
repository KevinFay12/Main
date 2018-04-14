import pandas as pd
field = ['ComponentSymbol']
yourData = pd.read_csv('POSITION.LIMITS.20180130.csv', usecols=field,) 
writer = pd.ExcelWriter('exampleFile124.xlsx', engine='xlsxwriter')
yourData.to_excel(writer, 'exampleFile124')
writer.save()
