"""Facade example

Facade is a pattern that is used to abstact complex logic into simple one simple 
interface. Often used in large libraries like pandas, langchain, or such.

Can also be used to simplify how your own application uses these libraries. Can 
help isolating your application's dependencies, so it would be easier to change 
from one library to another.
"""

class TextFormatter:
    """Placeholder for a class that can format text to multiple styles."""
    def format_text(self, text, style):
        """Imagine complex formatting logic here.""" 
        return f"{style} formatted text: {text}"

class SpellChecker:
    """Placeholder for a spell checker."""
    def check_spelling(self, text):
        """ Placeholder for spell checking logic"""
        errors = []  # Assume here we would run a function that finds spelling errors.
        if errors:
            return f"Text with errors: {errors}"
        else:
            return "Text is error-free"

class Exporter:
    """Class that can export the text into multiple formats."""
    def export_to_pdf(self, text):
        """Placeholder for PDF conversion"""
        return f"Text exported to PDF"

    def export_to_word(self, text):
        """Placeholder for Word conversion"""
        return "Text exported to Word"

class TextEditorFacade:
    """Facade used to do common tasks with the previously introduced classes."""
    def __init__(self, text):
        self.text = text
        self.formatter = TextFormatter()
        self.spell_checker = SpellChecker()
        self.exporter = Exporter()

    def format_and_check(self, style):
        formatted_text = self.formatter.format_text(self.text, style)
        spell_check_result = self.spell_checker.check_spelling(formatted_text)
        return f"{formatted_text}\nSpell check result: {spell_check_result}"

    def export_document(self, format_type):
        if format_type == 'PDF':
            return self.exporter.export_to_pdf(self.text)
        elif format_type == 'Word':
            return self.exporter.export_to_word(self.text)
        else:
            return "Unsupported format"

def main():
    text = "This is an example text."
    editor = TextEditorFacade(text)
    
    print(editor.format_and_check("Bold"))
    print(editor.export_document("PDF"))
    print(editor.export_document("Word"))

if __name__ == "__main__":
    main()

