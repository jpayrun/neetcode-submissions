class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = {}
        mag = {}
        for c in ransomNote:
            note[c] = note.get(c, 0) + 1
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        for key in note:
            if key in mag and mag[key] >= note[key]:
                continue
            else:
                return False
        return True