import time

ADMIN_ID = 'admin@123'
PASSWORD = '12345'

questions = {
    'python':
    {
        '1':{
            'question':'Is pyhton is interpreted?',
            'options':['yes','No'],
            'answer':1
            },
        '2':{
            'question':'Which data type is immutable in Python?',
            'options':['List','Ditionary','Set','Tuple'],
            'answer':4
            },
        '3':{
            'question':'Is python is dynamically typed?',
            'options':['No','Yes'],
            'answer':2
            },
        '4':{
            'question':'Which of the following is not a valid Python data type?',
            'options':['Set','List','Array','Tuple'],
            'answer':3
            }
        },
    'sql':
    {
        '1':{
            'question':'SQL stands for:',
            'options':['Structured Queue Language','Sequal Queue Language','Structured Query Language','Stored Query Language'],
            'answer':3
            },
        '2':{
            'question':'Which SQL command is used to remove a table from a database?',
            'options':['DELETE','DROP','CREATE','ERASE'],
            'answer':2
            },
        '3':{
            'question':'Which SQL statement is used to update data in a table?',
            'options':['CHANGE','MODIFY','UPDATE','SET'],
            'answer':3
            },
        '4':{
            'question':'What does the SQL function COUNT(*) return?',
            'options':['Number of non-null values','Total number of rows','Sum of values','Number of columns'],
            'answer':2
            }
        }
    }

user_data = {1:
             {
                 'Name':'Ayyappa',
                 'Mobile no':9177645815,
                 'Highest score':6
                 },
             2:
             {
                 'Name':'Rupesh',
                 'Mobile no':7702240889,
                 'Highest score':7
                 },
             3:
             {
                 'Name':'Srikanth',
                 'Mobile no':8332924702,
                 'Highest score':5
                 }
             }
def admin_login():
    admin_id = input('\nEnter Admin Id: ')
    password = input('Enter Password: ')
    return admin_id == ADMIN_ID and password == PASSWORD

def add_questions():
    while True:
        tech = input('Enter Technology:').lower()
        while True:
            if tech in questions:
                break
            else:
                questions[tech] = {}
                break
        q_no = str(len(questions[tech])+1)
        question = input('Enter Question:')
        while True:
            option_num = input('How many options:')
            if not option_num.isdigit():
                print('Options must be in digits!!!')
            else:
                break
        options = []
        for i in range(int(option_num)):
            option = input(f'Option {i+1}:')
            options.append(option)
        while True:
            answer = input('Correct option number:')
            if not answer.isdigit() or int(answer)>len(options):
                print('Invalid answer number!!')
            else:
                break
        questions[tech][q_no] = {
            'question':question,
            'options':options,
            'answer':int(answer)
            }
        print('Question added successfulluy...')
        break

def modify_questions():
    while True:
        tech = input('\nEnter Technology:').lower()
        if tech in questions:
            q_no = input('Enter question number to modify:')
            if q_no not in questions[tech]:
                print('Question not Found')
                return
            else:
                q = questions[tech][q_no]
                print(f'Q{q_no}: {q['question']}')
                for i in range(0,len(questions[tech][q_no]['options'])):
                    print(f' {i+1}. {questions[tech][q_no]['options'][i]}')
                print(f'Answer: Option {q['answer']}')
                ch = input('Do you want modify this question(yes/no):').lower()
                if ch == 'yes':
                    question = input('New Question:')
                    while True:
                        option_num = input('How many options:')
                        if not option_num.isdigit():
                            print('Options must be in digits!!!')
                        else:
                            break
                    options = []
                    for i in range(int(option_num)):
                        option = input(f'Option {i+1}:')
                        options.append(option)
                    while True:
                        answer = input('Correct option number:')
                        if not answer.isdigit() or int(answer)>len(options):
                            print('Invalid answer number!!\n')
                        else:
                            break
                    questions[tech][q_no] = {
                        'question':question,
                        'options':options,
                        'answer':int(answer)
                        }
                    print('Question modified successfully..')
                    break
                else:
                    return
        else:
            print('Technology not available!')

def delete_questions():
    while True:
        tech = input('\nEnter Technology (Python/SQL):').lower()
        if tech in questions:
            while True:
                q_no = input('Enter question number to delete:')
                q = questions[tech][q_no]
                print(f'Q{q_no}: {q['question']}')
                for i in range(0,len(questions[tech][q_no]['options'])):
                    print(f' {i+1}. {questions[tech][q_no]['options'][i]}')
                print(f'Answer: Option {q['answer']}')
                ch = input('Do you want delete this question(yes/no):').lower()
                if ch == 'yes':
                    del questions[tech][q_no]
                    print('Question deleted successfully..')
                    break
                else:
                    return
            break
        else:
            print('Technology not avaliable')
            
def view_all_questions():
    for tech in questions:
        print(f'\n***{tech.upper()} questions***')
        for q_no,q in questions[tech].items():
            print(f'\nQ{q_no}: {q['question']}')
            for i in range(0,len(questions[tech][q_no]['options'])):
                print(f' {i+1}. {questions[tech][q_no]['options'][i]}')
            print(f'Answer: Option {q['answer']}')
            
def view_all_users_details():
    print('\n****User Details****')
    for i in user_data:
        print(f'User-{i}')
        for names,details in user_data[i].items():
            print(f'{names}: {details}\n')

def admin_menu():
    while True:
        print('\n*****ADMIN MENU*****')
        print('1. Add Question')
        print('2. Modify Question')
        print('3. Delete Question')
        print('4. View All Questions')
        print('5. View All User Details')
        print('6. Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_questions()
        elif choice == '2':
            modify_questions()
        elif choice == '3':
            delete_questions()
        elif choice == '4':
            view_all_questions()
        elif choice == '5':
            view_all_users_details()
        elif choice == '6':
            print('Logging out...')
            break
        else:
            print('Invalid choice!.Choose Again.')


def take_quiz(name,mobile,tech,u_no):
    score = 0
    print(f'\nStarting quiz on {tech}...\n')
    start = time.time()
    for q_no,q in questions[tech].items():
        print(f'\nQ{q_no}: {q['question']}')
        for i in range(0,len(questions[tech][q_no]['options'])):
            print(f' {i+1}. {questions[tech][q_no]['options'][i]}')
        ans = int(input('Enter answer:')) 
        if ans != questions[tech][q_no]['answer']:
            print('wrong answer')
            time.sleep(0.5)
        else:
            print('correct answer')
            score += 1
            time.sleep(0.5)
    end = time.time()
    print('Your score is ',score)
    print('Time taken(in seconds):',round(end-start))
    if score>user_data[u_no]['Highest score']:
        user_data[u_no]['Highest score'] = score

def highest_score():
    def score(item):
        return item[1]['Highest score']
    sorted_data = dict(sorted(user_data.items(),key=score,reverse=True))
    print('\n***Leader Board***')
    i = 1
    for details in sorted_data.values():
        print(f'{i}.{details['Name']} score:{details['Highest score']}')
        i = i+1

def user_login():
    while True:
        name = input('Enter your name: ')
        for ch in name:
            if ch.isdigit():
                break
        else:
            break
        print('name has no digits..!!')
    while True:
        mobile = input('Enter your mobile number: ')
        if mobile[0] not in '987' or len(mobile)!=10:
            print('Invalid mobile number')
        else:
            break
    while True:
        print('\n***User_Menu***')
        print('1.Take Quiz')
        print('2.Highest scores')
        print('3.Logout')
        choice = input('Enter your choice:')
        if choice == '1':
            for u_no in user_data:
                if name == user_data[u_no]['Name'] and mobile == user_data[u_no]['Mobile no']:
                    break
            else:
                u_no = len(user_data)+1
                user_data[u_no] = {
                    'Name':name,
                    'Mobile no': int(mobile),
                    'Highest score':0
                    }
            while True:
                tech = input('Enter technology: ')
                if tech in questions:
                    take_quiz(name,mobile,tech,u_no)
                    break
                else:
                    print(f'{tech} not avaliable')
        elif choice == '2':
            highest_score()
        elif choice == '3':
            break
        else:
            print('Invalid choice!.Choose Again.') 


def main():
   while True:
        print('\n*****QUIZ SYSTEM*****')
        print('1. Admin Login')
        print('2. User Login')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            while True:
                if admin_login():
                    admin_menu()
                    break
                else:
                    print('Invalid!.Enter again.')
        elif choice == '2':
            user_login()
        elif choice == '3':
            print('Thank you for using the Quiz System!')
            break
        else:
            print('Invalid choice. Try again.')
main()
