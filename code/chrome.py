#!/usr/bin/env python3

# chrome - Chrome (or other web browser) Terminal Launcher
# /w automatic search format functionality

# Written by Justus Languell
# <gtsbr.org> 
# <jus@gtsbr.org>
# <@justus.l_>

import os
import sys
import urllib.parse
from clint.textui import colored


def _help():

    print('''

    ─────────────────────
    ───────────████████──
    ──────────███▄███████
    ──────────███████████
    ──────────███████████
    ──────────██████─────
    ──────────█████████──
    █───────███████──────
    ██────████████████───
    ███──██████████──█───
    ███████████████──────
    ███████████████──────
    ─█████████████───────
    ──███████████────────
    ────████████─────────
    ─────███──██─────────
    ─────██────█─────────
    ─────█─────█─────────
    ─────██────██────────
    ─────────────────────

    Chrome Terminal Launcher Args

    Url:
    google.org
    www.google.org
    https://www.google.org

    Search:
    -s how does google search work
    --search stack overflow

    ~ Recomendations
    alias "google" or "alias" -> "chrome -s"

    (c) Justus Languell 2021 <jus@gtsbr.org> <@justus.l_>
    ''')


def _filter(url):

    return urllib.parse.quote_plus(url)


def search(argv,argc):

    error = False
    args = 'https://www.google.com/search?q='

    if len(sys.argv) > 2:

        query = False

        for arg in argv:

            if query:
                args += (_filter(arg) + '+')

            if arg == argc:
                query = True
            
    else:

        error = True

        print(colored.red('Error'))
        print('-s or --search Search arg requires valid query!')

    return args[:-1], error


def main():
    
    error = False

    if len(sys.argv) < 2:

        print(colored.red('Error'))
        print('Invalid args: -h or --help for help')

        error = True

    else:

        program = '/applications/Google\\ Chrome.app/contents/macos/Google\\ Chrome'

        path = 'www.google.com'

        if ('-h' in sys.argv) or ('--help' in sys.argv):
            error = True
            _help()

        elif '-s' in sys.argv:
            args, error = search(sys.argv,'-s')

        elif '--search' in sys.argv:
            args, error = search(sys.argv,'--search')

        else:
            args = sys.argv[1] 

            args = args.replace('http://','')
            args = args.replace('https://','')

            if args.split('/')[0].count('.') == 1:
                args = 'www.' + args
        
        if not error:

            kill = '' 

            if not ('-v' in sys.argv):
            
                kill = ' > /dev/null 2>&1' 

            else:
                print(f'Opening {args} in Chrome') 

            os.system(program + ' ' + args + kill)
            print(colored.green('Success'))


if __name__ == '__main__':
    main()



