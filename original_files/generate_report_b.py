import re
from rich.console import Console
from rich.table import Table


def parse_log_file(log_file_path: str) -> list:
    """
    Parses the log file and extracts relevant information.

    :param log_file_path: Path to the log file.
    :return: A list of rows with data extracted from all relevant entries.
    """
    # Define patterns to extract all relevant information
    patterns = {
        "file_name": re.compile(r"Arguments: Namespace\(path='([^']*)'"),
        "grade": re.compile(r"### Grade:\s*(\w)"),
        "summary": re.compile(r"### Summary of Grade:\s*([\s\S]+?)\n### Analysis"),
        "analysis": re.compile(
            r"### Analysis \(with Line Numbers\):\s*([\s\S]+?)\n### Suggested Improvements"
        ),
        "lines_changed": re.compile(r"### Number of Lines Changed:\s*(\d+)"),
    }

    # Initialize lists to collect all matches
    extracted_data = {
        "file_name": [],
        "grade": [],
        "summary": [],
        "analysis": [],
        "lines_changed": [],
    }

    try:
        # Read the log file content
        with open(log_file_path, "r") as log_file:
            log_content = log_file.read()

            # Extract data for each pattern and store all matches
            for key, pattern in patterns.items():
                matches = pattern.findall(log_content)
                extracted_data[key] = matches if matches else ["N/A"]

        # Prepare the data for a Markdown table, aligning lists row-wise
        rows = [
            [
                (
                    extracted_data["file_name"][i]
                    if i < len(extracted_data["file_name"])
                    else "N/A"
                ),
                (
                    extracted_data["grade"][i]
                    if i < len(extracted_data["grade"])
                    else "N/A"
                ),
                (
                    extracted_data["summary"][i]
                    if i < len(extracted_data["summary"])
                    else "N/A"
                ),
                (
                    extracted_data["analysis"][i]
                    if i < len(extracted_data["analysis"])
                    else "N/A"
                ),
                (
                    extracted_data["lines_changed"][i]
                    if i < len(extracted_data["lines_changed"])
                    else "N/A"
                ),
            ]
            for i in range(max(len(lst) for lst in extracted_data.values()))
        ]

        return rows

    except FileNotFoundError:
        print(f"Error: The file at {log_file_path} was not found.")
        return []


log_file_path = (
    "/Users/duke/Documents/github/proj_echo/fire_and_forget/logs/echo_20240517.log"
)

data = parse_log_file(log_file_path)

# Create a console instance
console = Console()

# Create a table object with a title
table = Table(title="Code Quality Report", show_lines=True)

# Add column headers
table.add_column("File Name", justify="left", style="cyan", no_wrap=True)
table.add_column("Grade", justify="center", style="magenta")
table.add_column("Summary of Grade", justify="left", style="green")
table.add_column("Analysis (with Line Numbers)", justify="left", style="yellow")
table.add_column("Lines Changed", justify="center", style="red")

# Add each row of data to the table
for row in data:
    table.add_row(*row)

# Print the table to the console
console.print("\n")
console.print(table)
