from typing import List

# Sample input 1: (arbitrarily ordered)
prereqs_courses = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]


# # In this case, the order of the courses in the program is:
# 	Software Design
# 	Computer Networks
# 	Computer Architecture
# 	Data Structures
# 	Algorithms
# 	Foundations of Computer Science
# 	Operating Systems

# Sample output 1:
# 	"Data Structures"

def get_mid_course(prereq_course_list: List):
    prereq_course_map = {}
    root_candidates = set()
    for entry in prereq_course_list:
        prereq = entry[0]
        course = entry[1]

        prereq_course_map[prereq] = course

        root_candidates.add(prereq)

        if course in root_candidates:
            root_candidates.remove(course)

    for course in prereq_course_map.values():
        if course in root_candidates:
            root_candidates.remove(course)

    curr = list(root_candidates)[0]
    course_list = [curr]

    # build sorted list
    while prereq_course_map:
        course = prereq_course_map[curr]
        course_list.append(course)
        del prereq_course_map[curr]
        curr = course

    mid = len(course_list) // 2
    if len(course_list) % 2 == 0:
        return course_list[mid - 1]
    else:
        return course_list[mid]


if __name__ == '__main__':
    mid_course = get_mid_course(prereqs_courses)
    print(mid_course)
