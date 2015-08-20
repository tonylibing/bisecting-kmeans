from kmeans.dataset import Dataset
from kmeans.bisectingKmeans import BisectingKmeans


class DataLoader():

    def __init__(self, filename, fields):
        def tryToFloat(value):
            try:
                return float(value)
            except ValueError:
                return value

        self.fields = fields
        loadedData = [tuple(map(tryToFloat, line.rstrip().split(',')))
                      for line in open(filename, 'r').readlines()][:-1]

        dataZiped = list(zip(*loadedData))

        for i, field in enumerate(fields):
            if 'types' in field:
                try:
                    dataZiped[i] = [field['types'][v] for v in dataZiped[i]]
                except KeyError as e:
                    print(e)
                    raise Exception("The field structure don't fit the data.")

        self.data = list(zip(*dataZiped))

if __name__ == "__main__":
    irisFields = [
        {'name': 'sepal length'},
        {'name': 'sepal width'},
        {'name': 'petal length'},
        {'name': 'petal width'},
        {'name': 'class', 'types': {
            'Iris-setosa': 0,
            'Iris-versicolor': 1,
            'Iris-virginica': 2
        }}
    ]

    wineFields = [
        {'name': 'identifier'},
        {'name': 'alcohol'},
        {'name': 'malic acid'},
        {'name': 'ash'},
        {'name': 'alcalinity of ash'},
        {'name': 'magnesium'},
        {'name': 'total phenols'},
        {'name': 'flavanoids'},
        {'name': 'nonflavanoid phenols'},
        {'name': 'proanthocyanins'},
        {'name': 'color intesity'},
        {'name': 'hue'},
        {'name': 'OD280/OD315 of diluted wines'},
        {'name': 'proline'
         }
    ]

    hungarianFields = [
        {'name': 'age'},
        {'name': 'sex'},
        {'name': 'cp'},
        {'name': 'trestbps'},
        {'name': 'chol'},
        {'name': 'fbs'},
        {'name': 'restecg'},
        {'name': 'thalach'},
        {'name': 'exang'},
        {'name': 'oldpeak'},
        {'name': 'slope'},
        {'name': 'ca'},
        {'name': 'thal'},
        {'name': 'num'
         }
    ]

    loader = DataLoader('iris.data', irisFields)
    loader = DataLoader('wine.data', wineFields)
    loader = DataLoader('reprocessed.hungarian.data', hungarianFields)
    ds = Dataset(data=loader.data)
    bisection = BisectingKmeans(dataset=ds, k=4, trials=20, maxRounds=100)
    bisection.run()
    bisection.showResults()