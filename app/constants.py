from datetime import datetime

CHECK_NAME_DUPLICATE = 'Проект с таким именем уже существует!'
PROJECT_NOT_FOUND = 'Проект не найден!'
CHECK_PROJECT_CLOSED = 'Закрытый проект нельзя редактировать!'
CHECK_EDIT_FULL_AMOUNT = 'Нельзя установить значение меньше, чем уже было внесено в проект!'
CANNOT_BE_DELETED = 'В проект были внесены средства, не подлежит удалению!'

PREFIX_CHARITY_PROJECT = '/charity_project'
PREFIX_DONATION = '/donation'
PREFIX_GOOGLE = '/google'

MIN_LENGTH_PASSWORD = 3
LIFETIME_SECONDS = 3600

FORMAT = '%Y/%m/%d %H:%M:%S'
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
SPREADSHEET_BODY = {
    'properties': {'title': f'Отчёт на {NOW_DATE_TIME}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 3}}}]}
TABLE_VALUES = [
    ['Отчёт от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']]