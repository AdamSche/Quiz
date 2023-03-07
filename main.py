import random

# Define the quiz questions and their possible answers
questions = {
    "What is the name of the most famous large language model?": ["GPT-3", "BERT", "ELMo", "ULMFiT"],
    "Which company developed GPT-3?": ["OpenAI", "Google", "Facebook", "Microsoft"],
    "What is the maximum sequence length that GPT-3 can handle?": ["2048", "1024", "512", "256"],
    "What is the name of the first large language model?": ["GPT-1", "GPT-2", "BERT", "ELMo"],
    "What is the name of the Transformer-based architecture used in GPT-3?": ["T5", "BERT", "XLNet", "Transformer-XL"],
    "What is the purpose of fine-tuning a large language model?": ["Adapting it to a specific task", "Increasing its training time", "Reducing its model size", "Adding more layers"],
    "Which of the following is not a common pre-training objective for large language models?": ["Classification", "Masked Language Modeling", "Next Sentence Prediction", "Translation"],
    "What is the purpose of attention mechanisms in large language models?": ["To capture dependencies between tokens", "To reduce overfitting", "To increase model complexity", "To speed up training"],
    "What is the name of the dataset used to pre-train GPT-3?": ["WebText", "WikiText-2", "BookCorpus", "Common Crawl"],
    "What is the main drawback of large language models?": ["They require a lot of computational resources", "They are not very accurate", "They cannot handle long texts", "They are prone to overfitting"]
}

# Define a function to ask a quiz question and return the user's answer
def ask_question(question, answers):
    print(question)
    random.shuffle(answers)
    for i in range(4):
        print(f"{i+1}. {answers[i]}")
    user_answer = input("Enter your answer (1-4): ")
    while user_answer not in ["1", "2", "3", "4"]:
        user_answer = input("Invalid input. Enter your answer (1-4): ")
    return answers[int(user_answer)-1]

# Define the main quiz function
def run_quiz():
    score = 0
    for question in questions:
        correct_answer = questions[question][0]
        user_answer = ask_question(question, questions[question])
        if user_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
        print("")
    print(f"Final score: {score} out of {len(questions)}")

# Run the quiz
run_quiz()
