import hdbscan
import pandas as pd
from matplotlib import pyplot as plt

from popcorn.popcorn import popcorn

X = pd.read_csv('./datasets/Xobs.csv')
Xsd = pd.read_csv('./datasets/Xsd.csv')

# Plot the distribution of original data
plt.scatter('V1', 'V2', s=10, data=X)
plt.title('Original data')
plt.xlim((-0.4, 0.4))
plt.ylim((-0.3, 0.3))
plt.show()

# run the POPCORN
U, S, V = popcorn(X, Xsd, 2)
result = U @ S @ V.T
result = pd.DataFrame(result)
column = []
for i in range(1, 21):
    column.append("V" + str(i))
result.columns = column

# Plot the distribution of denoised data
plt.scatter('V1', 'V2', s=10, data=result)
plt.title('Denoised data')
plt.xlim((-0.4, 0.4))
plt.ylim((-0.3, 0.3))
plt.show()

# Use the HDBScan to do the classification on the original data
clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=True)
clusterer.fit(X[['V1', 'V2']])
X['label'] = clusterer.labels_
X['proab'] = clusterer.probabilities_
X.loc[X['proab'] < 0.5, 'label'] = -1
plt.xlabel('V1', fontsize=12)
plt.ylabel('V2', fontsize=12)
plt.title('Classification on nosy data')
plt.scatter('V1', 'V2', c=X['label'], s=10, cmap='plasma', data=X)
plt.xlim((-0.4, 0.4))
plt.ylim((-0.3, 0.3))
plt.show()

# # Use the HDBScan to do the classification on the denoised data
clusterer2 = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=True)
clusterer2.fit(result[['V1', 'V2']])
result['label'] = clusterer2.labels_
result['proab'] = clusterer2.probabilities_
result.loc[result['proab'] < 0.5, 'label'] = -1
plt.xlabel('V1', fontsize=12)
plt.ylabel('V2', fontsize=12)
plt.title('Classify on denoised data')
plt.scatter('V1', 'V2', c=result['label'], s=10, cmap='plasma', data=result)
plt.xlim((-0.4, 0.4))
plt.ylim((-0.3, 0.3))
plt.show()
