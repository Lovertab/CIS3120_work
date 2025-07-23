import webbrowser

google = input('Enter a valuse to search via Google Maps:')

webbrowser.open("http://www.google.com/maps?btnG=1&q=%s' % google")