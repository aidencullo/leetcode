class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        current_line_width = 0
        lines = 1
        for c in s:
            width = widths[ord(c) - 97]
            if current_line_width + width > 100:
                lines += 1
                current_line_width = width
            else:
                current_line_width += width
                
        return [lines, current_line_width]
