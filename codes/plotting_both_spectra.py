import numpy as np
import matplotlib.pyplot as plt

l = np.array([6.250000000000000130e-04,
8.750000000000000182e-04,
1.124999999999999915e-03,
1.375000000000000137e-03,
1.624999999999999925e-03,
1.874999999999999714e-03])

amp = [5.554523012221631584e-01,
5.636435036947111676e-01,
1.379988600334177251e+00,
8.981623381691389296e-01,
2.538647574140815433e-01,
5.921284628998201294e-01]

amp_err = [1.771586611357615637e-01,
2.901468598047071690e-01,
4.782266397860808760e-01,
3.415021510926868897e-01,
1.691802574194539721e-01,
1.614078918592695699e-01]

amp_cross = [5.138539150089826979e-01,
4.314509039231070875e-01,
4.594740613120302797e-01,
5.152880832726842719e-01,
4.067705002602710063e-01,
5.256260551260376612e-01]

amp_err_cross = [1.379859362628176322e-01,
1.835695870136887231e-01,
2.028135282065127165e-01,
1.102815953134217569e-01,
1.391126400779626460e-01,
1.554547732708690677e-01]

plt.figure(dpi=600)
#plt.plot(lambdas_inv, amp, 'r.', label='Amplitude of power spectrum')
plt.plot(l+0.00001, amp, 'r.', label='Auto power spectrum')
plt.errorbar(l+0.00001,amp, yerr=amp_err, fmt='r.',ecolor='black',elinewidth=1,
            capsize = 4)

plt.plot(l, amp_cross, 'b.', label='Cross power spectrum')
plt.errorbar(l,amp_cross, yerr=amp_err_cross, fmt='b.',ecolor='black',elinewidth=1,
            capsize = 4)
# plt.plot(lambdas_inv_curve, curve, 'b', 
#          label='Best fit: Power law (power = %1.2f)'%p_fit)
plt.xlabel("$1/\lambda$ ($kpc^{-1}$)")
plt.ylabel("Amplitude of power spectrum")
plt.legend()
plt.title("Power Spectrum of normalised map")
#plt.savefig("../images/power_spectrum.png", dpi = 400)
plt.show()