from io import BytesIO
import tokenize

GALKIN_REPLACEMENTS = {
    # Управляющие конструкции
    "еслигалкин": "if",
    "иначежегалкин": "elif",  # Добавлено
    "илижегалкин": "else",
    "глиномескин": "while",
    "повторялкин": "for",
    "циклпрерывалкин": "break",  # Новое
    "продолжалкин": "continue",  # Новое
    "эксперименталкин": "try",
    "поймалкин": "except",
    "финалялкин": "finally",  # Новое
    "взвегалкин": "raise",
    
    # Функции и классы
    "функциональкин": "def",
    "класскин": "class",
    "возвращалкин": "return",
    "лямбдалкин": "lambda",  # Новое
    "самокалкин": "self",  # Новое
    
    # Логические значения
    "галкин": "True",
    "лжегалкин": "False",
    "безгалкина": "None",
    
    # Ввод-вывод
    "выводилкин": "print",
    "вводилкин": "input",
    "открывалкин": "open",  # Новое
    
    # Импорты
    "импортялкин": "import",
    "изъялкин": "from",
    "какгалкин": "as",  # Новое
    
    # Типы данных
    "списокалкин": "list",  # Новое
    "словаралкин": "dict",  # Новое
    "множествокин": "set",  # Новое
    
    # Операторы
    "негалкин": "not",
    "игалкин": "and",
    "илигалкин": "or",
    "ввозгалкин": "in",  # Новое
    "нетвгалкине": "not in",  # Новое
    
    # Асинхронность
    "асинхроникин": "async",  # Новое
    "ожидалкин": "await",  # Новое
}

def galkin_to_python(code: str) -> str:
    """Преобразует GalkinLang-код в Python."""
    result = []
    tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
    
    for tok in tokens:
        if tok.type == tokenize.NAME and tok.string in GALKIN_REPLACEMENTS:
            new_tok = (tokenize.NAME, GALKIN_REPLACEMENTS[tok.string])
            result.append(new_tok)
        else:
            result.append((tok.type, tok.string))
    
    return tokenize.untokenize(result).decode('utf-8')