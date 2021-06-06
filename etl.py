def transform(legacy_data):
    #flattening a dictionary consisting of lists
    res = {values.lower(): k for k, v in legacy_data.items() for values in v}
    #sorting values by key in dictionary
    return ({key: res[key] for key in sorted(res.keys())})
