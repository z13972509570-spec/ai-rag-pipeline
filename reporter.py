"""Report generator"""
import json
from typing import Any, Dict


class Reporter:
    """Report generator for RAG pipeline"""
    
    def __init__(self, format: str = "text"):
        self.format = format
    
    def generate(self, data: Any) -> str:
        """Generate report from data
        
        Args:
            data: Data to generate report from
            
        Returns:
            Formatted report string
        """
        if self.format == "json":
            return json.dumps(data, indent=2, ensure_ascii=False)
        elif self.format == "markdown":
            return self._to_markdown(data)
        return str(data)
    
    def _to_markdown(self, data: Dict) -> str:
        """Convert data to markdown format
        
        Args:
            data: Data dictionary
            
        Returns:
            Markdown formatted string
        """
        md = "# Analysis Report\n\n"
        for key, value in data.items():
            md += f"- **{key}**: {value}\n"
        return md
