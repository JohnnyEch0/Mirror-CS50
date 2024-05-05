import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    # print("people =    ")
    # for person, values in people.items():
    #     print(person, ":    ",values)

    # print("one gene =    ", two_genes)

    probs = []
    for person in people:

        # people without parents (poor harry)
        if people[person]["mother"] is None or people[person]["father"] is None:
            # likelyhood of genes is prob_1
            if person in one_gene:
                prob_1 = PROBS["gene"][1]
                gene_ev = 1
            elif person in two_genes:
                prob_1 = PROBS["gene"][2]
                gene_ev = 2
            else:
                prob_1 = PROBS["gene"][0]
                gene_ev = 0

            # likelihood of trait is prob_2
            if person in have_trait:
                prob2 = PROBS["trait"][gene_ev][True]
            else:
                prob2 = PROBS["trait"][gene_ev][False]

            # print(f"Probs for {person}:   gene: {prob_1}   trait: {prob2}, joined: {prob_1*prob2}")

            person_joined_prob = prob_1 * prob2
            probs.append(person_joined_prob)
        #  people with parents
        else:

            mother = people[person]["mother"]
            father = people[person]["father"]
            parents = {mother, father}
            parent_probs = []
            parent_not_probs = []

            for parent in parents:
                if parent in one_gene:
                    gene_from_p = 0.5
                elif parent in two_genes:
                    gene_from_p = 1 - PROBS["mutation"]
                else:
                    gene_from_p = 0 + PROBS["mutation"]
                parent_probs.append(gene_from_p)
                parent_not_probs.append(1 - gene_from_p)

            # gene_prob for child
            if person in two_genes:
                gene_prob = parent_probs[0] * parent_probs[1]
                gene_ev = 2
            elif person in one_gene:
                gene_prob = parent_probs[0] * parent_not_probs[1] +
                parent_probs[1] * parent_not_probs[0]
                gene_ev = 1
            else:
                gene_prob = parent_not_probs[0] * parent_not_probs[1]
                gene_ev = 0

            # trait prob for child
            if person in have_trait:
                prob2 = PROBS["trait"][gene_ev][True]
            else:
                prob2 = PROBS["trait"][gene_ev][False]

            person_joined_prob = gene_prob * prob2

            probs.append(person_joined_prob)

    final_prob = 1
    for prob in probs:
        # print(prob)
        final_prob = final_prob * prob

    # print(f"final prob: {final_prob}")
    # sys.exit("in dev.")
    return final_prob










    sys.exit("In dev.")


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # print(probabilities)
    for person in probabilities:
        # print(person)

        # genes
        if person in two_genes:
            probabilities[person]["gene"][2] += p
        elif person in one_gene:
            probabilities[person]["gene"][1] += p
        else:
            probabilities[person]["gene"][0] += p

        # trait
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p



def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # genes
        gene_prob_sum = probabilities[person]["gene"][2] + probabilities[person]["gene"][1] + probabilities[person]["gene"][0]
        if  gene_prob_sum != 1:
            multiplier = 1 / gene_prob_sum

        probabilities[person]["gene"][0] *= multiplier
        probabilities[person]["gene"][1] *= multiplier
        probabilities[person]["gene"][2] *= multiplier

        trait_prob_sum = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        if trait_prob_sum != 1:
            multiplier = 1 / trait_prob_sum

        probabilities[person]["trait"][True] *= multiplier
        probabilities[person]["trait"][False] *= multiplier



if __name__ == "__main__":
    main()
