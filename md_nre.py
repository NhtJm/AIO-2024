# Function of Mean Difference of n-th Root Error.
def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference**p
    print(loss)
    return

md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1) #>> 0.025031328369998107
md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1) #>> 0.03544417213033135
md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1) #>> 0.05625552183565574
md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1) #>> 0.45836890322464546