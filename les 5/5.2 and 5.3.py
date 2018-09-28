leeftijd =eval (input('uw leeftijd is?: '))
paspoort = input('heeft u een nederlands paspoort. voer in ja/nee: ')


if leeftijd > 17 and paspoort == 'ja':
    print('gefeliciteerd je mag stemmen')
else:
    print('sorry, maar u mag nog niet stemmen')
