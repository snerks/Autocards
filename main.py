from autocards import Autocards
a = Autocards()

a.clear()

content = '''
King Philip’s ultimate goal was to conquer Persia and help himself to the empire’s land and riches. This was not to be; King Philip was assassinated by his bodyguard Pausanias in 336 B.C. at his daughter’s wedding, before he could enjoy the spoils of his victories. His son Alexander, known to history as “Alexander The Great,” jumped at the chance to take over his father’s imperial project. The new Macedonian king led his troops across the Hellespont into Asia. (When he got there, he plunged an enormous sarissa into the ground and declared the land “spear won.”) From there, Alexander and his armies kept moving.
'''
# A few days after the subpostmasters’ convictions were quashed, Vennells finally agreed to step back from her duties as a minister. The Bishop of St Albans said that it was “right” that Vennells did so.[28] She also apologised, saying “I am truly sorry for the suffering caused to the 39 subpostmasters as a result of their convictions which were overturned last week”. On the same day, she resigned her non-executive directorships at UK supermarket chain Morrisons and furnishings group Dunelm.[29] Sky News quoted a boardroom colleague as saying “there was no way for her to stay on after the ruling - and it's hard to see how she will ever be able to work again”. The UK government is expected to make compensation payments likely to total millions of pounds, and Vennells faces calls for her to repay bonuses she received during her time at the Post Office.
# Kirchhoff’s junction rule says that the total current into a junction equals the total current out of the junction. This is a statement of conservation of charge. It is also sometimes called Kirchhoff’s first law, Kirchhoff’s current law, the junction rule, or the node rule. Junctions can’t store current, and current can’t just disappear into thin air because charge is conserved. Therefore, the total amount of current flowing through the circuit must be constant.
# DNA sequencing is a collection of scientific methods for determining the sequence of the nucleotide bases in a molecule of DNA. All living organisms have DNA (deoxyribonucleic acid) in each of their cells. Each cell in an organism contains the genetic code for the entire organism. The process of DNA sequencing transforms the DNA from a given organism into a format that can be used by researchers for the basic study of biologic processes, medical research, and in forensics.

prefix = 'DNA SEQUENCING'

a.consume_text(content)

a.print()

# a.print(prefix)

# a.print(prefix, jeopardy=True)

a.export('history.csv', prefix='HELLENISTIC AGE:', jeopardy=False)