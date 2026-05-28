family = {"child1":{'name':'kk','year':2009},'child2':{'name':'ll','year':1213}}
family['branch']='kalaignar'
print(family)
for x in family:
    print(x,family[x])
print(family['child1']['name'])
print(family['child1'].keys())
print(family.get('branchs','not'))
family.pop('child1')
print(family)


