class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args
        self.steps += inc

