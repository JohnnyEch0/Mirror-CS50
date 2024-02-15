import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        # print(sys.argv)
        print("Usage: (csvfile), (DNA-Sequence)")
        return 1

    # TODO: Read database file into a variable
    try:
        with open(sys.argv[1]) as csv_file:
            reader = csv.DictReader(csv_file)

    except:
        print("Couldn't open CSV file")

    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # syntax reminder
    # for r in rows:
    #     print(r["name"], r["AGATC"])


    # TODO: Read DNA sequence file into a variable
    try:
        with open(sys.argv[2]) as dna_file:
            dna_string = dna_file.read()
            # print(dna_string)

    except:
        print("Couldn't open DNA file")


    # TODO: Find longest match of each STR in DNA sequence
    load_str = rows[0].keys()
    len_str = len(load_str)

    print(load_str[1])
    # for i, c in enumerate(rows):
        # print(c)

    # might be garbage
    for r in rows: # [1:-1]
        print(r["name"])

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
