# def change_time(start, duration):
#     cdays = 0
#     other_day = False
#     time, format = start.split()
#     shour, smin = time.split(':')
#     dhour, dmin = duration.split(':')
#     pm = [str(i) for i in range(13, 24)]
#     am = [str(i) for i in range(1, 13)]
#     days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#     pm.append('00')
#     hsum = int(shour) + int(dhour)
#     msum = int(smin) + int(dmin)
#     if duration < 12:
#         if hsum < 12 and msum < 59:
#             pass
#     doce = int(dhour) // 12
#     print(doce)
#     dist = 12 - shour
#     if format == 'PM':
#         if duration - dist:
#             pass 


def add_time(start, duration, day=None):
    cdays = 0
    other_day = False
    time, format = start.split()
    shour, smin = time.split(':')
    dhour, dmin = duration.split(':')
    pm = [str(i) for i in range(13, 24)]
    am = [str(i) for i in range(1, 13)]
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    pm.append('00')
    

    # puedo hacer q cuando la suma de hasta 12, se reinicie el tiempo y sumar de nuevo. Sumar de a bloques de 12 horas si es que la duracion es muy larga  


    if int(dhour) >= 24:
        cdays += int(dhour) // 24
        hsum = int(shour) + (int(dhour)%24)
    else:
        hsum = int(shour) + int(dhour)
    msum = int(smin) + int(dmin)
    temp = format

    if msum > 60:
        hsum += msum // 60
        msum = msum % 60 
    elif msum == 60:
        msum = '00'
        hsum += 1
    if msum in range(10):
        msum = f'0{msum}'
    hsum = str(hsum)
    if hsum in pm:
        index = pm.index(hsum)
        hsum = am[index]
    
   
    
    # para los cambios de pm a am y viceversa uso el formato 24hr y despues transfiero
    if format == 'PM':
        # hdist =  int(shour) - int(hsum)
        # if hdist >= (12-int(shour)):
        #     format = 'AM'
        #     cdays += 1
        index = am.index(hsum)
        hsum_temp = pm[index]
        limit = 12
        # si la dist entre la hora final y la del principio es mayor o igual a 12 significa que paso la zona de am
        if int(hsum_temp) >= limit:
            format = 'AM'
            cdays += 1
    else:
        index = am.index(hsum)
        hsum_temp = pm[index]
        limit = 12
        # si la dist entre la hora final y la del principio es mayor o igual a 12 significa que paso la zona de am
        if int(hsum_temp) >= limit:
            format = 'PM'

    # if hdist < int(dhour):
    #     cdays += 1
    # if hdist < 11:
    #     pass


    if day is  None and cdays > 0 :
        if cdays == 1:
            new_time = f'{hsum}:{msum} {format} (next day)'
        else:
            new_time = f'{hsum}:{msum} {format} ({cdays} days later)'
    elif day is not None and cdays > 0:
        day = day.lower()
        pos = days.index(day) + (cdays % 7)
        if pos >= 7:
            pos = pos // 7
        day = days[pos]
        if cdays == 1:
            new_time = f'{hsum}:{msum} {format}, {day.capitalize()} (next day)'
        else:
            new_time = f'{hsum}:{msum} {format}, {day.capitalize()} ({cdays} days later)'
    elif cdays == 0:
        if day is None:
            new_time = f'{hsum}:{msum} {format}'
        else:
            new_time = f'{hsum}:{msum} {format}, {day}'

    return new_time


print(add_time("11:55 AM", "0:05"))
# change_time('6:40 AM', '34:00')

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00']