import random 
import time
print(" ДОТА-ТРЕНАЖЁР: МАТЧ ИЗ 3 ПОПЫТОК  НАЖИМАЙ НА ENTER КАК МОЖНО БЫСТРЕЕ!")
print("Пройди все 3 раунда и узнаешь свой средний результат!")
print("-" * 40)
total = 0
for round in range(1,4):
    print(f"\n РАУНД {round}")
    print("ПРИГОТОВИЛИСЬ....")
    w  = random.uniform(2,4)
    time.sleep(w)
    commands = ["ХУКАЙ! ", "ПРОЖИМАЙ BKB! ", "КАСТУЙ САНСТРАЙК! "]
    random.choice(commands)
    start = time.time()
    current_command = random.choice(commands)
    input(f"\n {current_command} ")
    end = time.time()
    reaction_s = end - start
    reaction  = int(reaction_s * 1000)
    print(F"РАУНД {round}. пройден за {reaction} мс")
    total += reaction
print("\n" + "="*40)
print("🏁 МАТЧ ОКОНЧЕН!")
xuy = total / 3
averaga = xuy
print(f"Твое  среднее время реакции {int(averaga)} мс")
if averaga < 200:
    print("ТЫ ЕБАНЫЙ ТИТАН!")
elif averaga < 350:
    print("Нормуль. Твой ранг легенда")
elif averaga <500:
    print("ДЕД ЕБАНЫЙ! ШЕЛ КА ТЫ НАХУЙ! ТЫ РЕКРУТ")
