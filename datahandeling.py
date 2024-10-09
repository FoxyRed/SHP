import sqlite3
from typing import Optional, List, Tuple

def empty_database() -> None:
    try:
        with sqlite3.connect('printer_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS prints')
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS prints (
                id INTEGER PRIMARY KEY,
                name TEXT,
                kind TEXT,
                printtime INTEGER,
                sl_approved BOOLEAN,
                sl_checked BOOLEAN,
                advanced INTEGER,
                hacked BOOLEAN,
                successful_drawn REAL
            )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def initialize_database() -> None:
    try:
        with sqlite3.connect('printer_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS prints (
                id INTEGER PRIMARY KEY,
                name TEXT,
                kind TEXT,
                printtime INTEGER,
                sl_approved BOOLEAN,
                sl_checked BOOLEAN,
                advanced INTEGER,
                hacked BOOLEAN,
                successful_drawn REAL
            )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def map_goal_lvl_to_kind(goal_lvl: int) -> str:
    kind_mapping = {
        1: "Basic",
        2: "Standard Electronics",
        3: "Advanced Electronics",
        4: "Mechanical"
    }
    return kind_mapping.get(goal_lvl, "Unknown")

def add_data_point(name: str, kind_int: int, printtime: int, sl_approved: Optional[bool] = None, sl_checked: Optional[bool] = None, advanced: Optional[int] = None, hacked: Optional[bool] = None, successful_drawn: Optional[float] = None) -> None:
    kind = map_goal_lvl_to_kind(kind_int)
    if kind == "Unknown":
        raise ValueError("Invalid goal level")

    try:
        with sqlite3.connect('printer_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO prints (name, kind, printtime, sl_approved, sl_checked, advanced, hacked, successful_drawn)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, kind, printtime, sl_approved, sl_checked, advanced, hacked, successful_drawn))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_names_by_kind(kind: str) -> Tuple[List[str], List[Tuple]]:
    try:
        with sqlite3.connect('printer_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prints WHERE kind = ?', (kind,))
            fulldata = cursor.fetchall()
            names = [el[1] for el in fulldata]
        return names, fulldata
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return [], []

# Example usage:
if __name__ == "__main__":
    initialize_database()
    add_data_point("Example", 2, 120, True, False, 3, True, 95.5)
    names, data = get_names_by_kind("Standard Electronics")
    print(names)
    print(data)
