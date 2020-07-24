import pathlib
import utils as u
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def hyper_tune_model(train_in: pathlib.Path, test_in: pathlib.Path, state_folder: pathlib.Path) -> None:
    u.assert_folder_is_readable(train_in)
    u.assert_folder_is_readable(test_in)
    u.ensure_folder_is_writable(state_folder)
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-train', '--train-in',
        help = 'Folder containing the training corpus',
        default = 'd:/corpus_train')
    parser.add_argument(
        '-test', '--test-in',
        help = 'Folder containing the test corpus',
        default = 'd:/corpus_test')
    parser.add_argument(
        '-s', '--state-folder',
        help = 'Folder containing the state',
        default = 'd:/state')
    args = parser.parse_args()
    print(f'corpus folder (training): {args.train_in}')
    print(f'corpus folder (test): {args.test_in}')
    print(f'state folder: {args.state_folder}')
    hyper_tune_model(pathlib.Path(args.train_in), pathlib.Path(args.test_in), pathlib.Path(args.state_folder))
