import time

def calculate_typing_speed():
    # Sample text for typing test
    sample_text = """
    The quick brown fox jumps over the lazy dog.
    This is a famous sentence that contains every letter of the alphabet.
    Try to type this text as fast as you can!
    """
    
    print("Typing Test:")
    print(sample_text)
    print("\nStart typing the above text...")
    
    # Start the timer
    start_time = time.time()
    
    # Get user input
    user_input = input("\nYour input: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate the time taken in seconds
    time_taken = end_time - start_time
    
    # Calculate the word count of the input
    word_count = len(user_input.split())
    
    # Calculate words per minute (WPM)
    wpm = (word_count / time_taken) * 60
    
    # Display the results
    print("\nTime taken: {:.2f} seconds".format(time_taken))
    print("Words per minute (WPM): {:.2f}".format(wpm))
    
    # Check if the user typed correctly
    if user_input == sample_text.strip():
        print("\nGreat job! You typed the text correctly.")
    else:
        print("\nOops! There were some mistakes in your typing.")
        print("Try again to improve your accuracy and speed.")

if __name__ == "__main__":
    calculate_typing_speed()
