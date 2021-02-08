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
            # replace missing value "?" and store them as NaN value 
            replaceStr = [math.nan if v == '?' else float(v) for v in strings] 
            # for each value type cast it to the correct type 
            for s in replaceStr:  
                try: 
                    z = int(s) 
                except ValueError:
                    try: 
                        z = float(s)
                    except ValueError: 
                        z = s 
            attributes = replaceStr[:279] 
            cc = int(replaceStr[279])
            X.append(attributes)
            y.append(cc)
    return X,y

def impute_missing(X):
    """imputes these missing entries with median """ 
    for lists in X[0:len(X)]:
        list_Sorted = sorted(lists, key=lambda x: x if not math.isnan(x) else 0.0 )
        
        count_Lists = len(lists)

        if count_Lists % 2 != 0:
            med = list_Sorted[count_Lists//2]
        else:
            med1 = list_Sorted[count_Lists//2]
            med2 = list_Sorted[count_Lists//2 - 1]
            med = (med1 + med2) / 2
        
        for v in lists:
            if math.isnan(v):
                lists[lists.index(v)] = med

    return X

def discard_missing(X,y):
    """discard completely the samples do not have an entry for every attribute """ 
    newlistX = []
    newlisty = [] 

    for lists in range(len(X)): 
        if len([x for x in X[lists] if math.isnan(x)]) > 0 :
           continue 
        else: 
           newlistX.append(X[lists])
           newlisty.append(y[lists])
    X = newlistX 
    y = newlisty 
    return X,y
           
def shuffle_data(X,y):
    """ shuffle the data - used numpy and zip function to shuffle x,y at the same time """
    newXlist = []
    newylist = [] 
    index = list(range(len(X)))
    np.random.shuffle(index)
    for i in index: 
        newXlist.append(X[i])
        newylist.append(y[i])
    X = newXlist 
    y = newylist 
    return X,y 

def compute_mean(X):
    """ get mean for standard deviation """
    num_of_rows = len(X)
    num_of_cols = len(X[0])
    mean = []

    for c in range(num_of_cols):
        total = 0.0
        for r in range(num_of_rows):
            total = total + X[r][c]
        mean.append(total/num_of_rows)
        
    return mean
            

def compute_std(X):
    """ calculate standard dev by columns  """ 
    num_of_rows = len(X)
    num_of_cols = len(X[0])
    std_dv = []
    mean = compute_mean(X)
    
    for c in range(num_of_cols):
        total = 0
        for r in range(num_of_rows):
            total = total +  ((X[r][c] - mean[c] ) ** 2.0)
        final_sqrt = (total / (num_of_rows)) ** 0.5 
        std_dv.append(final_sqrt)
    
    return std_dv

def remove_outlier (X,y): 
    """removes all entries that contain a feature value which is more than two standard deviations away frrom the mean of that feature. """
    
    num_of_rows = len(X)
    num_of_cols = len(X[0])
    mean_list = compute_mean(X)
    std_dv_list = compute_std(X)
    
    
    for c in range(num_of_cols):
        mean = mean_list[c]
        stdv = std_dv_list[c]
        for r in range(num_of_rows):
            if X[r][c] < (mean - stdv * 2.0 ) or X[r][c] > (mean + stdv * 2.0):
                X.remove(X[r])
                y.remove(y[r])
    return X,y 

def standardize_data(X):
    """ standardizes all the data points """
    num_of_rows = len(X)
    num_of_cols = len(X[0])
    mean_list = compute_mean(X)
    std_dv_list = compute_std(X)
    
    for c in range(num_of_cols):
        mean = mean_list[c]
        stdv = std_dv_list[c]
        for r in range(num_of_rows):
            if stdv == 0.0: 
                X[r][c] = (X[r][c] - mean) 
            else: 
                X[r][c] = (X[r][c] - mean) / stdv 
    return X,y 




#print(import_data('arrhythmia.data'))
#X,y = import_data('arrhythmia.data')
#print(import_data('test.txt'))
#X,y = import_data('test.txt')
#print(y)
#print(impute_missing(X))
#print(discard_missing(X,y))
#print(discard_missing(X,y))
#X,y = discard_missing(X,y)
#print(shuffle_data(X,y))
#print(compute_mean(X))
#print(compute_std(X))
#print(standardize_data(X))
#print(remove_outlier(X,y))










