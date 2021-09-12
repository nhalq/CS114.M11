import re
print('.' + '.'.join(re.sub('[aoyeui]', '', input().lower())))
