# add x into header
def addDict(dictin, item, docID):
    i = dictin.find(item)
    if i != -1:  # item found
        j = dictin[item].find(docID)
        if j != -1: # docID found
            dictin[item][j] += [docID];
            return dictin

    new_dict = {item, docID}
    dictin = dict(dictin.item() + new_dict.item())
    return dictin