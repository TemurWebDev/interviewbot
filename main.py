import asyncio
import logging
from date.date import usercreate,userget
from keyboards.defoult import admincommands,adminusers,admin_interview
from keyboards.usersKeyboards import BoshMenu,interview,endstate
from keyboards.inline import startpython, startdjango, startdrf, startjobinterview, rek
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


from date.date import interview_category_name,interview_answer
from date.fuzz import suniyintelekt,helpbot


from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")


#API_TOKEN = '6123719033:AAG-t3yeKsHdKIPEn2zvD4Zc-PKJdgP8A5k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

python = interview_category_name('python')
django = interview_category_name('django')
drf = interview_category_name('DRF')
jobinterview = interview_category_name('jobinterview')




class Python(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()
    savol12 = State()


class Django(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()



class DRF(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()




class Job(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()
    savol12 = State()
    savol13 = State()
    savol14 = State()
    savol15 = State()
    savol16 = State()
    savol17 = State()
    savol18 = State()
    savol19 = State()




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id

    usercreate(first_name, username, user_id)
    if message.from_user.id == 1363350178:
        await bot.send_message(chat_id=1363350178, text='Siz adminsiz', reply_markup=admincommands)

    else:
        await message.reply(f"Salom. {message.from_user.first_name}",reply_markup=interview,parse_mode="HTML")


@dp.message_handler(commands=['start'],state='*')
async def startstate(message: types.Message):
    await message.answer(f"Savollarga javob berishda davom eting!")



@dp.message_handler(commands=['help'],state='*')
async def helpstate(message: types.Message):
    await message.answer(f"{helpbot()}")




@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(f"{helpbot()}")





@dp.message_handler(text="interviews",chat_id=1363350178)
async def userinterview(message: types.Message):

    await message.answer('interviews',reply_markup=admin_interview)



@dp.message_handler(text="back")
async def userback(message: types.Message):
    if message.from_user.id == 1363350178:
        await message.answer('Bosh menyu', reply_markup=admincommands)
    # else:
    #     await message.answer('Main menu',reply_markup=BoshMenu)


# Interview commands


@dp.message_handler(text="Python")
async def pythoninterview(message: types.Message):
    await message.answer("Python interview savollari!\nSavollar soni: 12 ta",reply_markup=startpython)




@dp.message_handler(text="end interview",state='*')
async def stateend(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()
    await message.answer("Intervyu tugadi ❌", reply_markup=interview)


# @dp.message_handler(text="end interview")
# async def stateendnon(message: types.Message):
#
#     await message.answer("Intervyu tugadi ❌", reply_markup=interview)



# python state

@dp.callback_query_handler(text="python",state=None)
async def start_question(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{python[0]['question']} ?")
    await call.answer(cache_time=60)
    await Python.savol1.set()


@dp.message_handler(state=Python.savol1)
async def answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(python[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    print(oxshash)

    if len(javob1) > 15 and oxshash > 40:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{python[1]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Python.savol2)
async def answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(python[1]['question'])
    oxshash = suniyintelekt(javob2, javoblar)
    print(oxshash)
    if len(javob2) > 15 and oxshash > 40:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{python[2]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol3)
async def answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(python[2]['question'])
    oxshash = suniyintelekt(javob3, javoblar)
    print(oxshash)
    if len(javob3) > 15 and oxshash > 40:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{python[3]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol4)
async def answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(python[3]['question'])
    oxshash = suniyintelekt(javob4, javoblar)
    print(oxshash)
    if len(javob4) > 15 and oxshash > 40:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{python[4]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol5)
async def answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(python[4]['question'])
    oxshash = suniyintelekt(javob5, javoblar)
    print(oxshash)
    if len(javob5) > 15 and oxshash > 40:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{python[5]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol6)
async def answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(python[5]['question'])
    oxshash = suniyintelekt(javob6, javoblar)
    print(oxshash)
    if len(javob6) > 15 and oxshash > 40:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{python[6]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol7)
async def answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(python[6]['question'])
    oxshash = suniyintelekt(javob7, javoblar)
    print(oxshash)
    if len(javob7) > 15 and oxshash > 40:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{python[7]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Python.savol8)
async def answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(python[7]['question'])
    oxshash = suniyintelekt(javob8, javoblar)
    print(oxshash)
    if len(javob8) > 15 and oxshash > 40:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{python[8]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol9)
async def answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(python[8]['question'])
    oxshash = suniyintelekt(javob9, javoblar)
    print(oxshash)
    if len(javob9) > 15 and oxshash > 40:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{python[9]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Python.savol10)
async def answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(python[9]['question'])
    oxshash = suniyintelekt(javob10, javoblar)
    print(oxshash)
    if len(javob10) > 15 and oxshash > 40:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{python[10]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol11)
async def answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(python[10]['question'])
    oxshash = suniyintelekt(javob11, javoblar)
    print(oxshash)
    if len(javob11) > 15 and oxshash > 40:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        await message.answer(f"12-Savol ❗️\n{python[11]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Python.savol12)
async def answer12(message: types.Message, state: FSMContext):
    javob12 = message.text
    javoblar = interview_answer(python[11]['question'])
    oxshash = suniyintelekt(javob12, javoblar)
    print(oxshash)
    if len(javob12) > 15 and oxshash > 40:
        await state.update_data(
            {"javob12": javob12,"oxshash12":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")
        javob12 = data.get("javob12")
        oxshash12 = data.get("oxshash12")

        sum = oxshash1+oxshash2+oxshash3+oxshash4+oxshash5+oxshash6+oxshash7+oxshash8+oxshash9+oxshash10+oxshash11+oxshash12


        msg1 = f"{message.from_user.first_name} ning natijasi: {sum//12}\n\n"
        msg1 += f"javob1: - {oxshash1}--{javob1}\n\n"
        msg1 += f"javob2: - {oxshash2}--{javob2}\n\n"
        msg1 += f"javob3: - {oxshash3}--{javob3}\n\n"
        msg2 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg2 += f"javob4: - {oxshash4}--{javob4}\n\n"
        msg2 += f"javob5: - {oxshash5}--{javob5}\n\n"
        msg2 += f"javob6: - {oxshash6}--{javob6}\n\n"
        msg3 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg3 += f"javob7: - {oxshash7}--{javob7}\n\n"
        msg3 += f"javob8: - {oxshash8}--{javob8}\n\n"
        msg3 += f"javob9: - {oxshash9}--{javob9}\n\n"
        msg4 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg4 += f"javob10: - {oxshash10}--{javob10}\n\n"
        msg4 += f"javob11: - {oxshash11}--{javob11}\n\n"
        msg4 += f"javob12: - {oxshash12}--{javob12}"


        msg = f"{message.from_user.first_name} ning natijasi: {sum//12}\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"


        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178,text=msg)
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1)
                await bot.send_message(chat_id=1363350178, text=msg2)
                await bot.send_message(chat_id=1363350178, text=msg3)
                await bot.send_message(chat_id=1363350178, text=msg4)
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')


        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//12} %",reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


#end python state


# django state
@dp.message_handler(text="Django")
async def djangointerview(message: types.Message):

    await message.answer("Django interview savollari!\nSavollar soni: 11 ta",reply_markup=startdjango)


@dp.callback_query_handler(text="django",state=None)
async def start_question_django(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{django[0]['question']} ?")
    await call.answer(cache_time=60)
    await Django.savol1.set()



@dp.message_handler(state=Django.savol1)
async def django_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(django[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    print(oxshash)

    if len(javob1) > 1 and oxshash > 1:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{django[1]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol2)
async def django_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(django[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    print(oxshash)

    if len(javob2) > 1 and oxshash > 1:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{django[2]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Django.savol3)
async def django_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(django[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    print(oxshash)

    if len(javob3) > 1 and oxshash > 1:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{django[3]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol4)
async def django_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(django[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    print(oxshash)

    if len(javob4) > 1 and oxshash > 1:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{django[4]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol5)
async def django_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(django[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    print(oxshash)

    if len(javob5) > 1 and oxshash > 1:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{django[5]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Django.savol6)
async def django_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(django[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    print(oxshash)

    if len(javob6) > 1 and oxshash > 1:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{django[6]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Django.savol7)
async def django_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(django[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    print(oxshash)

    if len(javob7) > 1 and oxshash > 1:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{django[7]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol8)
async def django_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(django[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    print(oxshash)

    if len(javob8) > 1 and oxshash > 1:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{django[8]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol9)
async def django_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(django[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    print(oxshash)

    if len(javob9) > 1 and oxshash > 1:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{django[9]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol10)
async def django_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(django[9]['question'])
    oxshash = suniyintelekt(javob10,javoblar)
    print(oxshash)

    if len(javob10) > 1 and oxshash > 1:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{django[10]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Django.savol11)
async def django_answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(django[10]['question'])
    oxshash = suniyintelekt(javob11, javoblar)
    print(oxshash)
    if len(javob11) > 1 and oxshash > 1:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")

        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10 + oxshash11

        msg1 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg1 += f"javob1: - {oxshash1}--{javob1}\n\n"
        msg1 += f"javob2: - {oxshash2}--{javob2}\n\n"
        msg1 += f"javob3: - {oxshash3}--{javob3}\n\n"
        msg2 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg2 += f"javob4: - {oxshash4}--{javob4}\n\n"
        msg2 += f"javob5: - {oxshash5}--{javob5}\n\n"
        msg2 += f"javob6: - {oxshash6}--{javob6}\n\n"
        msg3 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg3 += f"javob7: - {oxshash7}--{javob7}\n\n"
        msg3 += f"javob8: - {oxshash8}--{javob8}\n\n"
        msg3 += f"javob9: - {oxshash9}--{javob9}\n\n"
        msg4 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg4 += f"javob10: - {oxshash10}--{javob10}\n\n"
        msg4 += f"javob11: - {oxshash11}--{javob11}\n\n"


        msg = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg)
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1)
                await bot.send_message(chat_id=1363350178, text=msg2)
                await bot.send_message(chat_id=1363350178, text=msg3)
                await bot.send_message(chat_id=1363350178, text=msg4)
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//11} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


#end django state



# DRF state

@dp.message_handler(text="DRF")
async def drfinterview(message: types.Message):

    await message.answer("DRF interview savollari!\nSavollar soni: 10 ta",reply_markup=startdrf)


@dp.callback_query_handler(text="drf",state=None)
async def start_question_drf(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{drf[0]['question']} ?")
    await call.answer(cache_time=60)
    await DRF.savol1.set()



@dp.message_handler(state=DRF.savol1)
async def drf_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(drf[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    print(oxshash)

    if len(javob1) > 1 and oxshash > 1:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{drf[1]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol2)
async def drf_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(drf[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    print(oxshash)

    if len(javob2) > 1 and oxshash > 1:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{drf[2]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol3)
async def drf_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(drf[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    print(oxshash)

    if len(javob3) > 1 and oxshash > 1:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{drf[3]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol4)
async def drf_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(drf[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    print(oxshash)

    if len(javob4) > 1 and oxshash > 1:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{drf[4]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=DRF.savol5)
async def drf_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(drf[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    print(oxshash)

    if len(javob5) > 1 and oxshash > 1:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{drf[5]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol6)
async def drf_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(drf[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    print(oxshash)

    if len(javob6) > 1 and oxshash > 1:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{drf[6]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol7)
async def drf_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(drf[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    print(oxshash)

    if len(javob7) > 1 and oxshash > 1:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{drf[7]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol8)
async def drf_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(drf[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    print(oxshash)

    if len(javob8) > 1 and oxshash > 1:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{drf[8]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol9)
async def drf_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(drf[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    print(oxshash)

    if len(javob9) > 1 and oxshash > 1:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{drf[9]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol10)
async def drf_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(django[9]['question'])
    oxshash = suniyintelekt(javob10, javoblar)
    print(oxshash)
    if len(javob10) > 1 and oxshash > 1:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")


        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"
        msg3 += f"<b>javob9: - {oxshash9}</b>--{javob9}\n\n"
        msg4 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg4 += f"<b>javob10: - {oxshash10}</b>--{javob10}\n\n"


        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg,parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg4,parse_mode='HTML')
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//10} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


# end DRF state

# jobinterview state

@dp.message_handler(text="Job interview")
async def jobinterview_f(message: types.Message):

    await message.answer("Job interview savollari!\nSavollar soni: 18 ta",reply_markup=startjobinterview)


@dp.callback_query_handler(text="jobinterview",state=None)
async def start_question_job(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{jobinterview[0]['question']} ?")
    await call.answer(cache_time=60)
    await Job.savol1.set()



@dp.message_handler(state=Job.savol1)
async def job_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(jobinterview[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    print(oxshash)

    if len(javob1) > 1 and oxshash > 1:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{jobinterview[1]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol2)
async def job_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(jobinterview[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    print(oxshash)

    if len(javob2) > 1 and oxshash > 1:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{jobinterview[2]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol3)
async def job_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(jobinterview[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    print(oxshash)

    if len(javob3) > 1 and oxshash > 1:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{jobinterview[3]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol4)
async def job_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(jobinterview[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    print(oxshash)

    if len(javob4) > 1 and oxshash > 1:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{jobinterview[4]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol5)
async def job_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(jobinterview[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    print(oxshash)

    if len(javob5) > 1 and oxshash > 1:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{jobinterview[5]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol6)
async def job_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(jobinterview[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    print(oxshash)

    if len(javob6) > 1 and oxshash > 1:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{jobinterview[6]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")





@dp.message_handler(state=Job.savol7)
async def job_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(jobinterview[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    print(oxshash)

    if len(javob7) > 1 and oxshash > 1:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{jobinterview[7]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol8)
async def job_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(jobinterview[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    print(oxshash)

    if len(javob8) > 1 and oxshash > 1:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{jobinterview[8]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol9)
async def job_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(jobinterview[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    print(oxshash)

    if len(javob9) > 1 and oxshash > 1:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{jobinterview[9]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol10)
async def job_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(jobinterview[9]['question'])
    oxshash = suniyintelekt(javob10,javoblar)
    print(oxshash)

    if len(javob10) > 1 and oxshash > 1:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{jobinterview[10]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol11)
async def job_answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(jobinterview[10]['question'])
    oxshash = suniyintelekt(javob11,javoblar)
    print(oxshash)

    if len(javob11) > 1 and oxshash > 1:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        await message.answer(f"12-Savol ❗️\n{jobinterview[11]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol12)
async def job_answer12(message: types.Message, state: FSMContext):
    javob12 = message.text
    javoblar = interview_answer(jobinterview[11]['question'])
    oxshash = suniyintelekt(javob12,javoblar)
    print(oxshash)

    if len(javob12) > 1 and oxshash > 1:
        await state.update_data(
            {"javob12": javob12,"oxshash12":oxshash}
        )

        await message.answer(f"13-Savol ❗️\n{jobinterview[12]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol13)
async def job_answer13(message: types.Message, state: FSMContext):
    javob13 = message.text
    javoblar = interview_answer(jobinterview[12]['question'])
    oxshash = suniyintelekt(javob13,javoblar)
    print(oxshash)

    if len(javob13) > 1 and oxshash > 1:
        await state.update_data(
            {"javob13": javob13,"oxshash13":oxshash}
        )

        await message.answer(f"14-Savol ❗️\n{jobinterview[13]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol14)
async def job_answer14(message: types.Message, state: FSMContext):
    javob14 = message.text
    javoblar = interview_answer(jobinterview[13]['question'])
    oxshash = suniyintelekt(javob14, javoblar)
    print(oxshash)

    if len(javob14) > 1 and oxshash > 1:
        await state.update_data(
            {"javob14": javob14, "oxshash14": oxshash}
        )

        await message.answer(f"15-Savol ❗️\n{jobinterview[14]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol15)
async def job_answer15(message: types.Message, state: FSMContext):
    javob15 = message.text
    javoblar = interview_answer(jobinterview[14]['question'])
    oxshash = suniyintelekt(javob15, javoblar)
    print(oxshash)

    if len(javob15) > 1 and oxshash > 1:
        await state.update_data(
            {"javob15": javob15, "oxshash15": oxshash}
        )

        await message.answer(f"16-Savol ❗️\n{jobinterview[15]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol16)
async def job_answer16(message: types.Message, state: FSMContext):
    javob16 = message.text
    javoblar = interview_answer(jobinterview[15]['question'])
    oxshash = suniyintelekt(javob16, javoblar)
    print(oxshash)

    if len(javob16) > 1 and oxshash > 1:
        await state.update_data(
            {"javob16": javob16, "oxshash16": oxshash}
        )

        await message.answer(f"17-Savol ❗️\n{jobinterview[16]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol17)
async def job_answer17(message: types.Message, state: FSMContext):
    javob17 = message.text
    javoblar = interview_answer(jobinterview[16]['question'])
    oxshash = suniyintelekt(javob17, javoblar)
    print(oxshash)

    if len(javob17) > 1 and oxshash > 1:
        await state.update_data(
            {"javob17": javob17, "oxshash17": oxshash}
        )

        await message.answer(f"18-Savol ❗️\n{jobinterview[17]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Job.savol18)
async def job_answer18(message: types.Message, state: FSMContext):
    javob18 = message.text
    javoblar = interview_answer(jobinterview[17]['question'])
    oxshash = suniyintelekt(javob18, javoblar)
    print(oxshash)
    if len(javob18) > 1 and oxshash > 1:
        await state.update_data(
            {"javob18": javob18,"oxshash18":oxshash}
        )
        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")
        javob12 = data.get("javob12")
        oxshash12 = data.get("oxshash12")
        javob13 = data.get("javob13")
        oxshash13 = data.get("oxshash13")
        javob14 = data.get("javob14")
        oxshash14 = data.get("oxshash14")
        javob15 = data.get("javob15")
        oxshash15 = data.get("oxshash15")
        javob16 = data.get("javob16")
        oxshash16 = data.get("oxshash16")
        javob17 = data.get("javob17")
        oxshash17 = data.get("oxshash17")
        javob18 = data.get("javob18")
        oxshash18 = data.get("oxshash18")

        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10
        sum += oxshash11 + oxshash12 + oxshash13 + oxshash14 + oxshash15 + oxshash16 + oxshash17 + oxshash18

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"
        msg3 += f"<b>javob9: - {oxshash9}</b>--{javob9}\n\n"
        msg4 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg4 += f"<b>javob10: - {oxshash10}</b>--{javob10}\n\n"
        msg4 += f"<b>javob11: - {oxshash11}</b>--{javob11}\n\n"
        msg4 += f"<b>javob12: - {oxshash12}</b>--{javob12}\n\n"
        msg4 += f"<b>javob13: - {oxshash13}</b>--{javob13}\n\n"
        msg5 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg5 += f"<b>javob14: - {oxshash14}</b>--{javob14}\n\n"
        msg5 += f"<b>javob15: - {oxshash15}</b>--{javob15}\n\n"
        msg5 += f"<b>javob16: - {oxshash16}</b>--{javob16}\n\n"
        msg5 += f"<b>javob17: - {oxshash17}</b>--{javob17}\n\n"
        msg5 += f"<b>javob18: - {oxshash18}</b>--{javob18}\n\n"


        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}\n{msg5}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg, parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg4, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg5, parse_mode='HTML')
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(
            f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum // 18} %",
            reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")
# end jobinterview state




# End interview commands








# Admin commands
ADMINS = [1363350178]

@dp.message_handler(text="admin panel", user_id=1363350178)
async def adminpanel(message: types.Message):

    await message.answer('admin panel',reply_markup=adminusers)




@dp.message_handler(chat_id=1363350178, text='users')
async def users(message: types.Message):
    datauser = userget()
    text = f"Interview Questions || Foydalanuvchilar soni: {len(datauser)}\n\n"
    for user in datauser:
        text += f"{user['id']}). || {user['first_name']} || @{user['username']} || {user['language']}\n"
    await message.answer(text)



@dp.message_handler(text="back", user_id=1363350178)
async def back_button(message: types.Message):

    await message.answer('Bosh menyu',reply_markup=admincommands)



@dp.message_handler(text="reklama",user_id=ADMINS)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("reklama yuboring")
    await state.set_state("reklama")



@dp.message_handler(state='reklama')
async def send_ad_to_all(message: types.Message,state: FSMContext):
    try:
        await bot.send_message(chat_id=ADMINS[0],text=f"Habar to'g'rimi ‼️\n{message.text}",reply_markup=rek)
        try:
            @dp.callback_query_handler(text="ha",state='reklama')
            async def rek_ha(call: CallbackQuery):
                users = userget()
                for user in users:
                    user_id = user['user_id']
                    try:
                        await bot.send_message(chat_id=user_id, text=f"{message.text}")
                    except Exception as e:
                        print(e)
                    await asyncio.sleep(0.05)
                await bot.send_message(chat_id=ADMINS[0],text=f"Reklama yuborildi! ✅")
                await state.finish()
                await call.message.delete()
        except Exception as e:
            print(e)
        @dp.callback_query_handler(text="yuq",state='reklama')
        async def rek_yuq(call: CallbackQuery):
            await bot.send_message(chat_id=ADMINS[0],text="Reklama yuborilmadi! ❌")
            await state.finish()
            await call.message.delete()
    except Exception as e:
        print(e)



# @dp.message_handler(text="rek",user_id=ADMINS)
# async def bot_start(message: types.Message, state: FSMContext):
#     users = userget()
#     for user in users:
#         user_id = user['user_id']
#         try:
#             img = 'https://temur01.pythonanywhere.com/media/images/osmon.jpg'
#             await bot.send_photo(chat_id=user_id, photo=img,caption='test')
#         except Exception as e:
#             print(e)
#         await asyncio.sleep(0.05)




# End admin commands

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
# 
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)