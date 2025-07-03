import os

def count_images(root_dir):
    """
    Traverse train/ and val/ subdirectories, 
    count how many images are in each class folder.
    """
    for split in ['train', 'val']:
        for cls in ['offensive', 'non_offensive']:
            path = os.path.join(root_dir, split, cls)
            if not os.path.isdir(path):
                print(f"WARNING: {path} does not exist")
                continue
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            print(f"{split}/{cls}: {len(files)} images")

def rename_images(root_dir, split, cls_prefix):
    """
    Rename all files in data/<split>/<cls_prefix>/ 
    to a standardized pattern:
      e.g. offensive_0001.jpg, offensive_0002.png, ...
    """
    folder = os.path.join(root_dir, split, cls_prefix)
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        return

    files = sorted(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    for idx, fname in enumerate(files, 1):
        ext = os.path.splitext(fname)[1].lower()  # keep original extension
        new_name = f"{cls_prefix[:3]}_{idx:04d}{ext}"
        src = os.path.join(folder, fname)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
    print(f"Renamed {len(files)} files in {split}/{cls_prefix} to {cls_prefix[:3]}_XXXX.jpg/png etc.")

if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), 'data')
    print("Image counts before renaming:")
    count_images(base)

    # Uncomment the two lines below to rename images in each folder
    # rename_images(base, 'train', 'offensive')
    # rename_images(base, 'train', 'non_offensive')
    # rename_images(base, 'val', 'offensive')
    # rename_images(base, 'val', 'non_offensive')

    # After renaming, check counts again:
    # print("\nImage counts after renaming:")
    # count_images(base)
