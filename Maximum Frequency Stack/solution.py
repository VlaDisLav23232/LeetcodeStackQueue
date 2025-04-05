from collections import deque, defaultdict

class FreqStack:
    """FREQSTACK CLASS"""
    def __init__(self):
        self.val_freq = defaultdict(int)
        self.freq_stack = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """PUSH METHOD"""
        self.val_freq[val] += 1
        freq = self.val_freq[val]
        self.freq_stack[freq].append(val)
        if freq > self.max_freq:
            self.max_freq = freq

    def pop(self) -> int:
        """POP METHOD"""
        val = self.freq_stack[self.max_freq].pop()
        self.val_freq[val] -= 1
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        return val
