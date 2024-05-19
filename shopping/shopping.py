import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    months = {
        "January": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    }

    value_dict = {
        0: int,
        1: float,
        2: int,
        3: float,
        4: int,
        5: float,
        6: float,
        7: float,
        8: float,
        9: float,
        10: months,
        11: int,
        12: int,
        13: int,
        14: int,
        15: int,
        16: int
    }
    evidence = []
    labels = []
    with open(filename, "r") as file:

        reader = csv.reader(file)
        header = next(reader, None)  # skip header
        # print(header)
        for line in reader:
            evidence_line = []
            for i in range(17):
                if i == 10:
                    ev = months[line[i]]

                elif i == 15:
                    if line[i] == "Returning_Visitor":
                        ev = 1
                    else:
                        ev = 0

                elif i == 16:
                    if line[i] == "TRUE":
                        ev = 1
                    else:
                        ev = 0

                else:
                    ev = value_dict[i](line[i])

                evidence_line.append(ev)
            if line[17] == "TRUE":
                lab = 1
            elif line[17] == "FALSE":
                lab = 0
            else:
                raise ValueError("Line[17] is not TRUE or FALSE")
            labels.append(lab)

            evidence.append(evidence_line)

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    nn = KNeighborsClassifier(n_neighbors=1)
    nn.fit(evidence, labels)

    return nn


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positives = 0
    negatives = 0

    pos_predictions = 0
    neg_preditions = 0

    for i, label in enumerate(labels):
        # positives
        if label == 1:
            positives += 1
            if predictions[i] == 1:
                pos_predictions += 1
        # negatives
        elif label == 0:
            negatives += 1
            if predictions[i] == 0:
                neg_preditions += 1

    sensitivity = pos_predictions/positives
    specificity = neg_preditions/negatives

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
