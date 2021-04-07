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
            xmin = str(round(rect["points"][0][0]))
            ymin = str(round(rect["points"][0][1]))
            xmax = str(round(rect["points"][1][0]))
            ymax = str(round(rect["points"][1][1]))

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
        j = 0
        for f in tqdm(list(data_files)):
            j += 1
            if j < 4:
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
