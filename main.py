import os
import re

from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

secret_token = os.getenv('TOKEN')
boss_token = os.getenv('BOSS_TOKEN')
updater = Updater(token=secret_token)

# dumb way to build a database before attaching a database
list_user = []


def sent_list_to_boss():
    """Отправляем необходимое письмо Дементьеву."""
    chat_id = boss_token
    bot = Bot(token=secret_token)
    message = list_user
    bot.send_message(chat_id, message)


def add_list_user(update):
    id_people = update.message.chat.id
    username = update.message.chat.username
    if [id_people, username] not in list_user:
        list_user.append([id_people, username])
        sent_list_to_boss()


def i_dont_know(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup(
        [['Перейти к оператору', 'Начнем сначала?']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Конкретизируйте свой вопрос или позовите оператора. ' +
            'Или может начнем сначала?'
            ),
        reply_markup=button
        )


def call_operator(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup(
        [['/start']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text='https://t.me/Mining_university_official',
        reply_markup=button
        )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup(
        [['Хочу узнать про поступление', 'Хочу узнать про общежития'],
         ['Конкурс "Лидер школы"', 'Не нашел ответа. Позвать оператора']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Приёмная комиссия Горного университета ' +
            'приветствует Вас, {}!'.format(name)
            ),
        reply_markup=buttons
        )
    add_list_user(update)


def questions_about_hostel(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Цены и виды комфортности'],
         ['Количество мест в общежитиях'],
         ['Как и когда подавать заявление на общежитие?'],
         ['Как узнать свой идентификационный номер?'],
         ['Вернуться в начало']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text='Что именно Вас интересует?',
        reply_markup=buttons
        )


def questions_about_identificate_number(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Данную информацию можете получить ' +
            'по ссылке: https://priem.spmi.ru/abiurient-nomer'
            )
        )


def questions_about_application_for_hostel(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Данную информацию можете получить по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager' +
            '/obzhezhitia/2023/Poryadok_predost.pdf'
            )
        )


def questions_about_price_hostel(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Данную информацию можете получить по ссылке: ' +
            'https://spmi.ru/stoimost-prozivania-s-ucetom-komfortnosti'
            )
        )


def question_len_hostels(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Данную информацию можете получить по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager/obzhezhitia' +
            '/2023/Svodnaya.pdf'
            )
        )


def questions_about_entry(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Бакалавриат или специалитет', 'Магистратура'],
         ['Аспирантура', 'Вернуться в начало']],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='На какой уровень образования Вы планируете поступать?',
        reply_markup=buttons
        )


def questions_about_phd(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Подать документы в аспирантуру'],
         ['Списки поступающих в аспирантуру'],
         ['Конкурсные группы в аспирантуре'],
         ['Вступительные испытания в аспирантуру'],
         ['Документы для поступления в аспирантуру'],
         ['Сроки подачи документов в аспирантуру'],
         ['Способы подачи документов в аспирантуру'],
         ['Возможность учета публикаций РИНЦ, ВАК, Scopus'],
         ['Контакты приёмной комиссии в аспирантуру'],
         ['Начать сначала']
         ],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=('Что Вас интересует?'),
        reply_markup=buttons
        )


def submit_documents(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Регистрируемся на сайте, заполняем анкету: \n'
              'https://priem.spmi.ru/podat-dokumenty-1'
              ),
        )


def questions_about_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Подать документы в магистратуру'],
         ['Направления подготовки магистратуры'],
         ['Вступительные испытания в магистратуру'],
         ['Документы для поступления в магистратуру'],
         ['Сроки подачи документов в магистратуру'],
         ['Способы подачи документов в магистратуру'],
         ['Списки поступающих в магистратуру'],
         ['Вернуться в начало']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text='Что именно Вас интересует?',
        reply_markup=buttons
        )


def questions_about_specialization_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['План приёма в магистратуру',
          'Информация о специальностях магистратуры'],
         ['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Предлагаем ознакомиться с количеством мест при приёме в ' +
            'магистратуру, а также получить информацию ' +
            'об образовательных программах'
            ),
        reply_markup=buttons
        )


def questions_about_kcp_magister(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Информация о количестве мест опубликована по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager' +
            '/03.PlanPriema/kcp_mag.pdf'
            ),
        )


def questions_about_landing_magister(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Подробная информация об образовательных программах мест ' +
            'собрана на сайте: http://landing.spmi.ru/magistratura'
            ),
        )


def questions_about_exams_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Вся информация по вступительным испытаниям размещена по ' +
            'ссылке: https://priem.spmi.ru/vstupitelnye-ispytaniya'
            ),
        reply_markup=buttons
        )


def questions_about_docs_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в магистратуру',
          'Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, диплом)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Договор о целевом обучении (при наличии)\n' +
            '*Фотографию\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_achievement_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Порядок учета индивидуальных достижений в магистратуру'],
         ['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Следующие пункты могут дать Вам дополнительные баллы:\n' +
            '*«Философия науки»\n' +
            '*«Я-Профессионал»\n' +
            '*«Актуальные проблемы недропользования»\n' +
            '*Наличие диплома о высшем образовании с отличием\n' +
            '*Наличие публикации Scopus и Web of Science (WoS)\n' +
            '*Наличие международного сертификата, подтверждающего '
            'владение иностранным языком на уровне B2 и выше\n' +
            '*Наличие публикации ВАК\n' +
            '*Наличие наличие патента\n' +
            '*Студенческая олимпиады «Газпром»\n' +
            '*«CASE-IN»\n' +
            '*«Metal Cup. Устойчивое развитие»\n' +
            '*Всероссийский инженерный конкурс студентов и аспирантов'
        ),
        reply_markup=buttons
        )


def questions_about_achievement_magister_official(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Порядок учета ИД размещен по ссылке:  ' +
            'https://priem.spmi.ru/sites/default/files/manager/' +
            '02.NormativnayaBaza/' +
            'Poryadok_ucheta_individualnih_dostijenii_postupaushih.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_period_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Информация о сроках проведения приёма в магистратуру'],
         ['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=('Заявление на бюджет: ' +
              'с 20 июня по 25 июля 2023 года (18.00 МСК)\n' +
              'Окончание приёма оригиналов на бюджет: 2 августа 2023 года ' +
              '(в 18.00 МСК)\n' +
              'Приказ о зачислении на бюджет: 3 августа 2023 года\n' +
              'Заявление на контракт: ' +
              'с 20 июня по 11 августа 2023 года ' +
              '(18.00 по московскому времени)\n' +
              'Окончание приёма оригиналов на контракт: ' +
              '11 августа 2023 года (в 18.00 МСК)\n' +
              'Приказ о зачислении на контракт: 12 августа 2023 года\n'
              ),
        reply_markup=buttons
    )


def questions_about_period_magister_official(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Информация о сроках проведения приёма размещена по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager/' +
            '01.Postupaushim/Informaciya_o_srokah_provedeniya_priema.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_method_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Заявление о приеме и документы, необходимые для поступления, ' +
            'от поступающих принимаются следующими способами:\n' +
            '1) представляются в Университет лично поступающим;\n' +
            '2) через операторов почтовой связи;\n' +
            '3) посредством электронной информационной системы ' +
            'Университета (личный кабинет)\n'
        ),
        reply_markup=buttons
        )


def questions_about_lists_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к магистратуре']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=('Списки поступающих доступны по ссылке: ' +
              'http://priem2023.spmi.ru/'
              ),
        reply_markup=buttons
        )


def questions_about_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Подать документы в бакалавриат/специалитет'],
         ['Направления подготовки/специальности'],
         ['Требуемые ЕГЭ'],
         ['Минимальные баллы'],
         ['Необходимые документы на первый курс'],
         ['Сроки подачи на первый курс'],
         ['Способы подачи на первый курс'],
         ['Списки поступающих на первый курс'],
         ['Вернуться в начало']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text='Что именно Вас интересует?',
        reply_markup=buttons
        )


def questions_about_specialization_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['План приёма на первый курс'],
         ['Информация о направлениях подготовки/специальностях'],
         ['Назад к специалитету/бакалавриату']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Предлагаем ознакомиться с количеством мест при приёме на ' +
            'первый курс, а также получить информацию ' +
            'об образовательных программах'
            ),
        reply_markup=buttons
        )


def questions_about_kcp_first_course(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Информация о количестве мест опубликована по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager' +
            '/03.PlanPriema/kcp_bak_spec.pdf'
            ),
        )


def questions_about_landing_first_course(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Подробная информация об образовательных программах мест ' +
            'собрана на сайте: http://landing.spmi.ru/bakalavriat'
            ),
        )


def questions_about_ege_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Перечень вступительных испытаний (т.е. ЕГЭ) опубликован ' +
            'по ссылке: https://priem.spmi.ru/sites/default/files/manager/' +
            '04.VstupitelnieIspitaniya/Perechen_Vstupitelnih_ispitaniy.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_min_ege_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Минимальные пороговые'],
         ['Минимальные проходные баллы прошлых лет'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Здесь Вы можете ознакомиться с ' +
            'двумя видами минимальных баллов:\n' +
            '*Минимальные пороговые - это минимальные баллы для подачи ' +
            'документов (если будут меньше - мы не сможем их принять)\n' +
            '*Минимальные проходные баллы прошлых лет - балл последнего ' +
            'зачисленного в прошлом году'
            ),
        reply_markup=buttons
    )


def questions_about_min_ege_threshold_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к минимальным баллам'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Минимальные пороговые баллы опубликованы ' +
            'по ссылке: https://priem.spmi.ru/sites/default/files/manager/' +
            '04.VstupitelnieIspitaniya/' +
            'Minimalnie_bally_uspeshnogo_prohojdeniya_VI.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_min_ege_last_year_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к минимальным баллам'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Минимальные проходные баллы опубликованы ' +
            'по ссылке: https://priem.spmi.ru/sites/default/files/manager/' +
            '01.Postupaushim/Minimalny_prokhodnoy.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_period__first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Информация о сроках проведения приёма в бакалавриат/специалитет'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Заявление на бюджет:\n' +
            'с 20 июня по 10 июля 2023 (по ВИ) или ' +
            'по 25 июля 2023 года (по ЕГЭ) (18.00 МСК).\n\n' +
            'Окончание приёма оригиналов на бюджет:\n' +
            'по 28 июля 2023 года (12.00 МСК) - для поступающих ' +
            'на приоритетном этапе зачисления (квоты и БВИ)\n' +
            'по 3 августа 2023 года (12.00 МСК) - для поступающих ' +
            'по общему конкурсу.\n\n'
            'Приказы о зачислении на бюджет:\n' +
            '29 июля 2023 года - для поступающих на приоритетном этапе\n' +
            '5 августа 2023 года - для поступающих по общему конкурсу.\n\n' +
            'Заявления на контракт:\n' +
            'с 20 июня по 11 августа (18.00 МСК).\n\n' +
            'Окончание приёма оригиналов на контракт:\n' +
            'по 11 августа 2023 года (18.00 МСК).\n\n' +
            'Приказ о зачислении на контракт:\n' +
            '12 августа 2023 года'
            ),
        reply_markup=buttons
    )


def questions_about_period_first_course_official(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Информация о сроках проведения приёма размещена по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager/' +
            '01.Postupaushim/Informaciya_o_srokah_provedeniya_priema.pdf'
            ),
        reply_markup=buttons
        )


def questions_about_method_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Заявление о приеме и документы, необходимые для поступления, ' +
            'от поступающих принимаются следующими способами:\n' +
            '1) представляются в Университет лично поступающим;\n' +
            '2) через операторов почтовой связи;\n' +
            '3) посредством электронной информационной системы ' +
            'Университета (личный кабинет)\n' +
            '4) «Единый портал государственных и муниципальных услуг ' +
            '(функций)» (ГосУслуги))'
        ),
        reply_markup=buttons
        )


def questions_about_lists_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=('Списки поступающих доступны по ссылке: ' +
              'http://priem2023.spmi.ru/'
              ),
        reply_markup=buttons
        )


def questions_about_docs_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Поступление на бюджет'],
         ['Поступление на платное'],
         ['Поступление иностранных граждан']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=('Что именно Вас интересует?'),
        reply_markup=buttons
        )


def questions_about_first_course_budget(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Общий конкурс'],
         ['Квота приёма на целевое обучение'],
         ['Особая квота'],
         ['Отдельная квота'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text='Выберите вид приёма',
        reply_markup=buttons
        )


def questions_about_first_course_budget_general(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_first_course_budget_targeted(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Договор о целевом обучении \n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_first_course_budget_specific(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Подтверждающие документы \n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_first_course_budget_separated(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Подтверждающие документы \n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_first_course_contract(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
            '*Договор об оказании платных образовательных услуг \n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_first_course_foreigner(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень индивидуальных достижений в бакалавриате/специалитете'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '*Заявление о приеме в Университет \n' +
            '*Документ, удостоверяющий личность и гражданство ' +
            'поступающего (как правило, паспорт)\n' +
            '*Документ, удостоверяющий образование соответствующего ' +
            'уровня (как правило, аттестат)\n' +
            '*Перевод документов на русский язык \n' +
            '*Фотографию (если необходимо сдавать ВИ)\n' +
            '*Документы, подтверждающие индивидуальные достижения'
        ),
        reply_markup=buttons
        )


def questions_about_achievement_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Порядок учета индивидуальных достижений в бакалавриат/специалитет'],
         ['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Следующие пункты могут дать Вам дополнительные баллы:\n' +
            '*чемпион/призёр спортивных соревнований' +
            'международного уровня\n' +
            '*олимпиада школьников «Гранит науки»\n' +
            '*олимпиада школьников «Бельчонок»\n' +
            '*олимпиада школьников «Газпром»\n' +
            '*олимпиады из перечня РСОШ\n' +
            '*аттестат/диплом с отличием\n' +
            '*региональный этап Всероссийской олимпиалы\n' +
            '*Международная конференция-конкурс' +
            '«Экологическое образование в средней школе»'
            ),
        reply_markup=buttons
        )


def questions_about_achievement_first_course_official(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Назад к бакалавриату/специалитету']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Порядок учета ИД размещен по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager/' +
            '02.NormativnayaBaza/' +
            'Poryadok_ucheta_individualnih_dostijenii_postupaushih.pdf'
            ),
        reply_markup=buttons
        )


def lider_of_the_school(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Как принять участие в конкурсе?'],
         ['Я подал соглашение, что дальше?'],
         ['Когда будет итоговый конкурсный список участников "Лидер школы"?'],
         ['Я в списке. Что дальше?'],
         ['Когда зачисление?'],
         ['Вернуться в начало']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Конкурс «Лидер школы» проводится с целью организации ' +
            'качественного ' +
            'приема на обучение по направлениям подготовки и специальностям ' +
            'Горного университета в 2023 году. В конкурсе могут принять ' +
            'участие выпускники средних общеобразовательных учреждений, ' +
            'успешно сдавших ЕГЭ по предметам, профильным для ' +
            'поступления в Университет и имеющим суммарный конкурсный ' +
            'балл выше установленного порогового значения для ' +
            'поступления на места в рамках «Отраслевого гранта».'
        ),
        reply_markup=buttons
        )


def enter_leader_school(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Подать заявку на участие в конкурсе'],
         ['Ознакомиться с положением о конкурсе'],
         ['Вернуться назад к Лидеру школы']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Вы можете оставить заявку на нашем сайте но ' +
            'предварительно советуем прочитать положение.'
        ),
        reply_markup=buttons
        )


def download_booklet(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Скачать положение о конкурсе можно по ссылке: ' +
            'https://leaderschool.spmi.ru/sites/default/files' +
            '/LeaderSchool/lider_polozhenie2023.pdf'
        ),
        )


def welcome_to_leader_school(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Подать заявку можно по ссылке: ' +
            'https://docs.google.com/forms/d/e/1FAIpQLSdZhKA47Elb-' +
            'iCrvmtnt3FwU2yxFAVDskqg0aZxj7QqCnbUGg/viewform?pli=1'
        ),
        )


def finish_entering_leader_school(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Подать документы в бакалавриат/специалитет'],
         ['Вернуться назад к Лидеру школы']],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Для участия в конкурсе необходимо подать заявление (и на ' +
            'бюджет и на контракт)'
            ),
        reply_markup=buttons
    )


def list_leader_school(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Итоговый конкурсный список участников "Лидер школы" ' +
            'будет опубликован после 05 июля. \n' +
            'Список участников доступен по ссылке:\n' +
            'http://priem2023.spmi.ru/'
        ),
        )


def what_next_leader_school(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Далее два простых действия: \n' +
            '1) Подать оригиналы документов до 12 июля \n' +
            '2) Заключить договор до 31 июля\n'
        ),
        )


def when_enrollment_leader_school(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '5 августа 2023 года - при поступлении на бюджет\n' +
            '12 августа 2023 года - при поступлении за счет ' +
            'средств отраслевого гранта'
        ),
        )


def list_abiturs_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Списки поступающих в аспирантуру опубликованы по ссылке:\n' +
            'https://priem2023.spmi.ru/aspirant/'
        ),
        )


def competitive_groups_phd(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Количество мест для приёма в аспирантуру'],
         ['Описание образовательных программ в аспирантуре'],
         ['Назад к аспирантуре']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Выберите интересующий Вас пункт'
            ),
        reply_markup=buttons
    )


def kcp_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Количество мест для приёма в аспирантуру опубликовано' +
            'по ссылке:\n' +
            'https://priem.spmi.ru/sites/default/files/' +
            'manager/08.aspirantura/bot/1.kcp_phd.pdf'
        ),
        )


def landing_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: http://landing.spmi.ru/aspirantura'),
        )


def entrance_tests_phd(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Перечень вступительных испытаний в аспирантуру'],
         ['Учет дополнительных показателей'],
         ['Структура комплексной оценки'],
         ['Учет дополнительных показателей'],
         ['Требования к структуре и содержанию научного задела'],
         ['Назад к аспирантуре']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            '- Cредний балл диплома в переводе в 100-балльную шкалу;\n' +
            '- комплексная оценка по уровню подготовленности ' +
            'и компетентности (до 100 баллов):\n' +
            'а) защита Научного задела (до 50 баллов);\n' +
            'б) cобеседование по педагогической ' +
            'подготовленности до 50 баллов);\n' +
            '- специальная дисциплина (до 100 баллов):\n' +
            'а) Вопросы по специальности (до 50 баллов);\n' +
            'б) учет дополнительных показателей (до 45 баллов);\n' +
            '- ИД (5 баллов) красный диплом\n' +
            'https://priem.spmi.ru/sites/default/' +
            'files/manager/08.aspirantura/bot/7.Vstup_isp.pdf'
            ),
        reply_markup=buttons
    )


def list_of_entrance_tests_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/7.Perechen_VI.pdf'
              ),
        )


def additional_indicators_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/bot/5.dop_pokazat.pdf'
              ),
        )


def comprehensive_assessment_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/bot/3.kompl_ocen.pdf'
              ),
        )


def scientific_groundwork(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/bot/4.trebovan_zadel.pdf'
              ),
        )


def docs_for_entrance_phd(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Приём документов в аспирантуру'],
         ['Назад к аспирантуре']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Необходимы следующие документы:\n' +
            '• заявление о приеме в аспирантуру;\n' +
            '• документ, удостоверяющий личность и гражданство поступающего ' +
            '(копию);\n' +
            '• документ об образовании (оригинал или копию);\n' +
            '• СНИЛС;\n' +
            '• при необходимости создания ' +
            'специальных условий при проведении ' +
            'вступительных испытаний – документ, ' +
            'подтверждающий инвалидность, в связи ' +
            'с наличием которой необходимо создание специальных условий;\n' +
            '• документы, подтверждающие уровень научно-педагогической ' +
            'компетентности и подготовленности поступающего по выбранному ' +
            'направлению;\n' +
            '• научный задел по каждой из выбранных конкурсных групп;\n' +
            '• документы, подтверждающие индивидуальные достижения;\n' +
            '• 4 фотографии 3 х 4 см;\n' +
            '• ИНН.'
            ),
        reply_markup=buttons
    )


def acceptance_of_documents_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/bot/6.priem_docs.pdf'
              ),
        )


def period_phd(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['План проведения Приёмной кампании в аспирантуру'],
         ['Назад к аспирантуре']
         ],
        resize_keyboard=True
        )
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Прием заявлений на обучение на места за счет ' +
            'бюджетных ассигнований федерального бюджета и по договорам ' +
            'об оказании платных образовательных услуг ' +
            'с 26.06.2023 по 28.07.2023 и' +
            'с 21.08.2023 по 29.08.2023'
            ),
        reply_markup=buttons
        )


def period_phd_official(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Проходите по ссылке: https://priem.spmi.ru/sites/' +
              'default/files/manager/08.aspirantura/bot/2.sroki_phd.pdf'
              )
        )


def method_giving_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Документы можно подать одним из трёх способов:\n' +
              '- в электронной форме посредством электронной ' +
              'информационной системы Университета ' +
              '(http://tandem-online.spmi.ru/login);\n' +
              '- через операторов почтовой связи общего пользования;\n' +
              '- лично поступающим.'
              ),
        )


def contacts_phd(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Для упрощения получения информации ' +
              'подписывайтесь на канал в телеграме:\n' +
              'https://t.me/+bUEGIrtIspI5MmNi\n' +
              'При возникновении дополнительных ' +
              'вопросов можете писать на почту:\n' +
              'asp-spb-gorniy@spmi.ru'
              ),
        )


def publication_vak_rinc_scopus(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Примеры оформления статей при подаче документов:\n' +
              'РИНЦ:https://priem.spmi.ru/sites/default' +
              '/files/manager/08.aspirantura/bot/10.Rinc_.pdf'
              'ВАК: https://priem.spmi.ru/sites/default' +
              '/files/manager/08.aspirantura/bot/9.Vak_.pdf\n' +
              'Scopus: https://priem.spmi.ru/sites/default' +
              '/files/manager/08.aspirantura/bot/8.Scopus.pdf\n'
              ),
        )


dict = {
    r'оператор':
        call_operator,
    r'здравствуйте|сначала|привет|начало':
        wake_up,
    r'Возможность учета публикаций РИНЦ, ВАК, Scopus':
        publication_vak_rinc_scopus,
    r'Контакты приёмной комиссии в аспирантуру':
        contacts_phd,
    r'Способы подачи документов в аспирантуру':
        method_giving_phd,
    r'Сроки подачи документов в аспирантуру':
        period_phd,
    r'План проведения Приёмной кампании в аспирантуру':
        period_phd_official,
    r'Приём документов в аспирантуру':
        acceptance_of_documents_phd,
    r'Документы для поступления в аспирантуру':
        docs_for_entrance_phd,
    r'Требования к структуре и содержанию научного задела':
        scientific_groundwork,
    r'Структура комплексной оценки':
        comprehensive_assessment_phd,
    r'Учет дополнительных показателей':
        additional_indicators_phd,
    r'Перечень вступительных испытаний в аспирантуру':
        list_of_entrance_tests_phd,
    r'Вступительные испытания в аспирантуру':
        entrance_tests_phd,
    r'Конкурсные группы в аспирантуре':
        competitive_groups_phd,
    r'Количество мест для приёма в аспирантуру':
        kcp_phd,
    r'Описание образовательных программ в аспирантуре':
        landing_phd,
    r'Списки поступающих в аспирантуру':
        list_abiturs_phd,
    r'Когда зачисление?':
        when_enrollment_leader_school,
    r'Я в списке. Что дальше?':
        what_next_leader_school,
    r'конкурсный список участников "Лидер школы"':
        list_leader_school,
    r'Я подал соглашение, что дальше?':
        finish_entering_leader_school,
    r'Ознакомиться с положением':
        download_booklet,
    r'Подать заявку':
        welcome_to_leader_school,
    r'Как принять участие в конкурсе?':
        enter_leader_school,
    r'Лидер школы|Вернуться назад к Лидеру школы':
        lider_of_the_school,
    r'Подать документы':
        submit_documents,
    r'Порядок учета индивидуальных достижений в бакалавриат/специалитет':
        questions_about_achievement_first_course_official,
    r'Перечень индивидуальных достижений в бакалавриате/специалитете':
        questions_about_achievement_first_course,
    r'иностран':
        questions_about_first_course_foreigner,
    r'платн|контракт':
        questions_about_first_course_contract,
    r'особа':
        questions_about_first_course_budget_specific,
    r'отдельн':
        questions_about_first_course_budget_separated,
    r'целев':
        questions_about_first_course_budget_targeted,
    r'общий конкурс':
        questions_about_first_course_budget_general,
    r'Поступление на бюджет':
        questions_about_first_course_budget,
    r'Необходимые документы на первый курс':
        questions_about_docs_first_course,
    r'Списки поступающих на первый курс':
        questions_about_lists_first_course,
    r'Способы подачи на первый курс':
        questions_about_method_first_course,
    r'Информация о сроках проведения приёма в бакалавриат/специалитет':
        questions_about_period_first_course_official,
    r'Сроки подачи на первый курс':
        questions_about_period__first_course,
    r'проходн.. бал':
        questions_about_min_ege_last_year_first_course,
    r'Минимальные пороговые':
        questions_about_min_ege_threshold_first_course,
    r'Минимальны. бал':
        questions_about_min_ege_first_course,
    r'Требуемые ЕГЭ':
        questions_about_ege_first_course,
    r'Информация о направлениях подготовки/специальностях':
        questions_about_landing_first_course,
    r'План приёма на первый курс':
        questions_about_kcp_first_course,
    r'Направления подготовки/специальности':
        questions_about_specialization_first_course,
    r'Бакалавр|специалит':
        questions_about_first_course,
    r'Списки поступающих в магистратуру':
        questions_about_lists_magister,
    r'Способы подачи документов в магистратуру':
        questions_about_method_magister,
    r'Информация о сроках проведения приёма в магистратуру':
        questions_about_period_magister_official,
    r'Сроки подачи документов в магистратуру':
        questions_about_period_magister,
    r'Порядок учета индивидуальных достижений в магистратуру':
        questions_about_achievement_magister_official,
    r'Перечень индивидуальных достижений в магистратуру':
        questions_about_achievement_magister,
    r'Документы для поступления в магистратуру':
        questions_about_docs_magister,
    r'Вступительные испытания в магистратуру':
        questions_about_exams_magister,
    r'План приёма в магистратуру':
        questions_about_kcp_magister,
    r'Информация о специальностях магистратуры':
        questions_about_landing_magister,
    r'Направления подготовки магистратуры':
        questions_about_specialization_magister,
    r'магистратур|Назад к магистратуре':
        questions_about_magister,
    r'аспирантур':
        questions_about_phd,
    r'Хочу узнать про поступление':
        questions_about_entry,
    r'заявление на общежитие':
        questions_about_application_for_hostel,
    r'Цены и виды комфортности':
        questions_about_price_hostel,
    r'Количество мест в общежитиях':
        question_len_hostels,
    r'Идентификационный':
        questions_about_identificate_number,
    r'общежити|общаг':
        questions_about_hostel,
    }


updater.dispatcher.add_handler(
    CommandHandler('start', wake_up)
    )


for a in dict:
    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.regex(
                re.compile(a, re.IGNORECASE)),
            dict[a]
            )
        )


updater.dispatcher.add_handler(MessageHandler(Filters.text, i_dont_know))
updater.start_polling()
updater.idle()
