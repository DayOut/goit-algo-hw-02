import os
import shutil
import argparse


def copy_and_sort_files_recursively(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивний виклик для вкладених директорій
            copy_and_sort_files_recursively(item_path, dest_dir)
        else:
            # Копіювання файлів у відповідну піддиректорію за розширенням
            file_extension = item.split('.')[-1] if '.' in item else 'no_extension'
            dest_path = os.path.join(dest_dir, file_extension)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            try:
                shutil.copy(item_path, dest_path)
                print(f"Copied {item_path} to {dest_path}")
            except Exception as e:
                print(f"Failed to copy {item_path} to {dest_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("src_dir", help="Source directory to copy files from")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Destination directory to copy files to")
    args = parser.parse_args()

    if not os.path.exists(args.src_dir):
        print(f"Source directory {args.src_dir} does not exist.")
        return

    copy_and_sort_files_recursively(args.src_dir, args.dest_dir)


if __name__ == "__main__":
    main()