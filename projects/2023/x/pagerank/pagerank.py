import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    """ Main function to run pagerank algorithm """
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

    If a page has no outgoing links, returns an equal probability for all pages in the corpus
    """

    n = len(corpus) # num of pages in corpus
    p_dist = { name: 0 for name in corpus } # dict for probability distribution
    rand_p = (1 - damping_factor) / n # prob for picking a random page
    linked_p = damping_factor / len(corpus[page]) # prob for picking a linked page
    
    if len(corpus[page]) == 0: # if no outgoing links
        for name in p_dist: # for each page in corpus
            p_dist[name] = 1 / n # <- equal prob
        return p_dist
    
    for name in p_dist: 
        p_dist[name] += rand_p if name not in corpus[page] else linked_p # add rand_p if no outgoing links, else add linked_p
    return p_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pg_visits = {page_name: 0 for page_name in corpus} # dict for page visits
    curr_page = random.choice(list(pg_visits)) # pick random page from corpus
    pg_visits[curr_page] += 1 # increment page visit count

    for i in range(n-1): # for the remaining n-1 samples

        model = transition_model(corpus, curr_page, damping_factor) # init transition model
        rand_p = random.random() # init random probability
        cml_p = 0 # init cumulative probability

        for page_name, probability in model.items(): # for each page in transition model 
            cml_p += probability 
            if rand_p <= cml_p: 
                # if rand prob is less than or equal to cumulative prob, pick that page
                curr_page = page_name
                break

        pg_visits[curr_page] += 1

    ranks = {page_name: (value/n) for page_name, value in pg_visits.items()} # normalise page visits to get page ranks
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    n = len(corpus) # num of pages in corpus
    rank = 1 / n # initial ranks
    rand_p = (1 - damping_factor) / n # prob for picking a random page
    pages = { name: rank for name in corpus } # dict for page ranks
    new_ranks = { name: 0 for name in corpus } # dict for new page ranks

    i = 0; max_change = rank # init iteration and max change
    while max_change > 0.001: # while max change is greater than 0.001
        i += 1; max_change = 0

        for name in corpus: # for each page in corpus
            surf_p = 0 #
            for next_page in corpus: # for each link in page
                if len(corpus[next_page]) == 0: # if page has no outgoing links
                    surf_p += pages[next_page] * rank
                
                if name in corpus[next_page]: # if page links to current page
                    surf_p += pages[next_page] / len(corpus[next_page])

            new_ranks[name] = rand_p + (damping_factor * surf_p) # new rank 
        
        new_ranks = { name: value / sum(new_ranks.values()) for name, value in new_ranks.items() } # normalise new ranks

        for name in corpus: # for each page in corpus
            change = abs(pages[name] - new_ranks[name]) # calculate max change
            max_change = change if change > max_change else max_change # update max change

        pages = new_ranks.copy() # copy new ranks to pages
    return pages


if __name__ == "__main__":
    main()