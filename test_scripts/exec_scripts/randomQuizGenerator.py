#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
# import pprint

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# pprint.pprint(capitals)

# Generate 35 quiz files.
for quizNum in range(3):
# Create the quiz and answer key files.
    quizFile = open('C:\\Users\\pascaie\\Documents\\python_test_private\\test_scripts\\exec_scripts\\quizFiles\\capitalsQuiz%s.txt' %(quizNum + 1), 'w')
    answerKeyFile = open('C:\\Users\\pascaie\\Documents\\python_test_private\\test_scripts\\exec_scripts\\quizFiles\\capitalsQuiz_answers%s.txt' %(quizNum + 1), 'w')

    # write the header for each quizFile
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' '*20) + 'State Capital Quiz - Form %s' %(quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the state order
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # get right and wrong answer
        rightAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(rightAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [rightAnswer]  # wrongAnswer is a list, rightAnswer is a single value
        random.shuffle(answerOptions)

        # write the question and the answer otpions to quizFile
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('     %s. %s\n' %('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key to a file
        answerKeyFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(rightAnswer)]))
    quizFile.close()
    answerKeyFile.close()
