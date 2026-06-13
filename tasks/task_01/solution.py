try:
    from google import genai
    from google.genai import errors
except ImportError:
    genai = None
    errors = None


ENV_PATHS = [".env", "../../.env"]
MODEL_NAME = "gemini-2.5-flash"


def load_gemini_api_key():
    for env_path in ENV_PATHS:
        try:
            env_file = open(env_path, "r", encoding="utf-8")
        except FileNotFoundError:
            continue

        with env_file:
            for line in env_file:
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip()

    return ""


def ask_the_ai(client, my_prompt):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=my_prompt,
        )
        return response.text
    except errors.ServerError:
        return "Gemini is busy right now. Please try again in a few minutes."
    except errors.APIError as error:
        return f"Gemini API error: {error}"
    except Exception:
        return "Could not connect to Gemini. Please check your internet connection and try again."


def calc_free_time(home_hour, sleep_hour):
    return sleep_hour - home_hour


def build_prompt(home_hour, sleep_hour, free_time, tasks_text, total_task_time, long_tasks_text):
    return f"""
I get home at {home_hour}:00.
I plan to sleep at {sleep_hour}:00.
I have {free_time} hours total for tasks and fun.
My tasks are: {tasks_text}
The tasks take {total_task_time} hours total.
Long tasks that may need splitting: {long_tasks_text}

Please build a balanced and encouraging schedule for my day.
Include both required tasks and fun time.
If there are long tasks, suggest how to split them into smaller parts.
If there is not enough time for everything, suggest what I should choose or prioritize.
Write the schedule in a friendly tone.
"""


def main():
    print("Balanced Day")

    if genai is None:
        print("Gemini library is not installed. Install dependencies from requirements.txt first.")
        return

    home_hour = int(input("What hour do you get home? For example, 14: "))
    sleep_hour = int(input("What hour do you plan to sleep? For example, 22: "))

    free_time = calc_free_time(home_hour, sleep_hour)

    print(f"You have {free_time} hours today.")

    total_task_time = 0
    tasks_text = ""
    long_tasks_text = ""

    task_name = input("Enter a task name, or type done to finish: ")

    while task_name != "done":
        task_time = int(input("How many hours will this task take? "))

        total_task_time += task_time
        tasks_text += f"{task_name} - {task_time} hours; "

        if task_time > 3:
            long_tasks_text += f"{task_name} - {task_time} hours; "

        task_name = input("Enter a task name, or type done to finish: ")

    print(f"Your tasks take {total_task_time} hours.")
    print(f"Your tasks: {tasks_text}")

    if free_time > 0:
        tasks_percent = round(total_task_time / free_time * 100)
        rest_percent = 100 - tasks_percent

        print(f"Tasks take {tasks_percent}% of your free time.")
        print(f"Rest time is {rest_percent}%.")

    api_key = load_gemini_api_key()

    if not api_key:
        print("Gemini API key was not found in .env.")
        return

    prompt = build_prompt(
        home_hour,
        sleep_hour,
        free_time,
        tasks_text,
        total_task_time,
        long_tasks_text,
    )

    client = genai.Client(api_key=api_key)
    answer = ask_the_ai(client, prompt)

    print("Your balanced schedule:")
    print(answer)


if __name__ == "__main__":
    main()
