import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: (csvfile), (DNA-Sequence)")
        return 1

    # TODO: Read database file into a variable
    try:
        with open(sys.argv[1]) as csv_file:
            reader = csv.DictReader(csv_file)

    except:
        print("Couldn't open CSV file")

    # split rows and save them in an array
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)


    # TODO: Read DNA sequence file into a variable
    try:
        with open(sys.argv[2]) as dna_file:
            dna_string = dna_file.read()

    except:
        print("Couldn't open DNA file")


    # TODO: Find longest match of each STR in DNA sequence

    # isolate the first line of the csv for matches
    load_first_row = rows[0].keys()

    # get larges matches and str's
    str, long_matches = get_str_largest_matches(load_first_row, dna_string)


    # TODO: Check database for matching profiles

    # input rows, str's and longest matches
    # the function handles final printing.
    get_match(rows, str, long_matches)






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

def get_str_largest_matches(strs, dna):
    # takes a list of the first line of the csv strs and the dna
    # returns a list of strs and one of longest matches
    str = []
    long_matches = []
    for key in strs:
        if key == "name":
            continue
        else:
            str.append(key)
            lon_match = longest_match(dna, key)
            long_matches.append(lon_match)
    return str, long_matches


def get_match(rows, str, long_matches):
    for _, row in enumerate(rows):
        matches = 0
        for j, _str in enumerate(str):
            # for each str, if long_matches[j] matches
            if long_matches[j] != int(row[_str]):
                # when a longest match is unequal to a persons longest match, skip this j
                continue
            else:
                # count
                matches +=1
        # if all match, print name and stop function
        if matches == len(str):
                print(row["name"])
                return

    # else print No Match
    print("No Match")
    return

main()
