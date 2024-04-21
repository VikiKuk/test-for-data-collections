from pprint import pprint



def unic_mentors(mentors):
	all_list = []
	for m in mentors:
		all_list.extend (m)

	all_names_list = []
	for mentor in all_list:
		name = mentor.split ()[0]
		all_names_list.append(name)

	unique_names = set (all_names_list)
	all_names_sorted = sorted (list (unique_names))
	result = ', '.join(all_names_sorted)
	return result


def courses_and_mentors(courses, mentors):

	massive = []
	name = []
	for index, course_name in enumerate (courses): #цикл по курсам, перебирает с 1 по 4
		for x in mentors[index]: #цикл по менторам, берет первый список и перебирает ФИО
			name.append (x.split ()[0]) #отрезает имя
		massive.append ([course_name, name])
		name = []

	pairs = []
	result = ''
	for id1 in range(len(massive)):
		for id2 in range((id1 + 1), len(massive)):
			intersection_set = (set (massive[id1][1])).intersection (set (massive[id2][1]))
			if len (intersection_set) > 0:
				pair = [massive[id1][0], massive[id2][0]]
				pairs.append(pair)
				all_names_sorted = sorted(list (intersection_set))
				result += f"На курсах '{massive[id1][0]}' и '{massive[id2][0]}' преподают: {', '.join (all_names_sorted)} \n"
	return result


def mentors_top3(courses, mentors):
	all_list = []
	for m in mentors:
		all_list.extend(m)

	all_names_list = []
	for mentor in all_list:
		name = mentor.split()[0]
		all_names_list.append(name)

	unique_names = set(all_names_list)
	all_names_sorted = sorted(list(unique_names))
	result = ', '.join(all_names_sorted)

	popular = []
	for name in unique_names:
		popular.append([name, all_names_list.count(name)])
	popular.sort(key=lambda x: x[1], reverse=True)

	result = ''
	top_3 = popular[:3]
	for x in top_3:
		result += f'{x[0]}: {x[1]} раз(а), '
	return (result[:-2])


courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
print(f'Уникальные имена менторов: {unic_mentors(mentors)}')
print(courses_and_mentors(courses, mentors))
print(mentors_top3(courses, mentors))