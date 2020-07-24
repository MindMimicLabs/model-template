import pathlib
import utils as u
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def extract_fold(corpus_in: pathlib.Path, corpus_out: pathlib.Path, subset: pathlib.Path) -> None:
    u.assert_folder_is_readable(corpus_in)
    u.assert_file_is_readable(subset)
    u.ensure_folder_is_writable(corpus_out)
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-in', '--corpus-in',
        help = 'Folder containing the full corpus',
        default = 'd:/corpus_tok')
    parser.add_argument(
        '-out', '--corpus-out',
        help = 'Folder containing the subsetted corpus',
        default = 'd:/corpus_out')
    parser.add_argument(
        '-sub', '--subset',
        help = 'CSV file describing the subset needed',
        default = 'd:/state/sub/hypertune.train.csv')
    args = parser.parse_args()
    print(f'corpus folder (in): {args.corpus_in}')
    print(f'corpus folder (out): {args.corpus_out}')
    print(f'subset file: {args.subset}')
    extract_fold(pathlib.Path(args.corpus_in), pathlib.Path(args.corpus_out), pathlib.Path(args.subset))
