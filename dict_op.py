# add x into header
def addDict(dictin, item, docID):
    if item in dictin:  # item found
        if docID not in dictin[item]:
            dictin[item] += [docID]
        return dictin

    new_dict = {item: [docID]}
    dictin.update(new_dict)  # = dict(dictin.items() + new_dict.items())
    return dictin
