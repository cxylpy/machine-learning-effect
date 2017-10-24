# coding=utf-8
from __future__ import unicode_literals
from math import log
from copy import copy
#5个属性，每个属性5个值1,2,3,4,5，计算每个元组的属性和序号的乘积，再计算和得出类别
# a:[15,30)   b:[30,45)   c:[45,60)   d:[60,75]
train_data=[[3, 3, 1, 2, 5], [4, 4, 2, 3, 1], [1, 2, 3, 4, 1], [5, 1, 3, 5, 2], [3, 4, 3, 5, 1], [4, 4, 3, 1, 5], [3, 4, 2, 2, 2], [4, 4, 3, 4, 4], [1, 3, 5, 1, 4], [4, 1, 2, 1, 1], [2, 1, 4, 5, 3], [4, 4, 5, 1, 1], [3, 3, 2, 2, 1], [2, 2, 3, 3, 5], [5, 3, 5, 4, 3], [5, 2, 1, 5, 4], [3, 2, 2, 3, 1], [5, 3, 1, 1, 3], [5, 1, 5, 1, 2], [4, 2, 2, 5, 4], [4, 4, 2, 3, 1], [1, 4, 3, 5, 4], [5, 3, 4, 3, 3], [2, 5, 4, 4, 1], [5, 1, 4, 1, 4], [1, 2, 3, 2, 3], [4, 2, 4, 5, 5], [5, 2, 1, 2, 2], [4, 2, 4, 5, 5], [3, 2, 2, 1, 4], [3, 1, 1, 4, 1], [1, 5, 1, 4, 5], [5, 5, 4, 5, 4], [2, 4, 1, 4, 2], [5, 3, 4, 4, 4], [4, 5, 5, 3, 4], [4, 3, 3, 1, 1], [1, 3, 4, 3, 4], [3, 4, 5, 4, 3], [1, 4, 2, 3, 3], [3, 2, 5, 5, 2], [4, 2, 5, 2, 1], [1, 5, 4, 5, 5], [2, 3, 3, 2, 1], [3, 5, 2, 3, 4], [2, 5, 1, 5, 2], [4, 3, 4, 2, 1], [2, 3, 3, 5, 1], [1, 4, 4, 5, 1], [2, 2, 5, 5, 3], [5, 1, 1, 2, 2], [4, 5, 2, 2, 3], [1, 4, 5, 4, 4], [4, 4, 5, 4, 3], [3, 3, 5, 2, 4], [5, 2, 2, 5, 3], [5, 4, 1, 2, 5], [3, 3, 3, 1, 2], [5, 2, 3, 5, 3], [5, 1, 3, 5, 4], [3, 3, 2, 4, 3], [3, 5, 3, 5, 3], [4, 5, 5, 5, 4], [2, 3, 1, 5, 4], [1, 4, 1, 4, 1], [5, 2, 2, 1, 5], [3, 4, 3, 3, 2], [5, 5, 5, 4, 1], [5, 3, 4, 5, 5], [3, 3, 4, 4, 5], [4, 1, 4, 5, 4], [1, 5, 5, 3, 5], [2, 2, 5, 3, 1], [5, 1, 4, 3, 2], [5, 4, 4, 3, 5], [4, 3, 4, 1, 2], [3, 3, 2, 1, 5], [2, 1, 2, 4, 4], [5, 3, 2, 5, 2], [2, 3, 5, 5, 1], [2, 1, 5, 5, 5], [2, 2, 3, 1, 1], [5, 4, 2, 5, 4], [3, 1, 5, 1, 3], [5, 3, 3, 4, 1], [5, 4, 4, 5, 4], [5, 2, 4, 5, 4], [5, 1, 1, 1, 3], [2, 2, 3, 4, 2], [3, 3, 2, 3, 1], [2, 2, 5, 3, 1], [5, 2, 4, 1, 5], [2, 4, 3, 4, 4], [3, 5, 2, 5, 1], [2, 1, 2, 2, 4], [2, 4, 5, 1, 4], [4, 3, 2, 3, 3], [4, 1, 3, 5, 2], [5, 3, 4, 4, 1], [3, 1, 2, 5, 1]]
train_class=[u'c', u'b', u'b', u'c', u'c', u'c', u'b', u'c', u'c', u'a', u'c', u'b', u'a', u'c', u'c', u'c', u'b', u'b', u'b', u'c', u'b', u'c', u'c', u'c', u'b', u'b', u'd', u'b', u'd', u'b', u'a', u'c', u'd', u'b', u'c', u'd', u'a', u'c', u'c', u'b', u'c', u'b', u'd', u'b', u'c', u'c', u'b', u'b', u'c', u'c', u'a', u'b', u'd', u'c', u'c', u'c', u'c', u'b', u'c', u'c', u'c', u'c', u'd', u'c', u'b', u'b', u'b', u'c', u'd', u'd', u'c', u'd', u'b', u'b', u'd', u'b', u'b', u'c', u'c', u'c', u'd', u'a', u'c', u'b', u'b', u'd', u'd', u'a', u'b', u'b', u'b', u'c', u'c', u'b', u'b', u'c', u'b', u'c', u'b', u'b']
attr_idx=[0,1,2,3,4]

class Node:
    attr_idx=None
    attr_val=None
    rest_attr_idx=None
    children=None
    indexes=None

    def __init__(self,attr_idx=None,attr_val=None):
        self.children = []
        self.rest_attr_idx = []
        self.indexes = []
        self.attr_idx = attr_idx
        self.attr_val = attr_val

def id3_main():
    root = Node()
    root.indexes = range(len(train_data))
    root.rest_attr_idx = copy(attr_idx)
    id3(root)
    return root

def id3(node):
    target_attr_idx=None
    min_sum = 9999999
    children = []
    if len(node.rest_attr_idx) == 0:
        return
    if len(node.indexes) == 0:
        return
    last_clazz=None
    all_the_same=True
    for index in node.indexes:
        if last_clazz is None:
            last_clazz=train_class[index]
            continue
        if train_class[index] != last_clazz:
            all_the_same = False
            break
    if all_the_same:
        print "all the same:",node.indexes
        return
    for attr_idx in node.rest_attr_idx:
        info_sum,temp_children = info_after_divide(node, attr_idx)
        if min_sum > info_sum:
            min_sum = info_sum
            target_attr_idx = attr_idx
            children = temp_children
    node.children = children
    node.attr_idx = target_attr_idx
    for child in children:
        child.rest_attr_idx = list(set(node.rest_attr_idx)-set([target_attr_idx,]))
        id3(child)

tree={}
clazz_num=4
attr_num=5

def info_after_divide(node,attr_idx):
    children=[Node(attr_val=i+1) for i in range(5)]
    for index in node.indexes:
        attr_val=train_data[index][attr_idx]
        children[attr_val-1].indexes.append(index)
    sum_info=0.
    for child in children:
        sum_info+=float(len(child.indexes))/float(len(node.indexes))*info(child)

    return sum_info,children

def info(node):
    clazz_dict={}
    for index in node.indexes:
        clazz = train_class[index]
        key = clazz
        if clazz_dict.get(key) is not None:
            clazz_dict[key] += 1
        else:
            clazz_dict[key] = 1
    vals=clazz_dict.values()
    s=float(sum(vals))
    info=0
    for val in vals:
        info += -float(val)/s*log(float(val)/s)
    return info

