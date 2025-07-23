import webbrowser
to_search = ["Brooklyn College", "Baruch College", "Hunter College", "Pizza",
"Barclays Center"]
for item in to_search:
    webbrowser.open("http://www.google.com/search?btnG=1&q=%s' % item")

