import json
import pytest
import datetime
from src.helpers.month_helper import get_string, get_month_num
from rich.console import Console
from rich.table import Table

# GLOBAL VARIABLES
indent_string = '*-------------------------------- '
console = Console()

def positions_searched(month_fixture, options_fixture):
    current_year_int = datetime.date.today().year
    current_month_int = datetime.date.today().month
    data_year = None
    with open('jobbs.json', 'r') as f:
        full_file = json.load(f)
        data_year = full_file[str(current_year_int)]

    # get searched works and interviews for previous month
    month_to_print = None
    if month_fixture == None:
        month_to_print = get_string(current_month_int)
    else:
        month_to_print = get_string(get_month_num(month_fixture))

    work_objects = None
    interview_objects = None
    if options_fixture == "all":
        searched_objects = list()
        work_objects = data_year[month_to_print]["work"]
        interview_objects = data_year[month_to_print]["interviews"]
    elif options_fixture == "work":
        work_objects = data_year[month_to_print]["work"]
    elif options_fixture == "interviews":
        interview_objects = data_year[month_to_print]["interviews"]

    if options_fixture == "all":
        print_work_table(work_objects)
        print_interview_table(interview_objects)
    elif options_fixture == "work":
        print_work_table(work_objects, table)
    elif options_fixture == "inter":
        print_interview_table(interview_objects)

def print_work_table(objects):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Arbetsgivare", justify="center")
    table.add_column("Jobb", justify="center")
    table.add_column("Ort", justify="center")
    table.add_column("Day", style="dim", justify="center")

    if objects == None or len(objects) == 0:
        console.log("[bold]No jobs found[bold]")
        return None
    else:
        for object in objects:
            if object['employer'] != "":
                work_item = []
                work_item.append(str(object['employer']))
                work_item.append(str(object['job']))
                work_item.append(str(object['locality']))
                work_item.append(str(object['day']))
                table.add_row(*work_item)

    console.log(f"\n[bold]Amount searched: {len(objects)}[bold]")
    console.print(table)

def print_interview_table(objects):
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Arbetsgivare", justify="center")
    table.add_column("Jobb", justify="center")
    table.add_column("Ort", justify="center")
    table.add_column("Day", style="dim", justify="center")

    if objects == None or len(objects) == 0:
        console.log("[bold]No interviews found[bold]")
        return None
    else:
        for object in objects:
            if object['employer'] != "":
                inter_item = []
                inter_item.append(str(object['employer']))
                inter_item.append(str(object['job']))
                inter_item.append(str(object['locality']))
                inter_item.append(str(object['day']))
                table.add_row(*inter_item)

    console.log(f"\n[bold]Amount Attended: {len(objects)}[bold]")
    console.print(table)
