import pickle

import matplotlib.pyplot as plt

import ib_naming_model
from tools import *

LOGGER = get_logger('main')


def main():
    # Load model. Leave blank for a default model, or pass in a path to a custom model as done here.
    model = ib_naming_model.load_model('models/IB_color_naming_model/unif_model.pkl')
    curve = model.IB_curve

    with open('data/pw_m', 'rb') as file:
        pw_m = pickle.load(file)
    eps, gnid, bl, qw_m_fit = model.fit(pw_m)
    acc = model.accuracy(pw_m)
    comp = model.complexity(pw_m)
    print("Acc", acc)
    print("Comp", comp)

    # Plot the theoretical bound and the actual point
    plt.figure()
    plt.plot(curve[0], curve[1])
    plt.xlabel('complexity, $I(M;W)$')
    plt.ylabel('accuracy, $I(W;U)$')
    plt.scatter(comp, acc)  # The actual point that was recorded.
    plt.xlim([0, H(model.pM)])
    plt.ylim([0, model.I_MU + 0.1])
    plt.show()

    # let's plot a mode map!
    qW_M = qw_m_fit
    plt.figure(figsize=(6.4, 2.5))
    model.mode_map(qW_M)
    plt.title('Optimal IB system for $\\beta = %.3f$' % bl)
    plt.tight_layout()
    plt.show()
    print(model.complexity(qW_M), model.accuracy(qW_M))


if __name__ == '__main__':
    main()
