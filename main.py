import pandas as pd
import Linear_regression

def main():
    data = pd.read_csv("Fortune500beg.csv")
    print(data)
    y = list(data['Profits ($M)'])
    for i in range(len(y)):
        y[i] = [y[i]]

    matrix = []
    for i in range(len(data['Profits ($M)'])):
        matrix.append([data['Revenues ($M)'][i], data['Assets ($M)'][i], data['Total Stockholder Equity ($M)'][i]])
    print(matrix)
    transposed = Linear_regression.transpose(matrix)
    print(transposed)
    multiplication = Linear_regression.multiplication(matrix, transposed)
    coef = Linear_regression.lin(multiplication, transposed, y)
    return coef

print(main())
