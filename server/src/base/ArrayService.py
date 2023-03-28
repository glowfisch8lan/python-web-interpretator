import json, re


def build_job(file):

    def branch(tree, vector, value):

        # Originally based on https://stackoverflow.com/a/47276490/2903486

        # Convert Boolean
        if isinstance(value, str):
            value = value.strip()

            if value.lower() in ['true', 'false']:
                value = True if value.lower() == "true" else False

        # Convert JSON
        try:
            value = json.loads(value)
        except:
            pass

        key = vector[0]
        arr = re.search('\[([0-9]+)\]', key)

        if arr:

            # Get the index of the array, and remove it from the key name
            arr = arr.group(0)
            key = key.replace(arr, '')
            arr = int(arr.replace('[', '').replace(']', ''))

            if key not in tree:

                # If we dont have an array already, turn the dict from the previous
                # recursion into an array and append to it
                tree[key] = []
                tree[key].append(value \
                                     if len(vector) == 1 \
                                     else branch({} if key in tree else {},
                                                 vector[1:],
                                                 value))
            else:

                # Check to see if we are inside of an existing array here
                isInArray = False
                for i in range(len(tree[key])):
                    if tree[key][i].get(vector[1:][0], False):
                        isInArray = tree[key][i][vector[1:][0]]

                if isInArray and arr < len(tree[key]) \
                        and isinstance(tree[key][arr], list):
                    # Respond accordingly by appending or updating the value
                    tree[key][arr].append(value \
                                              if len(vector) == 1 \
                                              else branch(tree[key] if key in tree else {},
                                                          vector[1:],
                                                          value))
                else:
                    # Make sure we have an index to attach the requested array to
                    while arr >= len(tree[key]):
                        tree[key].append({})

                    # update the existing array with a dict
                    tree[key][arr].update(value \
                                              if len(vector) == 1 \
                                              else branch(tree[key][arr] if key in tree else {},
                                                          vector[1:],
                                                          value))

            # Turn comma deliminated values to lists
            if len(vector) == 1 and len(tree[key]) == 1:
                tree[key] = value.split(",")
        else:
            # Add dictionaries together
            tree.update({key: value \
                if len(vector) == 1 \
                else branch(tree[key] if key in tree else {},
                            vector[1:],
                            value)})
        return tree

    # file = [{
    #     "one.array[0].dict.dont-worry-about-me.se": "se",
    #     "one.array[0].dict.dont-worry-about-me.sse": "se",
    #     "one.array[0].dict.arrOne[0]": "1,2,3",
    #     "one.array[0].dict.arrTwo[1]": "4,5,6",
    #     "one.array[1].x.y[0].z[0].id": "789"
    # }]

    rowList = []
    for row in file:
        rowObj = {}
        for colName, rowValue in row.items():
            rowObj.update(branch(rowObj, colName.split("."), rowValue))
        rowList.append(rowObj)
    return rowList



