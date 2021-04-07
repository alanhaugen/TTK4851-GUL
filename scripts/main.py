import os
import json
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed


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


def main(dir_files, max_workers):
    assert os.path.isdir(dir_files)
    data_files = sorted((os.path.join(dir_files, f)
                         for f in os.listdir(dir_files)
                         if os.path.isfile(os.path.join(dir_files, f)) and f.endswith(".json")))
    print('Input is directory with', len(data_files), '.json files:', dir_files)

    if max_workers is None:
        print('Working with a single process, maybe set `--max-workers`?')
        for f in tqdm(list(data_files)):
            convert(f, dir_files)
    else:
        print('Working in parallel using', max_workers, 'processses')
        with tqdm(total=len(data_files)) as progress_bar:
            with ProcessPoolExecutor(max_workers=max_workers) as ex:
                futures = {ex.submit(convert, f, dir_files): f
                           for f in list(data_files)}

                for f in as_completed(futures):
                    progress_bar.update(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', required=True,
                        help='file or dir')
    parser.add_argument('--max-workers', type=int,
                        help='max parallel processes')

    args = parser.parse_args()

    main(args.input,
         max_workers=args.max_workers)
