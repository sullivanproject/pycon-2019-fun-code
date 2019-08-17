from copy import deepcopy, copy
import random
import sys
import traceback
import os


class CommandError(SyntaxError): pass


def print_help():
    print('''
Usage: python shuffle_me.py [option]
--unit -u\tchar | line
\tchar\tshuffle or sort each characters
\tline\tshuffle or sort each lines
--type -t\tsort | shuffle
\tsort\tremake source to sorting with unicode(utf-8)
\tshuffle\tremake source to randomly shuffle
--help -h\tShow usage message
                ''')


def get_conf():
    args = copy(sys.argv)
    options = {'this_file': args[0]}

    if '--unit' not in args or '-u' not in args:
        options['unit'] = 'char'
    if '--type' not in args or '-t' not in args:
        options['type'] = 'shuffle'

    for idx, arg in enumerate(args):
        if 'unit' not in options.keys() and arg == '--unit' or arg == '-u':
            options['unit'] = args[idx + 1]
        elif 'type' not in options.keys() and arg == '--type' or arg == '-t':
            options['type'] = args[idx + 1]
        elif arg == '--help' or arg == '-h':
            print_help()
            exit(0)

    return options


def read_code(filename):
    rp = open(filename, 'rb')
    org_code = deepcopy(rp.read()).decode('utf-8')
    rp.close()

    return org_code


def write_code(new_code, filename, unit):
    if unit == 'line':
        # If unit is line, new_code's elements does not have new line symbol
        join_token = os.linesep
    else:
        # If unit is char, new line symbol is element of new_code
        join_token = ''
    new_code = join_token.join(new_code).encode('utf-8')
    wp = open(filename, 'wb')
    wp.write(new_code)
    wp.close()


def make_sequence_from_source(org_source, unit):
    if unit == 'char':
        org_source = list(org_source)
    elif unit == 'line':
        if '\r\n' in org_source:
            # For windows or ms-dos
            sep = '\r\n'
        elif '\n' in org_source:
            # For linux ox
            sep = '\n'
        elif '\r' in org_source:
            # For unix or osx or somethings..
            sep = '\r'
        else:
            # I don't know what did I support any new line symbol
            raise SyntaxError('Not supported new line symbol.')
        org_source = org_source.split(sep)
    else:
        raise CommandError('Wrong command!!')

    return org_source


def do_func(org_seq_source, func):
    processed_code = copy(org_seq_source)
    if func == 'sort':
        processed_code.sort()
    elif func == 'shuffle':
        random.shuffle(processed_code)
    else:
        raise CommandError('Wrong command!!')

    return processed_code


def main():
    # 명령절에서 옵션을 받아온다.
    config = get_conf()
    # 자신의 소스코드를 읽어온다.
    code = read_code(config['this_file'])
    # 읽어온 소스코드를 주어진 단위로 쪼갠다.
    code = make_sequence_from_source(code, config['unit'])
    # 만들어진 코드 리스트 단위를 주어진 방법으로 바꾼다.
    code = do_func(code, config['type'])
    # 다시 자신의 소스코드에 덮어씌운다.
    write_code(code, config['this_file'], config['unit'])


if __name__ == "__main__":
    try:
        main()
    except CommandError as e:
        print(str(e))
        print_help()
    except Exception as e:
        traceback.print_tb(e)
