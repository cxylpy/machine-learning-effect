# coding=utf-8
#共10个属性，4个类别
#类别分别是各属性和在(0,10]，(10,20],(20,30],(30,45]，分别对应a,b,c,d

train_datas=[
    [0, 1, 3, 4, 7],
    [1, 2, 4, 6, 8],
    [1, 2, 4, 5, 6, 7],
    [0, 1, 3, 5, 6, 7, 8],
    [2, 4, 6, 7],
    [1, 3, 5, 6, 9],
    [0, 2, 4, 5, 8, 9],
    [0, 1, 2, 3, 4, 6, 8, 9],
    [4, 5, 6, 8, 9],
    [1, 2, 3, 4],
    [0, 5, 7, 9],
    [3, 6, 7, 9],
    [1, 5, 7, 8, 9],
    [1, 4, 5, 8, 9],
    [2, 8],
    [0, 1, 3, 6, 7],
    [1, 5, 6, 7, 9],
    [0, 3, 4, 5, 6, 8, 9],
    [1, 2, 3, 5, 9],
    [0, 2, 6, 8],
    [5, 8],
    [1, 4, 5, 6, 7, 8],
    [1, 2, 6],
    [1, 2, 4, 7],
    [1, 3, 4, 5, 9],
    [1, 4, 7, 8, 9],
    [2, 3, 5, 6, 8],
    [0, 2, 5, 6, 9],
    [0, 1, 2, 3, 5, 9],
    [0, 1, 4, 7, 9],
    [3, 4, 6, 7, 8],
    [4, 6, 7],
    [2, 3, 9],
    [1, 4, 9],
    [2, 3, 4, 5, 7, 8, 9],
    [0, 2, 5],
    [2, 5],
    [0, 2, 6, 8, 9],
    [0, 2, 3, 4, 6, 8],
    [0, 1, 2, 4],
    [0, 2, 3, 7],
    [0, 4, 5, 7, 8],
    [2, 3, 5, 8, 9],
    [0, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 6, 8],
    [1, 2, 5, 6, 7, 9],
    [0, 1, 4, 5, 6, 9],
    [1, 2, 4, 5],
    [0, 1, 4, 7],
    [2, 3, 4, 5, 8, 9],
    [2, 3, 4, 5, 7, 8],
    [0, 3, 6],
    [0, 1, 5, 6, 8],
    [2, 3, 6, 7],
    [4, 5, 6, 7, 8],
    [0, 2, 4, 6, 8],
    [0, 1, 2, 3, 4, 5, 6, 8],
    [0, 2, 4, 6],
    [1, 3, 4, 6, 7],
    [2, 3, 5, 6],
    [3, 4, 5, 6, 8, 9],
    [0, 3, 4, 6, 8],
    [0, 1, 2, 4, 6, 9],
    [0, 3, 6, 8, 9],
    [5, 7, 9],
    [2, 4],
    [5],
    [0, 1, 2, 5, 8],
    [0, 4, 5, 6],
    [1, 2, 6, 8],
    [1, 2, 3, 4, 6],
    [0, 3, 4, 5, 6],
    [0, 1, 8],
    [2, 9],
    [2, 6, 7, 9],
    [4, 5, 7, 9],
    [0, 2, 4, 8],
    [0, 2, 5, 6, 7],
    [0, 1, 5, 7, 8],
    [5, 7],
    [1, 3, 4, 7, 8],
    [0, 2, 5, 8, 9],
    [0, 1, 8, 9],
    [0, 3, 4, 5, 7],
    [0, 1, 4, 5, 8, 9],
    [0, 1, 2, 3, 7, 8, 9],
    [0, 4, 6],
    [3, 4, 5, 6, 7, 9],
    [0, 1, 2, 3, 4, 8, 9],
    [5, 6],
    [1, 3, 4, 6, 8, 9],
    [6, 8, 9],
    [1, 3, 5, 6, 8],
    [4, 5],
    [0, 4, 9]
]
train_types=['b', 'c', 'c', 'c', 'b', 'c', 'c', 'd', 'd', 'a', 'c', 'c', 'c', 'c', 'c', 'a', 'b', 'd', 'b', 'b', 'b', 'd', 'a', 'b', 'c', 'c', 'c', 'c', 'b', 'c', 'c', 'b', 'b', 'b', 'd', 'a', 'a', 'c', 'c', 'a', 'b', 'c', 'c', 'b', 'c', 'b', 'c', 'c', 'b', 'b', 'd', 'c', 'a', 'b', 'b', 'b', 'b', 'c', 'b', 'c', 'b', 'd', 'c', 'c', 'c', 'c', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'a', 'b', 'c', 'c', 'b', 'b', 'c', 'b', 'c', 'c', 'b', 'b', 'c', 'c', 'a', 'd', 'c', 'b', 'd', 'c', 'c', 'a', 'b']
test_datas=[
    [1,2,3,4,5],
    [5,6,7,8,9],
    [1,3,5,7,8],
]

def algorithm(train_datas,train_types,test_datas):
    all_attr=[i for i in range(10)]
    types=['a','b','c','d','e']
    types_num={'a':0,'b':0,'c':0,'d':0,'e':0}
    p={}
    length=len(train_datas)
    for val in train_types:
        types_num[val]+=1
    for type in types:
        p[type]=float(types_num[type])/float(length)
    temp_dict={}
    for i in range(len(train_datas)):
        for j in range(10):
            key = "%s%s%s"%(train_types[i],train_datas[i].count(j) and '+' or '-',j)
            if temp_dict.get(key):
                temp_dict[key]+=1
            else:
                temp_dict[key]=1
    for key,val in temp_dict.iteritems():
        temp_dict[key] = float(temp_dict[key]) / float(types_num[key[0]])
    results=[]
    for data in test_datas:
        result={}
        for type in types:
            for attr in all_attr:
                key = "%s%s%s"%(type,data.count(attr) and '+' or '-',attr)
                r=result.get(type)
                prob=temp_dict.get(key)
                if not prob:continue
                if not r:
                    result[type]=prob
                else:
                    result[type]=float(r)*float(prob)

        results.append(result)
        for key,val in result.iteritems():
            result[key]=float(val)*float(p[key])

    for result in results:
        print sorted([(v, k) for k, v in result.items()],reverse=True)
algorithm(train_datas,train_types,test_datas)