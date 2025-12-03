"""CLI entry point for the Sticky Notes application."""
import argparse
from app.storage import Storage
from app.controller import Controller


def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(description="Sticky Notes App CLI")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add")
    add.add_argument("--title")
    add.add_argument("--content")

    sub.add_parser("list")

    args = parser.parse_args()

    controller = Controller(storage=Storage())

    if args.command == "add":
        controller.create_note(args.title, args.content)
        print("Note added.")

    elif args.command == "list":
        for n in controller.list_notes():
            print(f"{n.id}: {n.title} (pinned={n.pinned})")


if __name__ == "__main__":
    main()
