class RegexEngine:

    def __init__(self, inp):
        self.pattern, self.stringer = inp.split("|")

    @staticmethod
    def compare_equal(pattern, stringer):
        for i, e in enumerate(pattern):
            if e not in [stringer[i], '.']:
                return False
        else:
            return True

    def compare_different(self):
        strin_len = len(self.stringer)
        idx = 0
        shift = len(self.pattern)
        # print(self.pattern)
        while True:
            if shift > strin_len:
                return False
            else:
                if self.compare_equal(self.pattern, self.stringer[idx: shift]):
                    return True
                else:
                    idx += 1
                    shift += 1

    def compare_meta(self):
        curr_sign = ""
        meta_start = 0
        mode = "normal"
        for i, e in enumerate(self.pattern):
            if mode == "normal":
                if e in ["?", "*", "+"]:
                    mode = e
                    curr_sign = self.pattern[i - 1]
                    meta_start = i
            if mode == "?":
                if self.stringer.count(curr_sign) > 1:
                    return False
                elif self.stringer.count(curr_sign) == 0:
                    self.pattern = self.pattern[:meta_start - 1] + self.pattern[meta_start + 1:]
                    return self.compare_different()
                elif self.stringer.count(curr_sign) == 1:
                    self.pattern = self.pattern[:meta_start] + self.pattern[meta_start + 1:]
                    return self.compare_different()
            elif mode == "*":
                if curr_sign == ".":
                    curr_sign = self.replace_dot(meta_start)
                self.pattern = self.pattern[:meta_start - 1] + curr_sign * self.stringer.count(
                    curr_sign) + self.pattern[meta_start + 1:]
                if not self.starter_ender():
                    return False
                self.pattern = self.pattern.replace("^", "")
                self.pattern = self.pattern.replace("$", "")
                return self.compare_different()

            elif mode == "+":
                if curr_sign == ".":
                    curr_sign = self.replace_dot(meta_start)
                if self.stringer.count(curr_sign) == 0:
                    return False
                else:
                    self.pattern = self.pattern[:meta_start - 1] + curr_sign * self.stringer.count(
                        curr_sign) + self.pattern[meta_start + 1:]
                    if not self.starter_ender():
                        return False
                    self.pattern = self.pattern.replace("^", "")
                    self.pattern = self.pattern.replace("$", "")
                    return self.compare_different()

    def replace_dot(self, start):
        if start == 1:
            return self.stringer[0]
        else:
            return self.stringer[self.stringer.index(self.pattern[start - 2]) + 1]

    def starter_ender(self):
        if any([("^" in self.pattern and self.pattern[1] not in [self.stringer[0], '.']),
                ("$" in self.pattern and self.pattern[-2] not in [self.stringer[-1], '.']),
                ("^" in self.pattern and "$" in self.pattern and len(self.pattern) - 2 != len(self.stringer))]):
            return False
        else:
            return True

    def compare(self):
        if any(["?" in self.pattern, "*" in self.pattern, "+" in self.pattern]) and '\\' not in self.pattern:
            return self.compare_meta()
        else:
            self.pattern = self.pattern.replace('\\?', '?').replace('\\+', '+').replace('\\*', '*').replace('\\.', '.').replace('\\\\', '\\')
            if not self.starter_ender():
                return False
            self.pattern = self.pattern.replace("^", "")
            self.pattern = self.pattern.replace("$", "")
            return self.compare_different()


rgx = RegexEngine(input())

print(rgx.compare())


class RegexEngine:

    def __init__(self, inp):
        self.pattern, self.stringer = inp.split("|")
        self.matched = False

    def compare_equal(self, pattern, stringer):
        for i, e in enumerate(pattern):
            if e not in [stringer[i], '.']:
                return False
        else:
            return True

    def compare_different(self):
        strin_len = len(self.stringer)
        idx = 0
        shift = len(self.pattern)
        # print(self.pattern)
        while True:
            if shift > strin_len:
                return False
            else:
                if self.compare_equal(self.pattern, self.stringer[idx: shift]):
                    return True
                else:
                    idx += 1
                    shift += 1

    def compare_meta(self):
        curr_sign = ""
        meta_start = 0
        shift = 0
        mode = "normal"
        for i, e in enumerate(self.pattern):
            if mode == "normal":
                if e in ["?", "*", "+"]:
                    mode = e
                    curr_sign = self.pattern[i - 1]
                    # print(curr_sign)
                    meta_start = i
                    # continue
            if mode == "?":
                if self.stringer.count(curr_sign) > 1:

                    return False
                elif self.stringer.count(curr_sign) == 0:

                    self.pattern = self.pattern[:meta_start - 1] + self.pattern[meta_start + 1:]
                    # print(self.pattern)
                    return self.compare_different()
                elif self.stringer.count(curr_sign) == 1:

                    self.pattern = self.pattern[:meta_start] + self.pattern[meta_start + 1:]
                    return self.compare_different()
            elif mode == "*":
                if curr_sign == ".":
                    curr_sign = self.replace_dot(meta_start)
                    # print(curr_sign)

                self.pattern = self.pattern[:meta_start - 1] + curr_sign * self.stringer.count(
                    curr_sign) + self.pattern[meta_start + 1:]
                if not self.starter_ender():
                    return False
                self.pattern = self.pattern.replace("^", "")
                self.pattern = self.pattern.replace("$", "")
                return self.compare_different()

            elif mode == "+":

                if curr_sign == ".":
                    curr_sign = self.replace_dot(meta_start)
                if self.stringer.count(curr_sign) == 0:
                    return False
                else:

                    self.pattern = self.pattern[:meta_start - 1] + curr_sign * self.stringer.count(
                        curr_sign) + self.pattern[meta_start + 1:]

                    if not self.starter_ender():
                        return False
                    self.pattern = self.pattern.replace("^", "")
                    self.pattern = self.pattern.replace("$", "")
                    return self.compare_different()

    def replace_dot(self, start):
        if start == 1:
            return self.stringer[0]
        else:
            return self.stringer[self.stringer.index(self.pattern[start - 2]) + 1]

    def starter_ender(self):
        if any([("^" in self.pattern and self.pattern[1] not in [self.stringer[0], '.']),
                ("$" in self.pattern and self.pattern[-2] not in [self.stringer[-1], '.']),
                ("^" in self.pattern and "$" in self.pattern and len(self.pattern) - 2 != len(self.stringer))]):
            return False
        else:
            return True

    def compare(self):

        if any(["?" in self.pattern, "*" in self.pattern, "+" in self.pattern]) and '\\' not in self.pattern:
            return self.compare_meta()
        else:

            self.pattern = self.pattern.replace('\\?', '?').replace('\\+', '+').replace('\\*', '*').replace('\\.',
                                                                                                            '.').replace(
                '\\\\', '\\')
            # print(self.pattern)
            if not self.starter_ender():
                return False
            self.pattern = self.pattern.replace("^", "")
            self.pattern = self.pattern.replace("$", "")
            return self.compare_different()


rgx = RegexEngine(input())

print(rgx.compare())







