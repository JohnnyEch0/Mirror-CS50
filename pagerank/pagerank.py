import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = dict()

    # damping
    damp_prob = (1-damping_factor) / len(list(corpus))

    for site in list(corpus):
        prob = damp_prob

        try:
            if site in corpus[page]:
                # if the site is linked to, distribute damp factor across all
                prob += damping_factor / len(corpus[page])
        except TypeError:
            raise TypeError("unhashable Type", f"{corpus} indexed {page}")

        distribution.update({f"{site}": round(prob, 15)})


    # catching pages with no links.
    if corpus[page] == set():
        for site in list(corpus):
            prob = 1 / len(list(corpus))
            distribution[site] = prob


    """
    Debugging
    """
    total = 0
    for key, item in distribution.items():
        total += item


    if total > 1.001 or total < 0.999:

        print(f"DEBUG: Trans_Model:{page} --> {distribution}")
        raise ValueError("trans_model Error, total Values dont Sum.")


    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = dict()
    for page in list(corpus):
        page_rank.update({page: 0})

    """
    TODO: Make A dictionary of the TRANS_Model returns, in order not to recalc that every time.
    """


    sample0 = random.choice(list(corpus))
    page_rank[sample0] += 1

    for _ in range(n-1):

        model = transition_model(corpus, sample0, damping_factor)
        pages = []
        weights = []

        for key, value in model.items():
            pages.append(key)
            weights.append(value)

        # print(pages, weights)
        sample0 = random.choices(pages, weights)[0]

        if sample0 in page_rank:
            page_rank[sample0] += 1
        else:
            raise ValueError("Sample not in Pages")

    total_ranks = 0
    for page_ in page_rank:
        page_rank[page_] = page_rank[page_] / n
        total_ranks += page_rank[page_]

    """
    Debugging
    """

    if total_ranks > 1.001 or total_ranks < 0.999:

        print(f"DEBUG: Sample_Pagerank: --> {page_rank}")
        raise ValueError("Sample-Pagerank, total Values dont Sum.")


    return page_rank





def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages_count = len(list(corpus))
    # starting rank is 1/n, where n is the page count
    ranking = dict()
    all_pages = set()
    for site in list(corpus):
        ranking.update({site: 1/pages_count})
        all_pages.add(site)


    # a page that has no links at all, shall be treated as having links to all pages

    for key, value in corpus.items():
        if value == set():
            corpus[key] = all_pages


    # this dictionary will have a key for each site, and a set as a dict which holds every page that links to the key
    linked_by = dict()

    for site in list(corpus):
        # for every page, get the pages that have a link to it.
        linked_by_set = set()

        for site_, links in corpus.items():
            if site in links:
                linked_by_set.add(site_)

        linked_by.update({site: linked_by_set})

    # print("DEBUG CORPUS:   ", corpus)


    # print(f" Page, gets linked by :  {linked_by}")

    # update the ranking for each site in the corpus
    # for every site that links to that page
        # take it's ranking and divide through its N of links
    # measure change

    while True:
        old_values = copy.deepcopy(ranking)
        damping_value = (1 - damping_factor) / pages_count



        for site in list(corpus):
            non_damp = 0
            linked_by_set = linked_by[site]

            for site_links in linked_by_set:
                value_for_lin = old_values[site_links] / len(corpus[site_links])
                non_damp +=  value_for_lin # / len(linked_by[site])
                # print(f"Non_damp Value for {site} for linked by {site_links}:    +=  {old_values[site_links]}  / {len(corpus[site_links])} /  {len(linked_by[site])}")




            # print(f"nu Value for {site} =   ", damping_value, "+  ", f"( {non_damp} * {damping_factor} / {len(linked_by[site])})")
            try:
                nu_value = damping_value + non_damp * damping_factor  # / len(linked_by[site])
            except ZeroDivisionError:
                raise ValueError(f" site: {site}, len linked by was 0, {linked_by[site]}")
            ranking[site] = nu_value

        # print("DEBUG: OLD/NEW RANKIKNG", old_values, "----", ranking)

        # check if the values converged

        process_finished = 0

        for page, rank in ranking.items():
            value_change = rank - old_values[page]
            if rank > 1:
                raise ValueError("Pagerank exceedet 1")
            if value_change < 0.001 and value_change > -0.001:
                process_finished += 1

        if process_finished == len(list(corpus)):
            total = 0
            for key, value in ranking.items():
                total += value
                # print(key, value)
            # print(total)

            if not total < 1.01 or not total > 0.99:
                # raise ValueError(f"total doesnt add up to 1, it is {total}")
                nutotal = 0
                for key, value in ranking.items():
                    ranking[key] /= total
                    nutotal += ranking[key]

                    # print(key, value)

                # print(nutotal)


            return ranking





if __name__ == "__main__":
    main()
