"""Folioforge command-line entry point."""
import argparse
from . import __version__
from .urls import delivery_url


def main() -> None:
    parser = argparse.ArgumentParser(description="Shared icon, banner, and brand asset tools.")
    parser.add_argument("--version", action="version", version=f"folioforge {__version__}")
    commands = parser.add_subparsers(dest="command")
    url = commands.add_parser("url", help="Build an unsigned Cloudinary image URL")
    url.add_argument("public_id", help="Asset path including extension, e.g. brands/acme/logo.svg")
    url.add_argument("--cloud", required=True, help="Cloudinary cloud name")
    url.add_argument("--gray", action="store_true", help="Deliver flat #808080 as PNG, preserving alpha")
    args = parser.parse_args()
    if args.command == "url":
        try:
            print(delivery_url(args.cloud, args.public_id, gray=args.gray))
        except ValueError as exc:
            parser.error(str(exc))
    else:
        parser.print_help()
