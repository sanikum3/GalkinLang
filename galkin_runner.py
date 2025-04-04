import sys
from galkin_lang import galkin_to_python

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python galkin_runner.py файл.gl")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            gl_code = f.read()
        
        python_code = galkin_to_python(gl_code)
        exec(python_code)
    
    except FileNotFoundError:
        print(f"Ошибка: Файл '{sys.argv[1]}' не найден!")
    except Exception as e:
        print(f"Галкин-Ошибка: {e}")