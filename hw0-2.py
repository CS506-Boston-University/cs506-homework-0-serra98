import math 
import numpy as np


def import_data(filename):
    """ code followed from hw0 submission video """ 
    X = []
    y = []
    with open(filename, "r") as f: 
        next(f)
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
                elif v == 'S\n' or v == 'S': 
                    strings[index] = 2
                elif v == 'Q\n' or v == 'Q':
                    strings[index] = 1 
                elif v == 'C\n' or v == 'C':
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
    newXlist = []
    newylist = []
    total_rows = int(len(X))
    
    if t_f >= 1 or t_f <= 0 :
        raise 'invalid t_f'
    else: 
        index = list(range(total_rows))
        np.random.shuffle(index)
        for i in index: 
           newXlist.append(X[i])
           newylist.append(y[i])
    
    divide = int(total_rows * t_f)

    X_train = newXlist[divide:]
    X_test = newXlist[:divide]
    y_train = newylist[divide:]
    y_test = newylist[:divide]

    return X_train, y_train, X_test, y_test 

def train_test_CV_split(X, y,t_f,cv_f):
    newXlist = []
    newylist = []
    total_rows = int(len(X))

    if t_f > 1 or t_f < 0 :
        raise 'invalid t_f'
    elif  cv_f > 1 or cv_f < 0:
        raise 'invalid cv_f'
    elif  cv_f + t_f >= 1 :
        raise 'sum of cv_f and t_f should be less than 1'
    else: 
        index = list(range(total_rows))
        np.random.shuffle(index)
        for i in index: 
           newXlist.append(X[i])
           newylist.append(y[i])
    
    divide1 = int(total_rows * (1 - (t_f + cv_f)))
    divide2 = divide1 + int(total_rows * t_f)

    X_train = newXlist[:divide1]
    X_test = newXlist[divide1:divide2]
    X_cv = newXlist[divide2:]
    y_train = newylist[divide1:]
    y_test = newylist[divide1:divide2]
    y_cv = newylist[divide2:]

    return X_train, y_train, X_test, y_test, X_cv , y_cv

#print(import_data('train.csv'))
#print(import_data('test2.txt'))
#X,y = import_data('test2.txt')
#X,y = import_data('train.csv')
#print(train_test_split(X,y,0.5))
#print(train_test_CV_split(X, y,0.2,0.6))
#X,y = import_data('test2.txt')
#print(train_test_CV_split(X,y,0.2,0.6))