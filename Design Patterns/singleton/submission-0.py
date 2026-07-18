class Singleton:

    inst = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls.inst:
            cls.inst = super(Singleton, cls).__new__(cls)
            cls.value = None
        return cls.inst

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
