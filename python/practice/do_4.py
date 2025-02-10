def count_bull_eye(scores):
    count = 0
    for number in scores:
        if number == 50:
            count += 1
    return count


scores = [1, 24, 50, 50, 34]
count_bull_eye(scores)
