import random
import webbrowser

websites = ["google.com", "facebook.com", "twitter.com", "stackoverflow.com"]

website = random.choice(websites)

webbrowser.open_new_tab("http://" + website)
