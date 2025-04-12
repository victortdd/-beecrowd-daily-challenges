# def event_time()
# day_start = input()
# day_start = day_start * 24
# day_end = input
# day_end = day_end * 24
# result_end = day_end - day_start / 24
# 

from datetime import datetime, timedelta
day_start = int(input())
hour, minutes, seconds = map(int, input().split(" : "))
day_end = int(input())
hour_e, minutes_e, seconds_e = map(int, input().split(" : "))
start = datetime.strptime(f"{hour} : {minutes} : {seconds}", "%H : %M : %S")
end = datetime.strptime(f"{hour_e} : {minutes_e} : {seconds_e}", "%H : %M : %S")

data_inicio_str = f"{day_start} {start}"
data_fim_str = f"{day_end} {end}"
# Se o fim for menor que o início, significa que passou pela meia-noite
if data_fim_str <= data_inicio_str:
    data_fim_str += timedelta(days=1)

diferenca = data_fim_str - data_inicio_str

print("Duração:", diferenca)  # exibe em formato HH:MM:SS
