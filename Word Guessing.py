{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1f9cdac4-ee1a-41aa-90d6-218fd32ec0c2",
   "metadata": {},
   "source": [
    "## (Simple?) Word Guessing Program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "576317fc-0653-4d5d-a5fb-57967e5d09f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the random module\n",
    "# Get user's name and greet them.\n",
    "import random\n",
    "\n",
    "user_name = input(\"What is your name? \")\n",
    "print(f\"Welcome, and good luck, {user_name.title()}!\\n\")\n",
    "\n",
    "# List of words and choosing a random word using random.choice()\n",
    "words = ['school', 'church', 'mosque', 'train station', 'building', 'louvre', 'eiffel']\n",
    "word = random.choice(words)\n",
    "\n",
    "# User is prompted to start guessing the characters of a randomly chosen word\n",
    "print(\"Guess the characters of the random word.\")\n",
    "\n",
    "\n",
    "\"\"\"\n",
    "guesses = empty string to hold all the characters guessed by the user.\n",
    "turns = total number of turns the user has before their luck runs out.\n",
    "\"\"\"\n",
    "guesses = \"\"\n",
    "turns = 12\n",
    "\n",
    "while turns > 0:\n",
    "    failed = 0 # number of incorrect character guesses\n",
    "\n",
    "    \"\"\"\n",
    "    the for loop iterates through each character in the word, and prints it if it is in guesses, but prints an underscore if it isn't.\n",
    "    \"\"\"\n",
    "    for char in word:\n",
    "        if char in guesses:\n",
    "            print(char, end=\"\")\n",
    "        else:\n",
    "            print(\"_\", end=\" \")\n",
    "            failed += 1\n",
    "\n",
    "    # if user guesses all characters right\n",
    "    if failed == 0:\n",
    "        print(f\"\\nYou win!\\nThe word is: {word.title()}.\")\n",
    "        break\n",
    "        \n",
    "\n",
    "    \"\"\"\n",
    "    1. prompts user for new character.\n",
    "    2. checks if user wants to quit the current game.\n",
    "    3. adds characters to the guesses string if user doesn't want to quit.\n",
    "    \"\"\"\n",
    "    guess = input(\"\\nGuess a character (or enter 'quit' to exit): \")\n",
    "    if guess.lower() == \"quit\":\n",
    "        print(\"Goodbye! Play again sometime.\")\n",
    "        break\n",
    "    guesses += guess\n",
    "\n",
    "    # error handling: incorrect guesses.\n",
    "    if guess not in word:\n",
    "        turns -= 1\n",
    "        print(f\"\\n\\tWrong. You have {turns} guesses left.\")\n",
    "\n",
    "    # check if user has lost\n",
    "    if turns == 0:\n",
    "        print(f\"\\nYou lose.\\nThe word is {word.title()}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5515e5a9-5068-425f-bc08-7899aff106c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_street = [\"kayode\", [\"rukayat\", \"lateef\"], \"kudirat\", [\"fatimah\", [\"tohir\", \"tijani\", \"adamu\"], \"suliyat\", [\"azeez\", \"azeezat\"]]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "b2c21fb6-cc7b-4056-8c56-0e06acf3a5bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kayode', ['rukayat', 'lateef'], 'kudirat', ['fatimah', ['tohir', 'tijani', 'adamu'], 'suliyat', ['azeez', 'azeezat']]]\n"
     ]
    }
   ],
   "source": [
    "print(data_street)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "c1a6ae8a-b41b-4268-94d7-1b4bc2515f6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# inserting into a nested list\n",
    "data_street[3][4].insert(1, \"ahmed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7d425d60-c0d9-40f9-a70d-a4785b43433d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kayode', ['rukayat', 'lateef'], 'kudirat', ['mulikat', 'fatimah', ['tohir', 'tijani', 'adamu'], 'suliyat', ['azeez', 'ahmed', 'azeezat']]]\n"
     ]
    }
   ],
   "source": [
    "print(data_street)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6e67d72-7277-44c7-aeb0-a2f8a3b9ac77",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
