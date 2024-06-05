# Function to calculate the F1-Score
def f1_score(tp, fp, fn):
    # check whether tp, fp, fn are legitimate
    if not isinstance(tp, int):
        print("tp must be integers")
        return None
    if not isinstance(fp, int):
        print("fp must be integers")
        return None
    if not isinstance(fn, int):
        print("fn must be integers")
        return None
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, fn must be greater than zero")
        return None

    # calculate precision, recall and F1-Score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Precision is", precision)
    print("Recall is", recall)
    print("F1-Score is", f1_score)


# Test the function
f1_score(tp=2, fp=3, fn=4)
f1_score(tp="a", fp=3, fn=4)
f1_score(tp=2, fp="a", fn=4)
f1_score(tp=2, fp=3, fn="a")
f1_score(tp=2, fp=3, fn=0)
f1_score(tp=2.1, fp=3, fn=0)