# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from algorithm.id3 import id3_main


def id3_page(request):
    root=id3_main()
    nodes=[]
    links=[]#source,relation,target
    nodes.append(root)
    travel_tree(root,0,nodes,links)
    context={'nodes':nodes,'links':links}
    return render(request,'website/id3.html',context)

def travel_tree(node,node_index,nodes,links):
    if len(node.indexes) == 0:return
    # print node.indexes
    # print node.rest_attrs
    # print {'source':node_index,'relation':node.attr,'target':len(nodes)-1}
    if len(node.children) > 0:
        for child in node.children:
            if len(child.indexes) == 0:continue
            nodes.append(child)
            links.append({'source': node_index, 'relation': "%s-%s"%(node.attr_idx,child.attr_val), 'target': len(nodes) - 1})
            travel_tree(child,len(nodes) - 1,nodes,links)