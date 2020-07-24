import pathlib
import utils as u
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def tokenize_corpus(corpus_in: pathlib.Path, corpus_out: pathlib.Path) -> None:
    u.assert_folder_is_readable(corpus_in)
    u.ensure_folder_is_writable(corpus_out)
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-in', '--corpus-in',
        help = 'Folder containing the source corpus',
        default = 'd:/corpus_raw')
    parser.add_argument(
        '-out', '--corpus-out',
        help = 'Folder containing the tokenized corpus',
        default = 'd:/corpus_tok')
    args = parser.parse_args()
    print(f'corpus folder (in): {args.corpus_in}')
    print(f'corpus folder (out): {args.corpus_out}')
    tokenize_corpus(pathlib.Path(args.corpus_in), pathlib.Path(args.corpus_out))
