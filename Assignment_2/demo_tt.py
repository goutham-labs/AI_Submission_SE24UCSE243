import random
import time


def ai_bot_reply(user_question):
    """
    Produces a simulated AI reply with random delay.
    """

    ai_answers = [
        "That sounds good.",
        "I think that makes sense.",
        "Maybe, I am not completely sure.",
        "Can you tell me more about it?",
        "Yes, possibly.",
        "I don't really know much about that.",
        "It depends on the situation.",
        "That is a nice question."
    ]

    # Simulate response delay to mimic thinking
    thinking_time = random.randint(1, 3)
    time.sleep(thinking_time)

    return random.choice(ai_answers)


def conduct_test():
    print("\n************ SIMPLE TURING TEST ************\n")
    print("You are assigned as the Judge.")
    print("Two participants will answer your questions.")
    print("Your task is to identify the Human.\n")

    total_rounds = 3
    conversation_log = []

    for round_no in range(1, total_rounds + 1):
        print(f"\n===== Interaction {round_no} =====")
        judge_question = input("Enter your question: ")

        # Human response
        human_input = input("Participant X: ")

        # AI response
        print("Participant Y is responding...")
        bot_output = ai_bot_reply(judge_question)
        print("Participant Y:", bot_output)

        conversation_log.append({
            "round": round_no,
            "human": human_input,
            "bot": bot_output
        })

    print("\n************ SUMMARY ************")
    for entry in conversation_log:
        print(f"\nInteraction {entry['round']}")
        print("Participant X:", entry["human"])
        print("Participant Y:", entry["bot"])

    print("\nDecision Time!")
    guess = input("Who is Human? (X/Y): ")

    if guess.strip().upper() == "X":
        print("Correct! Participant X is the Human.")
    else:
        print("Wrong choice. Participant X was the Human.")

    print("\nTest session ended.")


if __name__ == "__main__":
    conduct_test()
