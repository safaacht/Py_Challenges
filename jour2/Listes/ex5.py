#  Trier et organiser les données

scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]
# print(scores)

scores_copie = scores.copy()
# print(scores_copie)

scores.sort()
print(scores)

scores_copie.sort(reverse='True')
print(scores_copie, "\nLes meilleurs scores sont: ", scores_copie[:3])
