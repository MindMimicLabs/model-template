import pathlib
import utils as u
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def train_model(corpus_in: pathlib.Path, state_folder: pathlib.Path) -> None:
    u.assert_folder_is_readable(corpus_in)
    u.ensure_folder_is_writable(state_folder.joinpath('./weights'))
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-in', '--corpus-in',
        help = 'Folder containing the training corpus',
        default = 'd:/corpus_train')
    parser.add_argument(
        '-s', '--state-folder',
        help = 'Folder containing the state',
        default = 'd:/state')
    args = parser.parse_args()
    print(f'corpus folder: {args.corpus_in}')
    print(f'state folder: {args.state_folder}')
    train_model(pathlib.Path(args.corpus_in), pathlib.Path(args.state_folder))
