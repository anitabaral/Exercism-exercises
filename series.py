

def slices(series, length):
    if length <= 0 or len(series) == 0 or length>len(series):
        raise ValueError("value_error")

    final_series = []
    for i, value in enumerate(series):
        segments = ""
        if (len(series) - i) >= length:
            for j in range(length):
                segments += series[j+i]
            final_series.append(segments)
    return final_series
