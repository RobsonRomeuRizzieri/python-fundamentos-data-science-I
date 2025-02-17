
# Use an import statement at the top
word_file = "flying_circus_cast.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip()        				
		word_list.append(word)


def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list     
    for item in word_list:
        temp = item.split(',')
        cast_list.append(temp[0])

    return cast_list

print(create_cast_list(word_file))

#Segunda alternatica para fazer a leitura do arquivo
def create_cast_list(filename):
    cast_list = []
    # usar with para abrir o arquivo filename
    with open(filename) as f:
    # use a sintaxe do laço for para processar cada linha
    # e adicione o nome do ator a cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list

=================================================================================
#informações do arquivo txt
Graham Chapman,  Various / ... (46 episodes, 1969-1974)
Eric Idle,  Various / ... (46 episodes, 1969-1974)
Terry Jones,  Various / ... (46 episodes, 1969-1974)
Michael Palin,  It's Man / ... (46 episodes, 1969-1974)
Terry Gilliam,  Various / ... (46 episodes, 1969-1974)
John Cleese,  Announcer / ... (40 episodes, 1969-1973)
Carol Cleveland,  Various / ... (34 episodes, 1969-1974)
Ian Davidson,  Algy Braithwaite / ... (8 episodes, 1969-1970)
John Hughman,  Alfred Lord Tennyson / ... (8 episodes, 1970-1974)
The Fred Tomlinson Singers,  Amantillado Chorus / ... (7 episodes, 1969-1973)
Connie Booth,  Animated Mother / ... (6 episodes, 1969-1974)
Bob Raymond,  'Dad' / ... (5 episodes, 1974)
Lyn Ashley,  Algon Girl / ... (5 episodes, 1970-1972)
Rita Davies,  Argument Secretary / ... (4 episodes, 1969-1972)
Stanley Mason,  Clapper Man / ... (4 episodes, 1970-1971)
David Ballantyne,  Ivan the Terrible / ... (3 episodes, 1970-1971)
Donna Reading,  Girl in Bikini with Its Man / ... (3 episodes, 1969)
Peter Brett,  Door-to-Door Martial Arts Salesman (2 episodes, 1974)
Maureen Flanagan,  Anona Winn / ... (2 episodes, 1969-1970)
Katya Wyeth,  Elsie / ... (2 episodes, 1969)
Frank Lester,  The Late Professor Thynne (2 episodes, 1972-1974)
Neil Innes,  Hesitant guitarist / ... (2 episodes, 1974)
Dick Vosburgh,  Van der Berg (1 episode, 1969)
Sandra Richards,  'Semprini' Girl / ... (1 episode, 1970)
Julia Breck,  Puss In Boots / ... (1 episode, 1972)
Nicki Howorth,  Miss Bladder (1 episode, 1972)
Jimmy Hill,  Himself (1 episode, 1974)
Barry Cryer,  Herman Rodrigues (1 episode, 1969)
Jeannette Wild,  Second Secretary (1 episode, 1970)
Marjorie Wilde,  Dear Old Lady (1 episode, 1970)
Marie Anderson,  Girl interviewing the announcer (1 episode, 1972)
Caron Gardner,  Mary (1 episode, 1973)
Nosher Powell,  Jack Bodell (1 episode, 1973)
Carolae Donoghue,  Vera's Husband's Mistress (1 episode, 1969)
Vincent Wong,  Mr. Kamikaze (1 episode, 1970)
Helena Clayton,  Various Roles (1 episode, 1971)
Nigel Jones,  Various (1 episode, 1972)
Roy Gunson, (1 episode, 1970)
Daphne Davey,  Various Roles (1 episode, 1971)
Stenson Falke, (1 episode, 1974)
Alexander Curry,  Various (1 episode, 1970)
Frank Williams,  Clerk of the Court (1 episode, 1972)
Ralph Wood, (1 episode, 1970)
Rosalind Bailey,  Elizabethan Girl (1 episode, 1972)
Marion Mould, (1 episode, 1974)
Sheila Sands,  Stripper / ... (uncredited) (2 episodes, 1969)
Richard Baker,  Himself - BBC News Anchor (uncredited) (3 episodes, 1972-1973)
Douglas Adams,  Dr. Emile Koning - Surgeon / ... (uncredited) (2 episodes, 1974)
Ewa Aulin,  Harrassed Woman (uncredited) (1 episode, 1969)
Reginald Bosanquet,  Himself (uncredited) (1 episode, 1970)
Barbara Lindley,  Bride (uncredited) (1 episode, 1970)
Roy Brent,  Armoured Knight (uncredited) (1 episode, 1972)
Jonas Card,  Armoured Knight (uncredited) (1 episode, 1972)
Tony Christopher,  Armoured Knight (uncredited) (1 episode, 1972)
Beulah Hughes, (uncredited) (1 episode, 1972)
Peter Kodak,  Armoured Knight (uncredited) (1 episode, 1972)
Lulu,  Herself (uncredited) (1 episode, 1972)
Jay Neill,  Armoured Knight (uncredited) (1 episode, 1972)
Graham Skidmore,  Armoured Knight (uncredited) (1 episode, 1972)
Ringo Starr,  Himself (uncredited) (1 episode, 1972)
Fred Tomlinson,  Superintendent McGough (uncredited) (1 episode, 1972)
David Hamilton,  Himself - Thames TV Announcer (uncredited) (1 episode, 1973)
Suzy Mandel,  German Girl (uncredited) (1 episode, 1974)
Peter Woods,  BBC Presenter (uncredited) (1 episode, 1974)