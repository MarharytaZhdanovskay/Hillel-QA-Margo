# norway_text1 = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')

# norway_text2 = 'Automatisering akselererer {}syeblikket da roboter vil erobre planeten v{}sr. ({})'.format('ø', 'å', 'Æ')

# token1 = 'ø'
# token2 = 'å'
# token3 = 'Æ'
# norway_text3 = f'Automatisering akselererer {token1}syeblikket da roboter vil erobre planeten v{token2}sr. ({token3})'


norway_text = ('Automatisering akselererer %syeblikket da roboter vil'
               ' erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ'))

print(norway_text)

norway_text2 = ('Automatisering akselererer {0}yeblikket da roboter vil'
                ' erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ'))

print(norway_text2)

norway_text3 = (f'Automatisering akselererer {"ø"}yeblikket da roboter'
                f' vil erobre planeten v{"å"}r. ({"Æ"})')

print(norway_text3)
