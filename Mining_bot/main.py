import re
import os

from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

updater = Updater(token=secret_token)


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
        [['Хочу узнать про поступление', 'Хочу узнать про общежитие']],
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


def questions_about_hostel(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Цены и виды комфортности',
         'Как и когда подавать заявление на общежитие?'],
         ['Как узнать свой идентификационный номер?',
         'Вернуться в начало']
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
            '/obzhezhitia/2022/Poryadok_predost.pdf'
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
    button = ReplyKeyboardMarkup([['Начать сначала']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Консультация по поступлению в аспирантуру пока не ' +
            'осуществляется. Обращайтесь по номеру телефона +7(812)328-82-80'
            ),
        reply_markup=button
        )


def questions_about_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Направления подготовки магистратуры'],
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


def questions_about_KCP_magister(update, context):
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
            'Порядок учета ИД размещен по ссылке: ' +
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
              'с 20 июня по 25 июля 2023 г. (18.00 МСК)\n' +
              'Окончание приёма оригиналов на бюджет: 2 августа 2023 г. ' +
              '(в 18.00 МСК)\n' +
              'Приказ о зачислении на бюджет: 3 августа 2023 г.\n' +
              'Заявление на контракт: ' +
              'с 20 июня по 11 августа 2023 г. ' +
              '(18.00 по московскому времени)\n' +
              'Окончание приёма оригиналов на контракт: ' +
              '11 августа 2023 г. (в 18.00 МСК)\n' +
              'Приказ о зачислении на контракт: 12 августа 2023 г.\n'
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
            'Университета (личный кабинет)\n' +
            '4) «Единый портал государственных и муниципальных услуг ' +
            '(функций)» (ГосУслуги))'
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
        text='Списки поступающих будут опубликованы после 20-го июня.',
        reply_markup=buttons
        )


def questions_about_first_course(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['Направления подготовки/специальности'],
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


def questions_about_KCP_first_course(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Информация о количестве мест опубликована по ссылке: ' +
            'https://priem.spmi.ru/sites/default/files/manager' +
            '/03.PlanPriema/kcp_bac_spec.pdf'
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
            'по 25 июля 2023 г. (по ЕГЭ) (18.00 МСК).\n\n' +
            'Окончание приёма оригиналов на бюджет:\n' +
            'по 28 июля 2023 г. (12.00 МСК) - для поступающих ' +
            'на приоритетном этапе зачисления (квоты и БВИ)\n' +
            'по 3 августа 2023 г. (12.00 МСК) - для поступающих ' +
            'по общему конкурсу.\n\n'
            'Приказы о зачислении на бюджет:\n' +
            '29 июля 2023 г. - для поступающих на приоритетном этапе\n' +
            '5 августа 2023 г. - для поступающих по общему конкурсу.\n\n' +
            'Заявления на контракт:\n' +
            'с 20 июня по 11 августа (18.00 МСК).\n\n' +
            'Окончание приёма оригиналов на контракт:\n' +
            'по 11 августа 2023 г. (18.00 МСК).\n\n' +
            'Приказ о зачислении на контракт:\n' +
            '12 августа 2023 г.'
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
        text='Списки поступающих будут опубликованы после 20-го июня.',
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
            '*Страховое свидетельство обязательного пенсионного ' +
            'страхования (СНИЛС)\n' +
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
            '*олимпиада школьников «ОММО»\n' +
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


dict = {
    r'оператор':
        call_operator,
    r'здравствуйте|сначала|привет|начало':
        wake_up,
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
    r'Минимальны. балл':
        questions_about_min_ege_first_course,
    r'Требуемые ЕГЭ':
        questions_about_ege_first_course,
    r'Информация о направлениях подготовки/специальностях':
        questions_about_landing_first_course,
    r'План приёма на первый курс':
        questions_about_KCP_first_course,
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
        questions_about_KCP_magister,
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
    r'Идентификационный':
        questions_about_identificate_number,
    r'общежитие':
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
