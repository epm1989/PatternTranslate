import sys

from pattern_translate import PatternTranslate

if __name__ == '__main__':
    if len(sys.argv) != 2:
        msg_error = "please check the arguments \n" \
                    "Example:\n\n" \
                    '\tcat input.txt| python main.py "foo %{0} is a %{1} the is %{2S2} in or %{3G} foo" > output.txt\n'
        exit(msg_error)
    f = open("output.txt", 'w')
    f.close()
    lines = []
    for line in sys.stdin:
        lines.append(line.replace('\n', ''))

    pattern: str = sys.argv[1]

    if lines:
        alert = PatternTranslate(pattern, lines)
        alert.fetch_lines()

        for output in alert.output:
            sys.stdout.write(f"{output}\n")
    else:
        sys.exit('Error read file')
