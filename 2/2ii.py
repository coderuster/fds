import numpy as np
from scipy import stats

# Test scores
scores = np.array([85, 90, 75, 85, 100, 90, 85, 80])

mean_score = np.mean(scores)

median_score = np.median(scores)

mode_score = stats.mode(scores, keepdims=True)[0][0]

print("Mean:", mean_score)
print("Median:", median_score)
print("Mode:", mode_score)