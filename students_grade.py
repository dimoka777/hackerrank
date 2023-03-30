# !/bin/python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    return [i + 5 - (i % 5) if i > 37 and (i % 5) > 2 else i for i in grades]


if __name__ == '__main__':
    print(gradingStudents([73, 67, 38, 33]))

