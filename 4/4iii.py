import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

math_scores = np.array([88, 76, 95, 67, 89, 82])
science_scores = np.array([92, 80, 85, 70, 90, 75])
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']

plt.scatter(math_scores, science_scores)

for i, student in enumerate(students):
    plt.text(math_scores[i], science_scores[i], student)

plt.xlabel('Math Scores')
plt.ylabel('Science Scores')
plt.title('Math vs Science Scores')
plt.savefig('math_science_relationship.png')
# plt.show()
