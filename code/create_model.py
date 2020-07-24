import pathlib
import utils as u
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def create_model(state_folder: pathlib.Path) -> None:
    u.ensure_folder_is_writable(state_folder.joinpath('./weights'))
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-s', '--state-folder',
        help = 'Folder containing the state',
        default = 'd:/state')
    args = parser.parse_args()
    print(f'state folder: {args.state_folder}')
    create_model(pathlib.Path(args.state_folder))
