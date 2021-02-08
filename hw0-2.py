import math 
import numpy as np

def import_data(filename):
    """ code followed from hw0 submission video """ 
    X = []
    y = []
    with open(filename, "r") as f: 
        lines = f.readlines() 
        for line in lines: 
            # separate the values from csv to list 
            strings = line.split(",")
            # replace values
            for index, v in enumerate(strings):
                if v == 'female':
                    strings[index] = 0
                elif v == 'male':
                    strings[index] = 1
                elif v == 'S\n': 
                    strings[index] = 2
                elif v == 'Q\n':
                    strings[index] = 1 
                elif v == 'C\n':
                    strings[index] = 0
                else: 
                    strings[index] = v

            # for each value type cast it to the correct type 
            for s in strings:  
                try: 
                    z = int(s) 
                except ValueError:
                    try: 
                        z = float(s)
                    except ValueError: 
                        z = s 
            length = int(len(strings)) - 1
            attributes = strings[:length] 
            survival = strings[length]
            X.append(attributes)
            y.append(survival)
    return X,y

def train_test_split (X, y ,t_f):
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    if t_f >= 1 or t_f <= 0 :
        raise 'invalid t_f'
    else: 
        continue 
    return X_train, y_train, X_test, y_test 

def train_test_CV_split(X, y,t_f,cv_f):
    return X_train, y_train, X_test, y_test, X_cv, y_cv 

print(import_data('train.csv'))
X,y = import_data('train.csv')