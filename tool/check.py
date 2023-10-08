#!/usr/bin/env python
import os.path
import sys
from PIL import Image
IMG_WITH = 580
IMG_HEIGHT = 126


def ok(content):
    print(f"[o] {content}")


def err(content, should_exit=False):
    print(f"[X] {content}", file=sys.stderr)
    if should_exit:
        sys.exit(1)


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def run():
    # check enable
    if not os.path.exists("./enable"):
        err("enable file missing.", True)
    enable_content = read_file("./enable").strip()
    if enable_content != "0" and enable_content != "1":
        err("invalid content in the enable file.", True)
    ok("enable file ok.")

    if enable_content == "1":
        # check banner.png
        if not os.path.exists("./banner.png"):
            err("banner.png missing.", True)
        img: Image.Image = Image.open("./banner.png", formats=("PNG",))
        if img.width != IMG_WITH or img.height != IMG_HEIGHT:
            err("invalid image dimensions for banner.png.", True)
        ok("banner.png ok.")

        # check banner_url
        if not os.path.exists("./banner_url"):
            err("banner_url file missing.", True)
        # todo: we could check the content here
        ok("banner_url file ok.")


if __name__ == "__main__":
    run()
