# Text Formatting using Python Function Decorator

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@bold
def format_text(text):
    return text

print(format_text("Hello World"))