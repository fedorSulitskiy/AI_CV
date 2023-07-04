# AI CV Helper Project
Today we, graudate software engineers, have to apply to dozens of jobs to get a chance at an interview. We have to put up with recruiters using software which
rejects applications upon not spotting keywords in CVs. We have to show commitment by tailoring our CVs to vacancies. However it is a painful task when done for
so many applications.

Hence I made this simple tool to assist people like myself in this task! It allows one to "tailor" their CV to the job vacany, and do it en masse!

# How to use it:
1 - Create a file secret.py in the /data folder

2 - Add your openai API key to the secret.py file such as this:

    OPENAI_KEY = "your-key-right-here"

3 - In the /data/me.txt paste a few short bullet points about yourself to allow the model to compare info about you with the ideal candidate

4 - In the /data/vacancy.txt paste the bullet points / paragraph about the ideal candidate for vacany you want to apply to

5 - Go to main.py and run this file. The rest should be apparent :)

Don't be afraid to use the openai API; this program is very cheap even if used a lot. In the future I will add spending estimates, to let you know how much are you
spending on this.
