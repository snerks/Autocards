from autocards import Autocards
a = Autocards()

a.clear()

content = '''
Burnley is a town in Lancashire, England, with a 2001 population of 73,021.[1] It is 21 miles (34 km) north of Manchester and 20 miles (32 km) east of Preston, at the confluence of the River Calder and River Brun. The town is located near countryside to the south and east, with the towns of Padiham and Brierfield to the west and north respectively. It has a reputation as a regional centre of excellence for the manufacturing and aerospace industries. The town began to develop in the early medieval period as a number of farming hamlets surrounded by manor houses and royal forests, and has held a market for more than 700 years. During the Industrial Revolution it became one of Lancashire's most prominent mill towns; at its peak it was one of the world's largest producers of cotton cloth, and a major centre of engineering.
'''
# Bristol City Football Club is a professional football club based in Bristol, England. They currently play in the EFL Championship, the second tier of English football. Founded in 1894, they have played their home games at Ashton Gate since 1904. The club's latest appearance in the English top flight was in 1980. The club's highest-ever league finish was second in the top flight in 1906–07. They were FA Cup runners-up in 1909, and won the Welsh Cup in 1934 despite being an English team. The club have also won the second tier title once, the third tier title four times, the Anglo-Scottish Cup once, and the Football League Trophy a record three times. The club's home colours are red and white, and their nickname is The Robins—a robin featured on the club's badge from 1976 to 1994 and from 2019 onwards. Their main rivals are Bristol Rovers, with whom they contest the Bristol derby, and Cardiff City, with whom they contest the cross-border Severnside derby.
# King Philip’s ultimate goal was to conquer Persia and help himself to the empire’s land and riches. This was not to be; King Philip was assassinated by his bodyguard Pausanias in 336 B.C. at his daughter’s wedding, before he could enjoy the spoils of his victories. His son Alexander, known to history as “Alexander The Great,” jumped at the chance to take over his father’s imperial project. The new Macedonian king led his troops across the Hellespont into Asia. (When he got there, he plunged an enormous sarissa into the ground and declared the land “spear won.”) From there, Alexander and his armies kept moving.
# A few days after the subpostmasters’ convictions were quashed, Vennells finally agreed to step back from her duties as a minister. The Bishop of St Albans said that it was “right” that Vennells did so.[28] She also apologised, saying “I am truly sorry for the suffering caused to the 39 subpostmasters as a result of their convictions which were overturned last week”. On the same day, she resigned her non-executive directorships at UK supermarket chain Morrisons and furnishings group Dunelm.[29] Sky News quoted a boardroom colleague as saying “there was no way for her to stay on after the ruling - and it's hard to see how she will ever be able to work again”. The UK government is expected to make compensation payments likely to total millions of pounds, and Vennells faces calls for her to repay bonuses she received during her time at the Post Office.
# Kirchhoff’s junction rule says that the total current into a junction equals the total current out of the junction. This is a statement of conservation of charge. It is also sometimes called Kirchhoff’s first law, Kirchhoff’s current law, the junction rule, or the node rule. Junctions can’t store current, and current can’t just disappear into thin air because charge is conserved. Therefore, the total amount of current flowing through the circuit must be constant.
# DNA sequencing is a collection of scientific methods for determining the sequence of the nucleotide bases in a molecule of DNA. All living organisms have DNA (deoxyribonucleic acid) in each of their cells. Each cell in an organism contains the genetic code for the entire organism. The process of DNA sequencing transforms the DNA from a given organism into a format that can be used by researchers for the basic study of biologic processes, medical research, and in forensics.

prefix = 'DNA SEQUENCING'

a.consume_text(content)

a.print()

# a.print(prefix)

# a.print(prefix, jeopardy=True)

a.export('history.csv', prefix='HELLENISTIC AGE:', jeopardy=False)