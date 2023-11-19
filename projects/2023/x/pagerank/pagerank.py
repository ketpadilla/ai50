import os
import random
import re
import sys

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

    # Initialize number of pages in corpus
    n = len(corpus)

    # Initialize dictionary for probability distribution
    probability_distribution = { name: 0 for name in corpus }
    
    # If page has no outgoing links, return probability distribution with equal probability for all pages
    if len(corpus[page]) == 0:
        for name in probability_distribution:
            probability_distribution[name] = 1 / n
        return probability_distribution
    
    # Initialize probability of picking a random page
    random_probability = (1 - damping_factor) / n

    # Initialize probability of picking a page linked to by the current page
    linked_probability = damping_factor / len(corpus[page])

    # Add probabilities to probability distribution
    for name in probability_distribution:
        # Add random probability if page has no outgoing links, otherwise add linked probability
        probability_distribution[name] += random_probability if name not in corpus[page] else linked_probability
    
    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Initialize dictionary with page names as keys with initial values of 0
    pages = { name: 0 for name in corpus }

    # Choose the first page at random and increment its value in pages dictionary
    current_page = random.choice(list(pages))
    pages[current_page] += 1

    # Iterate n-1 times to sample picking pages
    for i in range(n - 1):

        # Initialize transition model
        model = transition_model(corpus, current_page, damping_factor)

        # Pick a page at random 
        random_page = random.random()

        # Initialize cumulative probability
        cumulative_probability = 0

        # Iterate through transition model
        for name, probability in model.items():

            # Add probability to cumulative probability
            cumulative_probability += probability

            # If cumulative probability is greater than or equal to random page, pick that page
            if cumulative_probability >= random_page:
                current_page = name
                break

            # Increment page's value in pages dictionary
            pages[current_page] += 1
    
    # Normalize values in pages dictionary
    ranks = { name: (value / n) for name, value in pages.items() }

    # Return ranks
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Initialize number of pages in corpus
    n = len(corpus)
    # Initialize initial ranks
    rank = 1 / n
    # Initialize random probability
    random_probability = (1 - damping_factor) / n

    # Initialize dictionary with page names as keys with initial ranks
    pages = { name: rank for name in corpus }

    # Initialize dictionary for new ranks
    new_pages = { name: 0 for name in corpus }

    # Iterate until convergence
    i = 0; max_rank = rank
    while max_rank > 0.001:
        i += 1; max_rank = 0

        # Iterate through pages
        for name in corpus:
            # Initialize surfer probability
            surfer_probability = 0
            # Iterate through pages that link to current page
            for next_page in corpus:
                # If page has no link, pick a random page
                if len(corpus[next_page]) == 0:
                    surfer_probability += pages[next_page] * rank
                
                # If page links to current page, pick a link at random
                if name in corpus[next_page]:
                    surfer_probability += pages[next_page] / len(corpus[next_page])

            # Calculate new rank
            new_pages[name] = random_probability + (damping_factor * surfer_probability)
        
        # Normalize new ranks
        new_pages = { name: value / sum(new_pages.values()) for name, value in new_pages.items() }

        # Find max change
        for name in corpus:
            # Calculate change
            change = abs(pages[name] - new_pages[name])
            # Update max change
            max_rank = change if change > max_rank else max_rank

        # Update page ranks to new ranks
        pages = new_pages.copy()

    # Return page ranks
    return pages


if __name__ == "__main__":
    main()
