import re
from pathlib import Path

CONTENT_PATH = "/Users/antonz/projects/antonz.ru/content/posts"
IMAGE_SRC_PATH = "/Users/antonz/projects/antonz.ru.ghost"
IMAGE_RE = re.compile(r'/content/images/[^")]+')


def main():
    path = Path(CONTENT_PATH)
    dirs = (p for p in path.iterdir() if p.is_dir())
    for yeardir in dirs:
        postdirs = (p for p in yeardir.iterdir() if p.is_dir())
        for postdir in postdirs:
            post = Path(postdir, "index.md")
            print(post)
            rename_images(post)


def rename_images(post: Path):
    contents = post.read_text()
    contents = IMAGE_RE.sub(rename_image, contents)
    post.write_text(contents)


def rename_image(match: re.Match):
    _, _, name = match.group(0).rpartition("/")
    print(f"\t{match.group(0)} → {name}")
    return name


if __name__ == "__main__":
    main()
