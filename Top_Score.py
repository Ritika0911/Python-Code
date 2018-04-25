def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in xrange(len(score_counts)-1, -1, -1):
        count = score_counts[score]

        for time in xrange(count):
            sorted_scores.append(score)

    return sorted_scores

if __name__ == '__main__':
    unsorted_scores = [100, 37, 89, 41, 65, 65, 65, 91, 53]
    highest_possible_score = 100
    print sort_scores(unsorted_scores, highest_possible_score)
