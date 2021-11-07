import re
import shutil
from pathlib import Path

SRC_PATH = "/Users/antonz/projects/hugo/content/post"
CONTENT_PATH = "/Users/antonz/projects/antonz.ru/content/posts"
DATE_RE = re.compile(r"date = (\d+)")


def main():
    create_dirs()
    copy_posts()


def create_dirs():
    for year in range(2014, 2022):
        dirpath(year).mkdir(exist_ok=True)


def dirpath(year):
    return Path(CONTENT_PATH, str(year))


def copy_posts():
    path = Path(SRC_PATH)
    for frompath in path.iterdir():
        copy_post(frompath)


def copy_post(frompath):
    contents = frompath.read_text()
    match = DATE_RE.search(contents)
    if not match:
        return
    year = match.group(1)
    dir = Path(dirpath(year), frompath.stem)
    dir.mkdir(exist_ok=True)
    topath = Path(dir, "index.md")
    shutil.copy(frompath, topath)
    print(topath)


if __name__ == "__main__":
    main()
