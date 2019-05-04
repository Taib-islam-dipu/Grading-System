#Grading System

score = int(input('Input Score: '))

if score >= 80 and score <= 100:
    print('Latter Grade : A+'+'\n'+'Grade Point: 5')
elif score >= 70 and score <=79:
    print('Latter Grade : A' + '\n' + 'Grade Point : 4')
elif score >= 60 and score >=69:
    print('Latter Grade : A-' + '\n' + 'Grade Point : 3.5')
elif score >=50 and score <= 59:
    print('Latter Grade : B' + '\n' + 'Grade Point : 3')
elif score >=40 and score <= 49:
    print('Latter Grade : C' + '\n' + 'Grade Point : 2')
elif score >= 33 and score <=39:
    print('Latter Grade : D' + '\n' + 'Grade Point : 1')
elif score >= 0 and score <=32:
    print('Latter Grade : F' + '\n' + 'Grade Point : 0')
else:
    print('Wrong Input')
