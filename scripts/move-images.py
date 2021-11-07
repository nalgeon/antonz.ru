import re
import shutil
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
            copy_images(post)


def copy_images(post: Path):
    contents = post.read_text()
    images = IMAGE_RE.findall(contents)
    for image in images:
        print(f"\t{image}")
        copy_image(post, image)


def copy_image(post: Path, image: str):
    frompath = Path(IMAGE_SRC_PATH, image[1:])
    topath = imagepath(post, image)
    shutil.copy(frompath, topath)
    print(f"\t{frompath}")
    print(f"\t→ {topath}")
    return topath.name


def imagepath(post: Path, image: str):
    _, _, name = image.rpartition("/")
    return Path(post.parent, name)


if __name__ == "__main__":
    main()
