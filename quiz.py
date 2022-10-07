print('Willkommen zum Python Quiz')
answer = input('Kanns losgehen ? (ja/nein) :')
score = 0
total_questions = 2

if answer.lower() == 'ja':
    answer = input('Frage 1: Welches Videospiel spielst du am liebsten?')
    if answer.lower() == 'lol' or answer.lower() == 'league of legends':
        score += 1
        print('Richtig!')
    else:
        print(f'Macht {answer} wirklich Spaß?')

    answer = input('Frage 2: Wo sind wir heute? ')
    if answer.lower() == 'Code Design Camp'.lower():
        score += 1
        print('Richtig!')
    else:
        print('Falsche Antwort :(')

print(f'Danke fürs mitspielen! du hast {score} von {total_questions} Fragen richtig beantwortet!')
print('Ciao!')
