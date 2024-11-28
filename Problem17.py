'''17. Compute Accuracy, Error rate, Precision, Recall for following confusion
matrix ( Use formula for each)

True Positives (TPs): 1 False Positives (FPs): 1
False Negatives (FNs): 8 True Negatives (TNs): 90'''


TP = 1
FP = 1
FN = 8
TN = 90

accuracy = (TP+TN) / (TP+FP+FN+TN)

error_rate = (FP+FN) / (TP+FP+FN+TN)

precision = TP / (TP+FP)

recall = TP / (TP+FN)

print(f"Accuracy: {accuracy}")
print(f"Error Rate: {error_rate}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
