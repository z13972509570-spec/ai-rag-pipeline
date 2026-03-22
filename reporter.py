import json

class Reporter:
    """Report generator"""
    
    def __init__(self, format="text"):
        self.format = format
    
    def generate(self, data) -> str:
        if self.format == "json":
            return json.dumps(data, indent=2)
        elif self.format == "markdown":
            return self._to_markdown(data)
        return str(data)
    
    def _to_markdown(self, data) -> str:
        md = "# Analysis Report\n\n"
        for key, value in data.items():
            md += `‹ */{key}*: {value}\n"
        return md
