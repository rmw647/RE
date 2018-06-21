import numpy as np
from kmodes.kprototypes import KPrototypes

#stock_file = '/Users/rebeccaward/Documents/professional/Levinson-consulting/toy-data/stocks.csv'
prop_file = '/Users/rebeccaward/Documents/professional/Levinson-consulting/toy-data/syn_prop_data.csv'
# stocks with their market caps, sectors and countries
# list of symbols
syms = np.genfromtxt(prop_file,dtype=str, delimiter=',',skip_header=1)[:,0]
print(syms)

# the rest of the data
X = np.genfromtxt(prop_file, dtype=object, delimiter=',',skip_header=1,usecols=(0,1,2,3))[:, 1:]

#make numeric data floats
X[:, 1] = X[:, 1].astype(float)
print(X)

# kproto = KPrototypes(n_clusters=3, init='Cao', verbose=2)
# clusters = kproto.fit_predict(X, categorical=[1, 2])
#
# # Print cluster centroids of the trained model.
# print(kproto.cluster_centroids_)
# # Print training statistics
# print(kproto.cost_)
# print(kproto.n_iter_)
#
# for s, c in zip(syms, clusters):
#     print("Symbol: {}, cluster:{}".format(s, c))
