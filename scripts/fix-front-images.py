import re
import shutil
from pathlib import Path

CONTENT_PATH = "/Users/antonz/projects/antonz.ru/content/posts"
IMAGE_SRC_PATH = "/Users/antonz/projects/antonz.ru.ghost"
IMAGE_RE = re.compile(r'image = "/images/([^"]+)"')


def main():
    path = Path(CONTENT_PATH)
    dirs = (p for p in path.iterdir() if p.is_dir())
    for yeardir in dirs:
        postdirs = (p for p in yeardir.iterdir() if p.is_dir())
        for postdir in postdirs:
            post = Path(postdir, "index.md")
            print(post)
            copy_image(post)
            rename_image(post)


def copy_image(post: Path):
    contents = post.read_text()
    match = IMAGE_RE.search(contents)
    if not match:
        return ""
    image = match.group(1)
    frompath = Path(IMAGE_SRC_PATH, "content/images", image)
    topath = imagepath(post, image)
    shutil.copy(frompath, topath)
    print(f"\t{frompath}")
    print(f"\t→ {topath}")
    return topath.name


def rename_image(post: Path):
    def rename(match: re.Match):
        _, _, name = match.group(1).rpartition("/")
        base_url = post.parent.name
        url = f'image = "/{base_url}/{name}"'
        print(f"\t{url}")
        return url

    contents = post.read_text()
    contents = IMAGE_RE.sub(rename, contents)
    post.write_text(contents)


def imagepath(post: Path, image: str):
    _, _, name = image.rpartition("/")
    return Path(post.parent, name)


if __name__ == "__main__":
    main()
