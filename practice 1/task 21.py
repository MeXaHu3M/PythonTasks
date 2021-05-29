def bmi(weight: float, height: float):
    return 10000 * weight / (height * height)

def print_bmi(bmi: float):
    if bmi < 18.5:
        print('Underweight')
        return
    if bmi < 25:
        print('Normal')
        return
    if bmi < 30:
        print('Overweight')
        return
    print('Obesity')

a = input().split(' ')
print_bmi(bmi(float(a[0]), float(a[1])))
