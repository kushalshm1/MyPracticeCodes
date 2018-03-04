def add_numbers(*args):
    total  = 0
    for a in args:
        total = total + a
        print(total)

add_numbers(3,32,34,56,34,25,2,5)

#Unpacking Arguments

def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) + (cigs_smoked * 2)
    print(answer)

kushals_data = [17,20,0]


health_calculator(kushals_data[0],kushals_data[1],kushals_data[3])
#Unpacking here
health_calculator(*kushals_data)

