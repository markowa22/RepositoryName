salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
def function(need_money, spend, salary):
	for a in range(months):
		need_money += spend - salary
		spend = spend*1.03
	return need_money

print(round(function(need_money, spend, salary)))
