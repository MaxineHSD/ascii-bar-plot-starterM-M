
from rich.console import Console
from rich.text import Text


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0

    return round(value / maximum * width)


def render_bar_chart(values):
    console = Console()

    maximum = max(value for name, value in values)

    colors = ["red", "green", "blue", "yellow"]

    for i, (name, value) in enumerate(values):
        bar_length = scale_bar(value, maximum)

        bar = "█" * bar_length

        line = Text(f"{name}: ")
        line.append(bar, style=colors[i % len(colors)])
        line.append(f" {value:.2f}")

        console.print(line)


if __name__ == "__main__":
    values = [
        ("A", 2.16),
        ("B", 4.33),
        ("C", 6.57),
        ("D", 8.71),
    ]

    render_bar_chart(values)