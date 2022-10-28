string = input(str())

doi = 'https' + '://' + 'sci-hub.mksa.top/' + string

import webbrowser
webbrowser.open(doi, new = 0, autoraise = True)

