def process_data(string_date):
    result = {}
    for i in string_date:
        name, age, *subjects = i.split(",")
        result[name] = {
            "age": int(age),
            "courses": subjects
        }
    return result


def average_age(data):
    all_ages = 0
    count = 0
    for v in data.values():
        count += 1
        all_ages += v["age"]
    return all_ages/count


def courses(data):
    result = set()
    for v in data.values():
        result.update(v["courses"])
    return result


def most_common_courses(data):
    result = set()
    list_of_courses = []
    most_students = 0
    for v in data.values():
        for l in v["courses"]:
            list_of_courses.append(l)
    for i in range(len(list_of_courses)):
        temp_count = 0
        for j in range(i, len(list_of_courses)):
            if list_of_courses[i] == list_of_courses[j]:
                temp_count += 1
        if temp_count > most_students:
            most_students = temp_count

    for i in list_of_courses:
        if list_of_courses.count(i) == most_students:
            result.add(i)

    return result


dictionary = {'Alan Smithee': {'age': 29, 'courses': ['Math', 'Latin', 'Economics']}, 'Jane Doe': {'age': 18, 'courses': [
    'Math', 'German', 'Physics', 'Biology']}, 'John Smith': {'age': 20, 'courses': ['Math', 'Latin', 'Physics']}}
print(most_common_courses(dictionary))
