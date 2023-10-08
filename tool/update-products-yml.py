#!/usr/bin/env python
import os
import shutil
import subprocess
import sys
from strictyaml import load

PATH_PRODUCTS_YML = "/skytemple-dist/products.yml"
PATH_BANNERS = "/skytemple-dist/banners"
PREFIX_PUBLIC_BANNERS = "https://skytemple-dist.s3.eu-central-1.wasabisys.com/banners"


def debug(content):
    print(f"[.] {content}")


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
    with open(PATH_PRODUCTS_YML, "r") as f:
        products_yml = load(f.read())
    # check enable
    enable = read_file("./enable").strip() == "1"
    if not enable:
        if "banner" in products_yml:
            del products_yml["banner"]
            ok("disabling banner.")
    else:
        debug("should enable.")
        git_hash = str(subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]), "ascii").strip()
        debug(f"git hash: {git_hash}")
        output_dir = os.path.join(PATH_BANNERS, git_hash)
        output_p_banner_url = os.path.join(output_dir, "banner_url")
        output_p_banner_png = os.path.join(output_dir, "banner.png")
        debug(f"creating output dir: {output_dir}")
        os.makedirs(output_dir, exist_ok=True)
        shutil.copyfile("./banner_url", output_p_banner_url)
        shutil.copyfile("./banner.png", output_p_banner_png)
        ok("copied.")
        products_yml["banner"] = {
            "url_file": f"{PREFIX_PUBLIC_BANNERS}/{git_hash}/banner_url",
            "image_file": f"{PREFIX_PUBLIC_BANNERS}/{git_hash}/banner.png"
        }
        ok("configuring banner.")

    yaml_text = products_yml.as_yaml()
    with open(PATH_PRODUCTS_YML, "w") as f:
        f.write(yaml_text)

    ok("done.")


if __name__ == "__main__":
    run()
