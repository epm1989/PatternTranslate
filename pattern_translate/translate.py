import re
from typing import List, Union, Tuple

from pattern_translate.settings import Setting
from pattern_translate import CodeTrace


class PatternTranslate:
    @CodeTrace.trace(skip=True)
    def __init__(self, pattern: str, rows: Union[str, List[str]]):
        """

        :param pattern: example, "foo %{0} is a %{1}"
        :param rows: list of string | single string | paragraph string
        """
        self.groups = re.findall(Setting.specification, pattern)
        self.lines = rows.split('\n') if isinstance(rows, str) else rows
        self.groups_mapped = self.__create_descriptions
        self.groups_len = len(self.groups)
        self.new_pattern = "^" + re.sub(Setting.specification, Setting.capture_group, pattern) + "$"
        self.new_re = re.compile(self.new_pattern)
        self.output = []

    @property
    def __create_descriptions(self) -> List[str]:
        """
        translate groups of capture to human readable
        :return: list of human readable capture groups
        """
        groups_mapped = []
        for group in self.groups:
            if "S" in group:
                number_of_spaces = re.sub(r'[\{\}%]', '', group).split('S')[-1]
                groups_mapped.append(f"spaces{number_of_spaces}")
            elif "G" in group:
                groups_mapped.append('greedy')
            else:
                groups_mapped.append('normal')
        return groups_mapped

    def fetch_lines(self):
        """
        iterate line by line
        :return: None
        """
        for line in self.lines:
            self.__match_line(line=line)

    @CodeTrace.trace()
    def __match_line(self, line: str = None) -> Tuple[bool, str]:
        """
        compute a first filter by regex
        :param line:
        :return: True|False, matched_line
        """
        result: Union[re.Match, None] = self.new_re.match(line)
        if result:
            return self.seek_spaces_rule(matched_line=result)
        return False, line

    @CodeTrace.trace(quiet=True)
    def seek_spaces_rule(self, matched_line):
        """
        compute a second filter by compliance of spaces
        :param matched_line:
        :return: True|False , matched_line with spaces verified|''
        """
        for i in range(1, self.groups_len + 1):

            if 'spaces' in self.groups_mapped[i - 1]:
                num_spaces_expected = int(self.groups_mapped[i - 1].replace('spaces', ''))
                num_spaces = matched_line.group(i).count(' ')
                if num_spaces != num_spaces_expected:
                    break
        else:
            self.output.append(matched_line.group(0))
            if self.output:
                return True, self.output[-1]
        return False, ''
