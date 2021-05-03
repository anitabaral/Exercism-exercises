def latest(scores):
    scores.sort(reverse = True)
    return scores[0]


def personal_best(scores):
    return scores[-1]


def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[:3]
