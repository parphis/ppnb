import sys
import os
from datetime import date, datetime
import db

def __exit__(v):
    if v=='q':
        back()

# Main definition - constants
menu_actions = {}

# field names related to data tables and the text to be shown for the user on input
user_fields = {
  'work_category': {
    'name':'Kategória? ',
    'color':'Szín? '
  },
  'work_company': {
    'name':'Cégnév? ',
    'color':'Szín? ',
    'contract_from':'Szerződés kezdete? ',
    'contract_to':'Szerződés vége? ',
    'salary_type':'Fizetés típus (M-havibér, H-óradíj, O-egyéb)? ',
    'salary':'Fizetés? ',
    'currency_id':'Pénznem (' + db.get_all_currency_helper_str() + ')? ',
    'type':'Típus? ',
    'contact_name':'Kapcsolattartó neve? ',
    'contact_phone':'Telefon? ',
    'contact_address':'Cím? ',
    'contact_other':'Egyéb kapcsolat? '
  },
  'work_project': {
    'name':'Projekt? ',
    'start':'Indul? ',
    'deadline':'Határidő? ',
    'work_company_id':'Cég ' + db.get_all_company_helper_str() + '? ',
    'description':'Leírás? ',
    'notes':'Egyéb? '
  },
  'work_hours': {
    'start_date':'Dátum ' + str(date.today()) + '? ',
    'start':'Kezdés ' + datetime.now().strftime("%H:%M") + '? ',
    'end':'Befejezés? ',
    'description':'Mi történt? ',
    'attachment':'Csatolmány? ',
    'work_category_id':'Kategória ' + db.get_all_category_helper_str() + '? ',
    'work_company_id':'Cég ' + db.get_all_company_helper_str() + '? ',
    'work_project_id':'Projekt ' + db.get_all_project_helper_str() + '? ',
  }
}

# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu
def main_menu():
    os.system('clear')

    choice = input("> ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            menu_actions['home']()
    return

def test_connection():
  db.test_connection()
  choice = input("> ")
  exec_menu(choice)
  return

def get_user_input(user_input_for, **params):
  prms = {}
  for key, value in user_fields[user_input_for].items():
    a = input(value + (' ['+str(params[key])+'] ' if params!={} else ""))
    __exit__(a)
    if(a=='' and params!={}):
      prms[key] = params[key]
    else:
      prms[key] = a
  return prms

def add_category():
  params = get_user_input('work_category')
  db.add_category(**params)
  choice = input("> ")
  exec_menu(choice)
  return

def edit_category():
  rows = db.find_all('work_category')
  print(db.show_categories(rows, ''))
  category_id = input('Szerkesztendő kategória id? ')
  __exit__(category_id)
  params = {}
  for row in rows:
    if(str(row[0])==category_id):
      params['name'] = row[1]
      params['color'] = row[2]
      break
  params = get_user_input('work_category', **params)
  db.edit_category(category_id, **params)
  choice = input("> ")
  exec_menu(choice)
  return

def delete_category():
  rows = db.find_all('work_category')
  print(db.show_categories(rows, ''))
  category_id = input('Törlendő kategória id? ')
  __exit__(category_id)
  db.delete_category(category_id)
  choice = input("> ")
  exec_menu(choice)
  return

def add_company():
  params = get_user_input('work_company')
  db.add_company(**params)
  choice = input("> ")
  exec_menu(choice)
  return

def edit_company():
  rows = db.find_all('work_company')
  print(db.show_companies(rows, ''))
  company_id = input('Szerkesztendő cég id? ')
  __exit__(company_id)
  params = {}
  for row in rows:
    if(str(row[0])==company_id):
      params['name'] = row[1]
      params['color'] = row[2]
      params['contract_from'] = row[3]
      params['contract_to'] = row[4]
      params['salary_type'] = row[5]
      params['salary'] = row[6]
      params['currency_id'] = row[7]
      params['type'] = row[8]
      params['contact_name'] = row[9]
      params['contact_phone'] = row[10]
      params['contact_address'] = row[11]
      params['contact_other'] = row[12]
      break
  params = get_user_input('work_company', **params)
  db.edit_company(company_id, **params)
  choice = input("> ")
  exec_menu(choice)
  return

def delete_company():
  rows = db.find_all('work_company')
  print(db.show_categories(rows, ''))
  company_id = input('Törlendő cég id? ')
  __exit__(company_id)
  db.delete_company(company_id)
  choice = input("> ")
  exec_menu(choice)
  return

def add_project():
  params = get_user_input('work_project')
  db.add_project(**params)
  choice = input("> ")
  exec_menu(choice)
  return

def edit_project():
  rows = db.find_all('work_project')
  print(db.show_projects(rows, ''))
  project_id = input('Szerkesztendő projekt id? ')
  __exit__(project_id)
  params = {}
  for row in rows:
    if(str(row[0])==project_id):
      params['name'] = row[1]
      params['start'] = row[2]
      params['deadline'] = row[3]
      params['description'] = row[4]
      params['notes'] = row[5]
      params['work_company_id'] = row[6]
      break
  params = get_user_input('work_project', **params)
  db.edit_project(project_id, **params)
  choice = input("> ")
  exec_menu(choice)
  return

def delete_project():
  rows = db.find_all('work_project')
  print(db.show_projects(rows, ''))
  project_id = input('Törlendő projekt id? ')
  __exit__(project_id)
  db.delete_project(project_id)
  choice = input("> ")
  exec_menu(choice)
  return

def add_workhour():
  params = get_user_input('work_hours')
  if not params['start_date']:
      params['start_date'] = date.today()
  if not params['start']:
      params['start'] = datetime.now().strftime("%H:%M")
  db.add_workhour(**params)
  choice = input("> ")
  exec_menu(choice)
  return

def edit_workhour():
  rows = db.workhours_for_editing()
  print(db.show_workhours(rows, ''))
  workhour_id = input('Szerkesztendő munkaóra id? ')
  __exit__(workhour_id)
  params = {}
  for row in rows:
    if(str(row[0])==workhour_id):
      params['start_date'] = row[1]
      params['start'] = row[2]
      params['end'] = row[3]
      params['description'] = row[4]
      params['attachment'] = row[7]
      params['work_category_id'] = row[8]
      params['work_company_id'] = row[9]
      params['work_project_id'] = row[10]
      break
  params = get_user_input('work_hours', **params)
  db.edit_workhour(workhour_id, **params)
  choice = input("> ")
  exec_menu(choice)
  return

def delete_workhour():
  rows = db.find_all('work_hours')
  print(db.show_workhours(rows, ''))
  workhour_id = input('Törlendő munkaóra id? ')
  __exit__(workhour_id)
  db.delete_workhour(workhour_id)
  choice = input("> ")
  exec_menu(choice)
  return

def add_diary_entry():
  res = input()
  __exit__(res)
  db.add_diary_entry(res)
  choice = input("> ")
  exec_menu(choice)
  return

def get_all_company_helper_str():
  all_rows = db.get_all_company_helper_str()
  print(all_rows)
  choice = input("> ")
  exec_menu(choice)
  return

# Back to main menu
def back():
    menu_actions['home']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================
# Menu definition
menu_actions = {
    'home': main_menu,
    'test-connection': test_connection,
    'tc': test_connection,
    'add-category': add_category,
    'acat': add_category,
    'edit-category':edit_category,
    'ecat':edit_category,
    'delete-category':delete_category,
    'add-project': add_project,
    'apro': add_project,
    'edit-project':edit_project,
    'delete-project':delete_project,
    'add-company': add_company,
    'acom': add_company,
    'edit-company':edit_company,
    'delete-company':delete_company,
    'add-workhour': add_workhour,
    'awor': add_workhour,
    'edit-workhour':edit_workhour,
    'ewor':edit_workhour,
    'delete-workhour':delete_workhour,
    'add-diary-entry':add_diary_entry,
    'ade':add_diary_entry,
    'get-all-company': get_all_company_helper_str,
    '9': back,
    'quit': exit,
    'q': exit
}
