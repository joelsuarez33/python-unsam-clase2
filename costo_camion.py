import pandas as pd
datos = pd.read_csv('camion.csv')
df = pd.DataFrame(datos)
total = 0
alto=df.loc[0,'cajones']
for i in range(0,len(df)):
    costo = df.loc[i,'cajones']*df.loc[i,'precio']
    costof = round(costo,2)
    total = total + costof
print(total)