from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.table import Table
from rich import print as rprint

first_name = Prompt.ask("Введіть ім'я")
last_name = Prompt.ask("Введіть прізвище")
group = Prompt.ask("Введіть групу", choices=["КБ-101", "КБ-102", "КБ-103", "КБ-104", "КБ-105"], case_sensitive=False)
variant = IntPrompt.ask("Введіть варіант")

first_name_styled = Text(first_name, style="blink bright_cyan")
last_name_styled = Text(last_name, style="italic #008700")
group_styled = Text(group, style="bold #d75f00")
variant_styled = Text(str(variant), style="blink #005fff")

rprint(first_name_styled)
rprint(last_name_styled)
rprint(group_styled)
rprint(variant_styled)

table = Table(title="Дані студента", header_style="bold yellow")

table.add_column("Ім'я", justify="left", style="blink bright_cyan")
table.add_column("Прізвище", justify="left", style="italic #008700")
table.add_column("Група", justify="left", style="bold #d75f00")
table.add_column("Варіант", justify="left", style="blink #005fff")

table.add_row(first_name_styled, last_name_styled, group_styled, variant_styled)

rprint(table)

