#Mainprogram
import matplotlib.pyplot
import numbers
import os

#kommentar



def printMainManu():
    print('==================================================')
    print('TEXT ANALYSER')
    print('==================================================')
    print('1. Load text file')
    print('2. Display basic statistics')
    print('3. Word frequency analysis')
    print('4. Sentence analysis')
    print('5. Character analysis')
    print('6. Export results')
    print('7. Exit')
    print('==================================================')

    #if-sats om vi har fil selekterad



def fileSelection():
    currentDirectory = os.getcwd()

    textFiles = []

    for file in os.listdir(currentDirectory):
        if file.endswith('.txt'):
            textFiles.append(file)
    
    




def displayBasicStatistics():



def wordFrequencyAnalysis():



def sentenceAnalysis():



def characterAnalysis():



def exportResults():






def exit():
    print('Goodbye!')


#Main programmet

while True:
    
    printMainManu()
    choice = input('Enter your choice (1-7): ')
        
    while choice not in ('1', '2', '3', '4', '5', '6', '7'):

        print('Invalid input')
        choice = input('Enter your choice (1-7): ')


    match choice:

        case '1':
            fileSelection()
        
        case '2':
            displayBasicStatistics()

        case '3':
            wordFrequencyAnalysis()

        case '4':
            sentenceAnalysis()
            
        case '5':
            characterAnalysis()
            
        case '6':
            exportResults()

        case '7':
            break
            #exit-metoden

