import os
import json
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image


def convert(file, dir_files):
    filename = os.path.basename(file).split(".")[0]
    with open(file) as f:
        data = json.load(f)

        f_txt = open(os.path.join(dir_files, filename + ".txt"), "w")

        for rect in data["shapes"]:
            output = ""
            yolo_class = rect["label"]
            x1 = round(rect["points"][0][0])
            y1 = round(rect["points"][0][1])
            x2 = round(rect["points"][1][0])
            y2 = round(rect["points"][1][1])

            xmin = str(min(x1,x2))
            xmax = str(max(x1,x2))
            ymin = str(min(y1,y2))
            ymax = str(max(y1,y2))

            output += yolo_class
            output += " " + xmin
            output += " " + ymin
            output += " " + xmax
            output += " " + ymax

            f_txt.write(output + "\n")


def convert_yolo(file, dir_files):
    file_path = os.path.basename(file)
    with open(file) as f:
        img_path = os.path.join(dir_files, file_path.split(".")[0] + ".png")
        img = Image.open(img_path)
        max_width = float(img.size[0])
        max_height = float(img.size[1])

        yolo_file = open(os.path.join(dir_files, file_path + ".yolo"), "w")

        for line in f:
            class_id, x_min, y_min, x_max, y_max = (int(s) for s in line.split())

            x_mid = (x_min + x_max) / 2.0
            y_mid = (y_min + y_max) / 2.0

            u = x_mid / max_width
            v = y_mid / max_height

            rect_width = x_max - x_min
            rect_height = y_max - y_min

            w = rect_width / max_width
            h = rect_height / max_height

            output = " ".join([str(class_id), str(u), str(v), str(w), str(h)]) + "\n"
            yolo_file.write(output)


def main(dir_files, max_workers, to_yolo):
    assert os.path.isdir(dir_files)
    if not to_yolo:
        filetype = ".json"
    else:
        filetype = ".txt"
    data_files = sorted((os.path.join(dir_files, f)
                             for f in os.listdir(dir_files)
                             if os.path.isfile(os.path.join(dir_files, f)) and f.endswith(filetype)))
    print('Input is directory with', len(data_files), " '", filetype, "' files:", dir_files)

    if max_workers is None:
        print('Working with a single process, maybe set `--max-workers`?')
        if not to_yolo:
            for f in tqdm(list(data_files)):
                convert(f, dir_files)
        else:
             for f in tqdm(list(data_files)):
                convert_yolo(f, dir_files)
    else:
        print('Working in parallel with ', max_workers, ' processses')
        with tqdm(total=len(data_files)) as progress_bar:
            with ProcessPoolExecutor(max_workers=max_workers) as ex:
                if not to_yolo:
                    futures = {ex.submit(convert, f, dir_files): f
                           for f in list(data_files)}
                else:
                    futures = {ex.submit(convert_yolo, f, dir_files): f
                           for f in list(data_files)}

                for f in as_completed(futures):
                    progress_bar.update(1)

def arg_to_bool(s):
    if isinstance(s, bool):
        return s
    elif s.lower() in ('1', 'yes', 'y', 'true', 't'):
        return True
    else:
        return False

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', required=True,
                        help='file or dir')
    parser.add_argument('--max-workers', type=int,
                        help='max parallel processes')
    parser.add_argument('--to-yolo', type=arg_to_bool, nargs='?', default=False,
                        help='arg 1/yes/y/true/t if converting from our other format to yolo')

    args = parser.parse_args()

    main(args.input,
         max_workers=args.max_workers, to_yolo=args.to_yolo)
