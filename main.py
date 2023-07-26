# First, import all needed modules
import argparse  # For command-line argument parsing
import time  # For time-related functions


# Next, define some custom functions
def integer(seconds: str) -> str:
    """
    Validate the 'seconds' argument received from the command line.

    Args:
        seconds (str): The input value for the number of seconds.

    Returns:
        str: The 'seconds' value as an integer (if no errors occur).

    Raises:
        argparse.ArgumentTypeError: If 'seconds' is not a positive integer or cannot be converted to an integer.
    """

    # Convert the 'seconds' input to an integer and check if it's less than or equal to 0
    if int(seconds) <= 0:
        # Raise an error if 'seconds' is not a positive integer
        raise argparse.ArgumentTypeError(f"{seconds} is not a positive integer")

    # Return 'seconds' if all is OK
    return seconds


def print_time(seconds: int, clear: bool) -> None:
    """
    Print the current time for each second in a given duration.

    Args:
        seconds (int): The total number of seconds to print the current time (it must be a positive integer).
        clear (bool): If True, print the time in "clear" mode (overwrite on the same line).

    Returns:
        None
    """
    # Iterate from 0 to 'seconds' (exclusive)
    for i in range(seconds):
        # Print the current time in the format "%H:%M:%S" (hours:minutes:seconds),
        # followed by "\r" if it's not the last second and 'clear' flag is set,
        # or "\n" if it's the last second or 'clear' flag is not set
        print(time.strftime("%H:%M:%S", time.localtime()), end="\r" if i != seconds - 1 and clear else "\n")

        # If it's not the last second, sleep for 1 second to create a timer effect
        if i != seconds - 1:
            time.sleep(1)


def main() -> None:
    """
    Main function to handle command-line arguments and execute the program.

    Returns:
        None
    """
    # Create an argument parser with a description of the script's purpose
    parser = argparse.ArgumentParser(description="Operations with time.")

    # Define the positional argument 'seconds', which represents the number of seconds
    # The 'validate_seconds' function is used as the type to ensure a positive integer input
    parser.add_argument('seconds', type=integer, help='Number of seconds (it must be a positive integer)')

    # Define the optional argument '-c' or '--clear' to enable the "clear" mode
    parser.add_argument('-c', '--clear', action='store_true',
                        help='Enable "clear" mode to overwrite output on the same line')

    # Parse the command-line arguments and store them in the 'args' variable
    args = parser.parse_args()

    # Convert the 'seconds' argument to an integer
    seconds = int(args.seconds)

    # Call the 'print_time' function to print the time for the specified duration
    print_time(seconds, args.clear)


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # If the script is run directly, execute the 'main' function
    main()
