f = open('staff_data.txt', 'x')


def start():
    name = input('Enter your name:      ')
    company = input('Enter your company name:      ')
    department = input('Enter your department:      ')
    position = input('Enter your position:      ')
    salary = input('Enter your salary:      ')
    web_or_not = input('Do you have a website? (Y/N)      ')
    answer = web_or_not.lower()

    if answer == 'y':
        website = input('Enter your website:      ')
    else:
        website = 'No website'

    print(f'Staff Name:   {name}.\n\nCompany Name:   {company}.\n\nDepartment:    {department}.\n\nStaff Position:  {position}.\n\nSalary:    {salary}.\n\nWebsite:     {website}.\n\n\n')
    okay_or_not = input('Are you okay with this info? (Y/N)     ')
    next_answer = okay_or_not.lower()

    if next_answer == 'y':
        save(name, company, department, position, salary, website)
        print('Your data has saved in the system successfully!')
    else:
        start()


def save(name, company, department, position, salary, website):
    f.write(f'Staff Name:   {name}.\n\nCompany Name:   {company}.\n\nDepartment:    {department}.\n\nStaff Position:  {position}.\n\nSalary:    {salary}.\n\nWebsite:     {website}')

