# Read Reddit in Terminal

A clean fun way to read [Reddit](https://reddit.com) in your terminal


Usage:

    python3 get_reddit_page.py modernwarfareii 'sniper' | less


New version of the program using 'requests' and argparse':

    python3 subreddit.py -h

(.venv) choi@paris ~/p/reddit-lite (main)$ python3 subreddit.py -h

    usage: subreddit.py [-h] subreddit search_query

    Search a subreddit

    positional arguments:
      subreddit     Subreddit name
      search_query  Search query

    options:
      -h, --help    show this help message and exit


    # do search
    python3 subreddit.py modernwarfareii 'sniper' | less

## TODO

- add a TUI library interface for interaction

