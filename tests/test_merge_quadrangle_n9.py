import numpy as np


def test_lanms():
    from lanms import merge_quadrangle_n9 as la_nms
    q_in = np.random.uniform(0, 1.0, [16, 9])
    thr = 0.5
    q_out = la_nms(q_in)
    print(q_out)


if __name__ == '__main__':
    test_lanms()
