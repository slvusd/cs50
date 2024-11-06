#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void update_guess(string word, string guess, string letters);
void insert_letter(string letters, string letter);

// Maximum chars in word to guess
const int MAX_WORD_LEN = 50;
// Maxiumn number of guesses
const int MAX_GUESSES = 100;

int main(int argc, string argv[])
{
    string word = argv[1];     // The word we're playing hangman for
    char guess[MAX_WORD_LEN];  // word with _'s for unguessed letters
    char letters[MAX_GUESSES]; // the letters the user guessed so far
    strcpy(letters, "");       // Initialize letters to an empty string
    strcpy(guess, word);       // Copy word into guess to start (sets \0 at end)
    int misses = 0;            // Count failed guesses

    while (true)
    {
        // TODO: Count number of incorrect guesses (misses)
        // TODO: Let user win if they guess all the letters (without guessing the word)

        // Update the guess string with _'s and letters appropriately
        update_guess(word, guess, letters);

        // Display our guess string
        printf("%s\n", guess);

        // Get input from user:
        // - Empty string means give up
        // - Single character means a guess
        // - Longer string means guess word
        string s = get_string("");

        if (strlen(s) == 0)
        {
            // Empty string = give up
            printf("%s (You gave up!)\n", word);
            return 1;
        }
        if (strlen(s) == 1)
        {
            // One character input means guessing a character

            // Insert our guess into our string of guesses
            insert_letter(letters, s);

            bool found = false; // Did we find the letter?

            // Loop over word and see if we found the letter
            for (int i = 0; i < strlen(word); i++)
            {
                if (word[i] == s[0])
                found = true;
            }

            // Display stats
            printf("Guesses: %i / Incorrect: %i / Letters: %s\n", (int) strlen(letters), misses, letters);
        }
        else if (strcmp(word, s) == 0)
        {
            // User won!
            printf("win! (%lu guesses)\n", strlen(letters));
            return 0;
        }
        else
        {
            // User guessed the wrong word!
            printf("Try again\n");
        }
    }
}

// Update guess string to fill in guessed letters of word
void update_guess(string word, string guess, string letters)
{
    // word and guess are the same length.
    // only set characters in guess that are in letters string
    for (int i = 0; i < strlen(word); i++)
    {
        guess[i] = '_';

        // TODO: Set guess[i] if letters contains word[i]
    }
}

// Insert letter alphabetically into the letters array
// i.e. insert_letter("ms", "p") modified letters to be "mps"
void insert_letter(string letters, string letter)
{
    // TODO: Replace strcat to insert characters alphabetically
    strcat(letters, letter);
}
