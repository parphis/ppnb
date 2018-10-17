import sqlite3
from datetime import date, datetime

def test_connection():
  db = sqlite3.connect('ppnb.sqlite')
  print("SQLite3 version is: " + sqlite3.sqlite_version)
  db.close()

def add_category(**params):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()

  try:
    cursor.execute('''
      insert into work_category
              (name, color)
        values(:name, :color)''', params)
    print("Category `", params['name'], "` has been added")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def edit_category(category_id, **params):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''
      update work_category 
        set name=?
          , color=?
      where id=?''', (params['name'], params['color'], category_id))
    print("Category `", params['name'], "` has been modified")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def delete_category(category_id):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''delete from work_category where id=?''', (category_id,))
    print("Category `", category_id, "` has been deleted")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def add_company(**params):
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  try:
    cursor.execute('''INSERT INTO work_company (name, color, contract_from, contract_to, type, contact_name, contact_phone, contact_address, contact_other, salary_type, salary, currency_id)
                    VALUES(:name, :color, :contract_from, :contract_to, :type, :contact_name, :contact_phone, :contact_address, :contact_other, :salary_type, :salary, :currency_id)''', params)
    print("Company `", params['name'], "` has been created")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def edit_company(company_id, **params):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''
      update work_company 
        set name=?
          , color=?
          , contract_from=?
          , contract_to=?
          , salary_type=?
          , salary=?
          , currency_id=?
          , type=?
          , contact_name=?
          , contact_phone=?
          , contact_address=?
          , contact_other=?
      where id=?''', (
        params['name'], params['color'], params['contract_from'], params['contract_to'],
        params['salary_type'], params['salary'], params['currency_id'], params['type'],
        params['contact_name'], params['contact_phone'], params['contact_address'], params['contact_other'], company_id))
    print("Company `", params['name'], "` has been modified")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def delete_company(company_id):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''delete from work_company where id=?''', (company_id,))
    print("Company `", company_id, "` has been deleted")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def add_project(**params):
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  try:
    cursor.execute('''INSERT INTO work_project (name, start, deadline, description, notes, work_company_id)
                    VALUES(:name, :start, :deadline, :description, :notes, :work_company_id)''', params)
    print("Project `", params['name'], "` has been added")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def edit_project(project_id, **params):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''
      update work_project 
        set name=?
          , start=?
          , deadline=?
          , description=?
          , notes=?
          , work_company_id=?
      where id=?''', (
        params['name'], params['start'], params['deadline'], params['description'],
        params['notes'], params['work_company_id'], project_id))
    print("Project `", params['name'], "` has been modified")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def delete_project(project_id):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''delete from work_project where id=?''', (project_id,))
    print("Project `", project_id, "` has been deleted")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def add_workhour(**params):
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  try:
    cursor.execute('''INSERT INTO work_hours (start_date, start, end, description, attachment, work_category_id, work_company_id, work_project_id)
                    VALUES(:start_date,:start,:end,:description,:attachment,:work_category_id,:work_company_id,:work_project_id)''', params)
    print("Work hours entry `", params['start_date'], "` has been added")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def edit_workhour(workhour_id, **params):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''
      update work_hours 
        set start_date=?
          , start=?
          , end=?
          , description=?
          , attachment=?
          , work_category_id=?
          , work_company_id=?
          , work_project_id=?
      where id=?''', (
        params['start_date'], params['start'], params['end'], params['description'],
        params['attachment'], params['work_category_id'], params['work_company_id'], params['work_project_id'], workhour_id))
    print("Workhour `", params['start_date'], "` has been modified")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def delete_workhour(workhour_id):
  db = sqlite3.connect('ppnb.sqlite')
  cursor = db.cursor()
  try:
    cursor.execute('''delete from work_hours where id=?''', (workhour_id,))
    print("Workhour `", workhour_id, "` has been deleted")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def add_diary_entry(entry):
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  try:
    cursor.execute('''INSERT INTO private_diary (entry) VALUES(?)''', (entry,))
    print("Diary entry `", entry[:10], "...` has been added")
  except sqlite3.Error as err:
    print("\t!!SQLite3 failed - ", err)

  db.commit()
  db.close()

def get_foreign_helper_str(table, field='name'):
  res = "("
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  cursor.execute('''select rowid as id, ''' + field + ''' from ''' + table)

  rows = cursor.fetchall()

  for row in rows:
    res += str(row[0]) + ": " + row[1] + ", "

  db.close()

  res = res[:-2] + ")"
  return res

def get_all_company_helper_str():
  return get_foreign_helper_str('work_company')

def get_all_category_helper_str():
  return get_foreign_helper_str('work_category')

def get_all_project_helper_str():
  return get_foreign_helper_str('work_project')

def get_all_currency_helper_str():
  return get_foreign_helper_str('currency', 'long_name')

def create_table_header(**head):
  res = ""
  for key, value in head.items():
    res += str(key).ljust(value) + "|"
  res += "\n"
  for key, value in head.items():
    res += "".ljust(value, "-") + "|"
  return res

def show_categories(rows, format):
  res = create_table_header(**{'ID':8, 'Kategória':45, 'Szín':45, 'Törölve?':9})
  for row in rows:
    res += "\n" + str(row[0]).ljust(8) + "|" + row[1].ljust(45) + "|" + row[2].ljust(45) + "|" + str(row[7]) + "|"
  return res

def show_companies(rows, format):
  res = create_table_header(**{'ID':8, 'Cégnév':45, 'Kezdet':45, 'Törölve?':9})
  for row in rows:
    res += "\n" + str(row[0]).ljust(8) + "|" + row[1].ljust(45) + "|" + (row[3].ljust(45) if row[3] else "".ljust(45)) + "|" + str(row[17]) + "|"
  return res

def show_projects(rows, format):
  res = create_table_header(**{'ID':8, 'Projekt':45, 'Kezdés':45, 'Törölve?':9})
  for row in rows:
    res += "\n" + str(row[0]).ljust(8) + "|" + row[1].ljust(45) + "|" + (row[2].ljust(45) if row[2] else "".ljust(45)) + "|" + str(row[11]) + "|"
  return res

def show_workhours(rows, format):
  res = create_table_header(**{'ID':4, 'Dátum':10, 'Kezd.':5, 'Bef.':5, 'Cég':10, 'Proj.':10, 'Leírás':65})
  for row in rows:
    res += "\n" + str(row[0]).rjust(4) + "|"
    res += str(row[1]).ljust(10) + "|"
    res += (row[2].ljust(5) if row[2] else " ~ ".ljust(5)) + "|"
    res += (row[3].ljust(5) if row[3] else " ~ ".ljust(5)) + "|"
    res += ((row[5][:10]).ljust(10) if row[5] else " ~ ".ljust(10)) + "|"
    res += ((row[6][:10]).ljust(10) if row[6] else " ~ ".ljust(10)) + "|"
    res += ((row[4][:65]).ljust(65) if row[4] else " ~ ".ljust(65)) + "|"
  return res

def find_all(table):
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  cursor.execute('''select * from ''' + table)

  rows = cursor.fetchall()

  db.close()

  return rows

def workhours_for_editing():
  db = sqlite3.connect('ppnb.sqlite')

  cursor = db.cursor()

  cursor.execute('''
    select
      w.rowid as id
    , w.start_date
    , w.start
    , w.end
    , w.description
    , c.name
    , p.name
    , w.attachment
    , w.work_category_id
    , w.work_company_id
    , w.work_project_id
    from
        work_hours w
    left join work_project p on w.work_project_id=p.id
    left join work_company c on w.work_company_id=c.id
    where
      1=1
      and w.deleted=0
    order by
        w.start_date desc
      , w.start desc;''')

  rows = cursor.fetchall()

  db.close()

  return rows