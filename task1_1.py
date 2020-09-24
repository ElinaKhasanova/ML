import pandas as pd
import matplotlib.pyplot as plt


def read_csv(file):
    dataset = pd.read_csv(file)
    return dataset


def fare(dataset):
    plt.hist(x = [dataset[dataset['survived']==1]['pclass'], dataset[dataset['survived']==0]['pclass']],
             stacked=False, color = ['g','r'])
    plt.title('Зависимость выживаемости от класса')
    plt.xlabel('Класс')
    plt.ylabel('Количество пассажиров')
    plt.show()

def embarked(dataset):
    dataset["embarked"].replace({"S": 1, "C": 2, "Q": 3}, inplace=True)
    plt.hist(x = [dataset[dataset['survived']==1]['embarked'], dataset[dataset['survived']==0]['embarked']], 
             stacked=False, color = ['g','r'])
    plt.title('Зависимость выживаемости от порта посадки')
    plt.xlabel('Порт посадки')
    plt.ylabel('Количество пассажиров')
    plt.show()


dataset = read_csv('titanic/train.csv')
#fare(dataset)
embarked(dataset)
