{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "116eac20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 10: 5\n",
      "Sorry, the correct number was 2\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# Generate a random number between 1 and 10\n",
    "random_number = random.randint(1, 10)\n",
    "\n",
    "# Ask the user to guess the number\n",
    "guess = int(input(\"Guess a number between 1 and 10: \"))\n",
    "\n",
    "# Check if the guess is correct\n",
    "if guess == random_number:\n",
    "    print(\"Congratulations! You guessed the correct number.\")\n",
    "else:\n",
    "    print(\"Sorry, the correct number was\", random_number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dab0b15",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
