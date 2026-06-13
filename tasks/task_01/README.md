# Task 1: Balanced Day

Course project: build a smart time-management program that uses Python logic
and Gemini AI to create a balanced daily schedule.

## Goal

The program asks the user:

- when they get home;
- when they plan to sleep;
- what tasks they have today;
- how long each task should take.

Then it calculates the available time and asks Gemini to create a balanced,
encouraging schedule with both tasks and fun time.

## Stages

1. Time calculation:
   - get home hour from the user;
   - get sleep hour from the user;
   - calculate total available hours;
   - print the result.

2. Task collection:
   - use a `while` loop;
   - keep asking for tasks until the user types `done`;
   - collect task names and estimated durations;
   - sum the task durations.

3. Gemini connection:
   - use the Gemini API key from the local `.env` file;
   - build a clear prompt with an f-string;
   - call Gemini once after all data is collected.

4. Extra features:
   - show what percent of free time is used by tasks;
   - ask Gemini to split long tasks into smaller parts;
   - ask Gemini to suggest priorities if there is not enough time.

## Current Progress

Stages 1, 2, 3, and selected stage 4 features are implemented in `solution.py`.

Before running the Gemini step, install the dependency:

```powershell
pip install -r requirements.txt
```
