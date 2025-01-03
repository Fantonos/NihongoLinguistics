import random
import data


# Generate a random prompt from the list
def generate_question():
    topics_choice = random.choice(topics)
    return topics_fuctions[topics_choice]()
    
    
#Check if the answer is valid
def math_prompt():
    gen_prompt = math_random()
    while True:
            if 0 <= gen_prompt[1] <= 20 and gen_prompt[1].is_integer():
                number1 = (list(data.numbers_dict.values())[gen_prompt[2]])[random.randint(0, 1)]
                nubmer2 = (list(data.numbers_dict.values())[gen_prompt[3]])[random.randint(0, 1)]
                print(number1, nubmer2)
                prompt = (f"What is {number1} {gen_prompt[4]} {nubmer2}?")
                print(f'OG English {[gen_prompt[0], int(gen_prompt[1])]}')
                return [prompt, int(gen_prompt[1])]
            else:
                gen_prompt = math_random()


#genorate a random math problem
def math_random():
    number1 = random.randint(0, 49)
    number2 = random.randint(0, 49)
    symbol = random.choice(['+', '-', '*', '/'])
    gen_prompt = (f"{number1} {symbol} {number2}")
    prompt = (f"What Is {gen_prompt}?")
    answer = eval(gen_prompt)
    return [prompt, answer, number1, number2, symbol]

#genorate a random month problem
def month_prompt():
    rand_month = list(data.Months.items())[random.randint(0, 11)]
    month_num, month_name = rand_month
    print(month_num, month_name)
    prompt = (f'What Is The {month_num} Month?')
    answer = month_name
    return [prompt, answer.lower()]

def alphabet_prompt():
    ran_letter = list(data.h_alphabet.items())[random.randint(0, 70)]
    hira_let, eng_let = ran_letter
    print(hira_let, eng_let)
    prompt = (f'What Does {hira_let} Mean?')
    answer = eng_let
    return [prompt, answer.lower()]

def colors_prompt():
    ran_color = list(data.Colors.items())[random.randint(0, 9)]
    eng_color, hira_color = ran_color
    print(eng_color, hira_color[0], hira_color[1])
    prompt = (f'What Is {hira_color[random.randint(0, 1)]} In English?')
    
    return prompt, eng_color.lower()


topics = ["Math", "Month", "Alphabet", "Colors"]

topics_fuctions = {
    "Math": math_prompt,
    "Month": month_prompt,
    "Alphabet": alphabet_prompt,
    "Colors": colors_prompt,
}

