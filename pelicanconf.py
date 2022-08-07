AUTHOR = 'Melek Gharbi'
SITENAME = "Melek Gharbi's blog - Growth Hacker & tech enthusiast blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Custom variables
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (
         ('Bakchich, the Crowdfunding platform for Tunisian and African creators', 'https://ba9chich.com'),
         ('The Growth Hacking agency i work in', 'http://art-guru.tech/'),
         ('Cold Mail Agency, our cold mailing tool', 'https://coldmail.agency/'),
            )

# Social widget
SOCIAL = (('Github', 'https://github.com/manfromtunis'),
          ('Linkedin', 'https://www.linkedin.com/in/melek-gharbi/'),
          ('Instagram', 'https://www.instagram.com/ghmelek/')
            )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = './venv/lib/python3.8/site-packages/pelican/themes/attila'
HOME_COVER = 'https://geekyshacklebolt.github.io/blog/images/my-blog-header-bg.jpg'

