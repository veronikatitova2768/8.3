def calc_stat(listened):
    total_time_seconds = sum(listened)
    total_time_minutes = total_time_seconds // 60
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {total_time_minutes} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))
