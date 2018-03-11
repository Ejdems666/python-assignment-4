import question1
import question2
import question3
import question4
import question5
from file_handler import download_csv_sheet


def run():
    csv_sheet_name = 'data.csv'
    url = 'https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv'
    download_csv_sheet(csv_sheet_name, url)
    with open(csv_sheet_name, encoding='utf-8') as f:
        print_question_separator('1. Richest and poorest teams by cumulative player worth')
        question1.run(f)

        print_question_separator('2. Nationality with most players')
        question2.run(f)

        print_question_separator('3. Difference between worth and release clause of top 10 valuable players')
        question3.run(f)

        print_question_separator('4. Frequency of age, height and weight for all players')
        question4.run(f)

        print_question_separator('5. Average difference between value and wage of players')
        question5.run(f)


def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
