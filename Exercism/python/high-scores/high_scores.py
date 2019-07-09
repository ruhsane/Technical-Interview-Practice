def latest(scores):
    last_index = len(scores) - 1
    return scores[last_index]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    descend_scores = sorted(scores, reverse=True)
    return descend_scores[:3]
