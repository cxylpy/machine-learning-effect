
datas=[[0, 1, 3, 4, 5, 9], [1, 2, 5, 7], [7, 8, 9], [0, 2, 3], [0, 1, 4, 6], [1, 2, 4, 5], [3, 5, 6, 7, 8], [1, 6, 7, 9], [3, 4, 7, 8, 9], [3, 4, 5, 7, 8, 9], [0, 6, 8, 9], [0, 4, 8, 9], [2, 4, 6, 7, 9], [0, 1, 2, 6, 7], [0, 1, 2, 3, 4, 6], [0, 2, 5, 6, 7, 8], [0, 2, 3, 6], [0, 1, 6, 7, 9], [1, 3, 4, 7], [0, 1, 3, 4, 8, 9], [0, 4, 5, 6, 8], [1, 5, 9], [5, 7, 9], [1, 2, 6, 7, 9], [0, 4, 5, 7, 8], [0, 1, 2, 6], [1, 2, 5, 7, 9], [1, 3, 5, 7, 8, 9], [1, 2, 5, 6, 7, 8, 9], [0, 2, 4, 6], [0, 1, 5, 6, 7, 9], [3, 4, 7, 8, 9], [2, 3, 6], [], [1, 3, 5, 6, 7], [1, 2, 5, 6, 7, 8], [1, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 4, 6, 8, 9], [1, 2, 3, 7, 8, 9], [2, 3, 4, 9], [2, 4, 5, 6, 7], [0, 1, 4, 5, 8], [2, 3, 8, 9], [3, 4, 5, 8, 9], [0, 3, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 8], [3, 5, 7], [0, 1, 2, 3, 6, 9], [0, 3, 4], [1, 2, 7], [0, 2, 4, 6, 9], [1, 2, 5, 7], [2, 3, 6, 9], [0, 1, 5, 8], [7, 8], [2, 3], [0, 1, 3, 6, 7], [0, 1, 2, 5, 7], [0, 1, 2, 3, 4, 6, 7, 8], [0, 1, 2, 3, 5, 7, 8], [1, 2, 5, 7, 9], [0, 1, 3, 4, 7], [2, 4, 7], [3], [0, 2, 3, 8, 9], [2, 8, 9], [4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 8], [0, 2, 3], [1, 2, 3, 4, 5, 6, 7], [4, 5, 8], [2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 8, 9], [0, 1, 5, 6, 9], [0, 1, 3, 4, 6], [3, 5, 7, 8], [2, 4, 9], [2, 3, 7], [1, 2, 4, 9], [0, 4], [1, 5, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7], [2, 4, 5, 6, 7, 8], [0, 4, 6], [0, 1, 5, 8, 9], [2, 3, 4, 7, 8], [3, 8], [2, 3, 4, 5, 9], [0, 1, 4, 5, 9], [1, 3, 4, 5, 7], [0, 2, 4, 5, 7], [2, 5, 6], [0, 5], [1, 3, 4, 7, 8], [0, 1, 2, 3, 6, 7, 8, 9], [5, 7, 9], [3, 4], [6, 8], [0, 2, 3, 5, 6, 8, 9]]

def algorithm(datas,min_support):
    data_sets = [set(data) for data in datas]
    sub_sets=[]
    for i in range(10):
        s=set([i])
        sub_sets.append(s)
    result_set=sub_set_method(sub_sets,data_sets,min_support)
    while result_set is not None:
        print result_set
        result_set = sub_set_method(result_set, data_sets, min_support)

def sub_set_method(sub_sets,data_sets,min_support):
    new_sub_sets=[]
    for i in range(len(sub_sets)):
        for j in range(i+1,len(sub_sets)):
            new_sub_sets.append(sub_sets[i].union(sub_sets[j]))

    dim = {str(x): 0 for x in new_sub_sets}
    for sub_set in new_sub_sets:
        for data_set in data_sets:
            if sub_set.issubset(data_set):
                dim[str(sub_set)] += 1

    new_dim={}
    for key,val in dim.iteritems():
        if val >= min_support:
            new_dim[key]=val

    result_sets=[]
    for key,val in new_dim.iteritems():
        result_sets.append(eval(key))

    if len(result_sets) == 0:
        return None
    return result_sets
algorithm(datas,20)